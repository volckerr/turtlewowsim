class Ignite:
    def __init__(self, env):
        self._uptimes = [0, 0, 0, 0, 0] # each index is number of ignite stacks
        self._num_ticks = [0, 0, 0, 0, 0]

        self.active = False
        self.env = env
        self.cum_dmg = 0
        self.last_crit_time = 0
        self.ticks_left = 0
        self.owner = None
        self.stacks = 0
        self.ticks = []
        self.power_infusion = False
        self.crit_this_window = False
        self.contains_scorch = False
        self.contains_fireblast = False
        self.ignite_id = 0

    def is_suboptimal(self):
        return self.contains_scorch or self.contains_fireblast

    def refresh(self, mage, dmg, spell_name):
        self.check_for_drop()
        self.last_crit_time = self.env.now

        if self.active:
            if self.stacks <= 4:
                self.cum_dmg += dmg
                self.stacks += 1
                if spell_name.lower() == 'scorch':
                    self.contains_scorch = True
                elif spell_name.lower() == 'fireblast':
                    self.contains_fireblast = True

            if self.owner.power_infusion.active:
                self.power_infusion = True

            self.ticks_left = 2
        else:  # new ignite
            self.active = True
            self.cum_dmg = dmg
            self.stacks = 1
            self.owner = mage
            self.ticks_left = 2

            # start tick thread
            self.env.process(self.run(self.ignite_id))

    def drop(self):
        self.owner.print(f"Ignite dropped")
        self.active = False
        self.owner = None
        self.cum_dmg = 0
        self.stacks = 0
        self.power_infusion = False
        self.ticks_left = 0
        self.last_crit_time = 0
        self.contains_scorch = False
        self.contains_fireblast = False
        self.ignite_id += 1  # increment ignite id

    def check_for_drop(self):
        # only check last crit time if ignite is active and down to 0 ticks
        if self.active and self.ticks_left == 0:
            # check if 4 seconds have passed since last crit
            if self.env.now - self.last_crit_time > 4:
                self.drop()

    def monitor(self):
        while True:
            # check if ignite dropped in last 0.05 sec
            self.check_for_drop()

            if self.active:
                for i in range(self.stacks):
                    self._uptimes[i] += 0.05

            yield self.env.timeout(0.05)

    def run(self, ignite_id):
        while self.ignite_id == ignite_id:
            yield self.env.timeout(2)
            if self.ticks_left > 0:
                self.ticks_left -= 1
                self._do_dmg()

    def _do_dmg(self):
        tick_dmg = self.cum_dmg * 0.2

        if self.env.debuffs.coe:
            tick_dmg *= 1.1  # ignite double dips on CoE

        if self.env.debuffs.nightfall:
            tick_dmg *= 1.15

        if self.power_infusion:
            tick_dmg *= 1.2

        tick_dmg *= 1 + self.env.debuffs.scorch_stacks * 0.03  # ignite double dips on imp.scorch
        if self.owner.dmf:
            tick_dmg *= 1.1  # ignite double dips on DMF

        tick_dmg = int(tick_dmg)
        if self.env.print:
            time_left = self.last_crit_time + 4 - self.env.now
            self.env.p(
                f"{self.env.time()} - ({self.owner.name}) ({self.stacks}) ignite tick {tick_dmg} ticks remaining {self.ticks_left} time left {round(time_left, 2)}s")

        self._num_ticks[self.stacks - 1] += 1
        self.env.meter.register(self.owner, tick_dmg)
        self.env.total_ignite_dmg += tick_dmg
        self.ticks.append(tick_dmg)

    @property
    def uptime_gte_1_stack(self):
        return self._uptimes[0] / self.env.now

    @property
    def uptime_gte_2_stacks(self):
        return self._uptimes[1] / self.env.now

    @property
    def uptime_gte_3_stacks(self):
        return self._uptimes[2] / self.env.now

    @property
    def uptime_gte_4_stacks(self):
        return self._uptimes[3] / self.env.now

    @property
    def uptime_5_stacks(self):
        return self._uptimes[4] / self.env.now

    @property
    def avg_tick(self):
        if not self.ticks:
            return 0
        return sum(self.ticks) / len(self.ticks)

    @property
    def max_tick(self):
        return max(self.ticks) if self.ticks else 0

    @property
    def num_ticks(self):
        return len(self.ticks)

    @property
    def num_1_stack_ticks(self):
        return self._num_ticks[0]

    @property
    def num_2_stack_ticks(self):
        return self._num_ticks[1]

    @property
    def num_3_stack_ticks(self):
        return self._num_ticks[2]

    @property
    def num_4_stack_ticks(self):
        return self._num_ticks[3]

    @property
    def num_5_stack_ticks(self):
        return self._num_ticks[4]

    def _justify(self, string):
        return string.ljust(30, ' ')

    def report(self):
        print(f"{self._justify('Ignite uptime')}: {round(self.uptime_gte_1_stack * 100, 2)}%")
        print(f"{self._justify('>=3 stack ignite uptime')}: {round(self.uptime_gte_3_stacks * 100, 2)}%")
        print(f"{self._justify('5 stack ignite uptime')}: {round(self.uptime_5_stacks * 100, 2)}%")
        print(f"{self._justify('Num Ticks')}: {len(self.ticks)}")
        print(f"{self._justify('Average tick')}: {round(self.avg_tick, 2)}")
        print(f"{self._justify('Max Tick')}: {max(self.ticks)}")
