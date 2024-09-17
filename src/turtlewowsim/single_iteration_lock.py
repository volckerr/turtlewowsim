from sim.env import Environment
from sim.warlock import Warlock
from sim.character import CooldownUsages
from sim.warlock_options import WarlockOptions
from sim.warlock_talents import SMRuin, DSRuin

locks = []
num_locks = 1

for i in range(num_locks):
    lock = Warlock(name=f'lock{i}', sp=1005, crit=30, hit=11, tal=DSRuin, opts=WarlockOptions())
    lock.corruption_agony_shadowbolt(cds=CooldownUsages(reos=1))
    locks.append(lock)

    #lock = Warlock(name=f'immolate_lock{i}', sp=1005, crit=30.73, hit=10, tal=DSRuin, opts=WarlockOptions())
    #lock.corruption_agony_immolate_shadowbolt(cds=CooldownUsages(reos=1))
    #locks.append(lock)

env = Environment(print_dots=False, permanent_cos=True)
env.add_characters(locks)
env.run(until=60)
env.meter.report()
