from sim.simulation import Simulation
from sim.warlock import Warlock
from sim.warlock_options import WarlockOptions
from sim.character import CooldownUsages
from sim.warlock_talents import SMRuin, DSRuin

locks = []
num_locks = 1

for i in range(num_locks):
    lock = Warlock(name=f'C_A_noimmo_lock{i}', sp=1005, crit=30, hit=11, tal=DSRuin, opts=WarlockOptions())
    lock.corruption_agony_shadowbolt(cds=CooldownUsages(reos=1))
    locks.append(lock)

    lock = Warlock(name=f'C_A_immolate_lock{i}', sp=1005, crit=30, hit=11, tal=DSRuin, opts=WarlockOptions())
    lock.corruption_agony_immolate_shadowbolt(cds=CooldownUsages(reos=1))
    locks.append(lock)

sim = Simulation(characters=locks)
sim.run(iterations=1000, duration=60)
sim.detailed_report()
sim.histogram_report_individual()
sim.histogram_report_overlay()
