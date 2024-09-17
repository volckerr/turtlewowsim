from sim.env import Environment
from sim.mage import Mage
from sim.simulation import Simulation
from sim.mage_talents import FireMageTalents

mages = []
num_mages = 3

for i in range(num_mages):
    fm = Mage(name=f'mage{i}', sp=1009, crit=33.17, hit=16, tal=FireMageTalents)
    fm.smart_scorch()
    mages.append(fm)

sim = Simulation(characters=mages)
sim.run(iterations=1000, duration=180)
sim.detailed_report()
