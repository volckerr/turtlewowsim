# turtlewowsim

Simulation for Turtle WoW that currently supports Fire/Frost Mages and Warlocks.

## Installation

Need python 3.10 or later

For windows users, run installer.bat


`python simulations/mage.py`

`python simulations/mage.py`

## Usage
For a single iteration:

``` python
from sim.env import Environment
from sim.mage import Mage
from sim.mage_options import MageOptions
from sim.mage_talents import FireMageTalents

mages = []
num_mages = 3

for i in range(num_mages):
    tal = FireMageTalents
    fm = Mage(name=f'mage{i}', sp=1009, crit=33.17, hit=16, tal=tal,
              opts=MageOptions(extend_ignite_with_scorch=True))
    fm.smart_scorch()
    mages.append(fm)

env = Environment()
env.add_characters(mages)
env.run(until=180)
env.meter.report()
```
or
``` python
from sim.env import Environment
from sim.warlock import Warlock
from sim.warlock_options import WarlockOptions
from sim.warlock_talents import SMRuin

locks = []
num_locks = 3

for i in range(num_locks):
    fm = Warlock(name=f'lock{i}', sp=1009, crit=33.17, hit=16, tal=SMRuin, opts=WarlockOptions())
    fm.corruption_immolate_shadowbolt()
    locks.append(fm)

env = Environment(print_dots=True)
env.add_characters(locks)
env.run(until=180)
env.meter.report()
```

You will get an output like this
```
[2.1] - (mage0) scorch (1.6 cast) 825
[2.8] - (mage1) scorch (1.6 cast) 847
[3.7] - (mage0) scorch (1.6 cast) **1254**
[4.4] - (mage1) scorch (1.6 cast) **1333**
[5.3] - (mage0) scorch (1.6 cast) 925
[5.7] - (mage0) (2) ignite tick 654 ticks remaining 1 time left 2.74s
[6.0] - (mage1) scorch (1.6 cast) **1396**
[7.7] - (mage0) (3) ignite tick 1007 ticks remaining 1 time left 2.34s
[8.4] - (mage0) fireball (3.1 cast) **3574**
[9.1] - (mage1) fireball (3.1 cast) 2455
[9.7] - (mage0) (4) ignite tick 1911 ticks remaining 1 time left 2.7s
[11.5] - (mage0) fireball (3.1 cast) **3519**
[11.7] - (mage0) (5) ignite tick 2802 ticks remaining 1 time left 3.8s
[12.2] - (mage1) fireball (3.1 cast) **3577**
[13.7] - (mage0) (5) ignite tick 2802 ticks remaining 1 time left 2.54s
[14.6] - (mage0) fireball (3.1 cast) **3477**
[15.3] - (mage1) fireball (3.1 cast) 2403
[15.7] - (mage0) (5) ignite tick 2802 ticks remaining 1 time left 2.9s
[17.7] - (mage0) fireball (3.1 cast) **3649**
[17.7] - (mage0) (5) ignite tick 2802 ticks remaining 1 time left 4.0s
[18.4] - (mage1) fireball (3.1 cast) **3606**
[19.7] - (mage0) (5) ignite tick 2802 ticks remaining 1 time left 2.74s
[20.8] - (mage0) fireball (3.1 cast) **3562**
[21.5] - (mage1) fireball (3.1 cast) 2453
[21.7] - (mage0) (5) ignite tick 2802 ticks remaining 1 time left 3.1s
[23.7] - (mage0) (5) ignite tick 2802 ticks remaining 0 time left 1.1s
[23.9] - (mage0) fireball (3.1 cast) 2269
[24.6] - (mage1) fireball (3.1 cast) 2295
[24.8] - (mage0) Ignite dropped
```
or
```
[0] - (lock2) Random initial delay of 1.69 seconds
[0] - (lock1) Random initial delay of 0.5 seconds
[0] - (lock0) Random initial delay of 1.68 seconds
[0.5] - (lock1) Corruption (0.1 cast) (1.5 gcd)
[1.7] - (lock0) Corruption (0.1 cast) (1.5 gcd)
[1.7] - (lock2) Corruption (0.1 cast) (1.5 gcd)
[2.0] - (lock1) Immolate (0.1 cast) (1.5 gcd) RESIST
[3.2] - (lock0) Immolate (0.1 cast) (1.5 gcd) **934**
[3.2] - (lock2) Immolate (0.1 cast) (1.5 gcd) 467
[3.5] - (lock1)  Corruption dot tick 366 ticks remaining 5
[4.7] - (lock0)  Corruption dot tick 366 ticks remaining 5
[4.7] - (lock2)  Corruption dot tick 366 ticks remaining 5
[6.1] - (lock1)  Shadowbolt (2.6 cast) **2712**
[6.1] - (lock1) Immolate (0.1 cast) (1.5 gcd) **934**
[6.2] - (lock0) Immolate dot tick 278 ticks remaining 3
[6.2] - (lock2) Immolate dot tick 278 ticks remaining 3
[6.5] - (lock1) (ISB) Corruption dot tick 439 ticks remaining 4
[7.3] - (lock0)  Shadowbolt (2.6 cast) **2794**
[7.3] - (lock2)  Shadowbolt (2.6 cast) 1362
[7.7] - (lock0) (ISB) Corruption dot tick 439 ticks remaining 4
[7.7] - (lock2) (ISB) Corruption dot tick 439 ticks remaining 4
[9.1] - (lock1) Immolate dot tick 278 ticks remaining 3
[9.2] - (lock0) Immolate dot tick 278 ticks remaining 2
[9.2] - (lock2) Immolate dot tick 278 ticks remaining 2
[9.5] - (lock1) (ISB) Corruption dot tick 439 ticks remaining 3
[9.8] - (lock0) (ISB) Shadowbolt (2.6 cast) 1615
[9.8] - (lock2) (ISB) Shadowbolt (2.6 cast) **3348**
[10.1] - (lock1) (ISB) Shadowbolt (2.6 cast) 1624
```

For multiple iterations:

``` python
from turtlewow_sim.env import Environment
from turtlewow_sim.mage import Mage
from turtlewow_sim.simulation import Simulation
from turtlewow_sim.specs import FireMageTalents

mages = []
num_mages = 5

for i in range(num_mages):
    fm = Mage(name=f'mage{i}', sp=1009, crit=33.17, hit=16, tal=FireMageTalents)
    fm.smart_scorch()
    mages.append(fm)

sim = Simulation(characters=mages)
sim.run(iterations=1000, duration=180)
sim.detailed_report()
```

After the simulation finishes the result will look like this:

```
Total spell dmg                         : 765822
Total dot dmg                           : 275181
Total ignite dmg                        : 275181
Total dmg                               : 275181
Average mage dps                        : 1169
Average >=1 stack ignite uptime         : 90.6%
Average >=3 stack ignite uptime         : 76.1%
Average   5 stack ignite uptime         : 63.1%
Average ignite tick                     : 3437
```
or
```
lock0 average DPS                       : 1018 in 80.0 casts
lock1 average DPS                       : 1016 in 80.0 casts
lock2 average DPS                       : 1016 in 80.0 casts
Total spell dmg                         : 423084
Total dot dmg                           : 125970
Total dmg                               : 549054
Average char dps                        : 1017
Highest single char dps                 : 1173.3
------ ISB ------
ISB uptime                              : 77.2%
Total added dot dmg                     : 10570
Total added spell dmg                   : 43159
```

but you can run with the `detailed_report()` method to get a more detailed output

## Talents and Debuffs

You can customize each character by passing additional arguments. The full constructor looks like this:
```
    class Character:
    def __init__(self,
                 tal: MageTalents,
                 env: Optional[Environment] = None,
                 name: str = '',
                 sp: int = 0,
                 crit: float = 0,
                 hit: float = 0,
                 haste: float = 0,
                 lag: float = 0.1,  # default lag between spells that seems to occur on turtle
                 opts: MageOptions = MageOptions(),
                 ):
```                 

There are premade talent configurations for each spec:
```
FireMageTalents = MageTalents(
    imp_scorch=True,
    fire_power=True,
    critial_mass=False,
    fire_blast_cooldown=8

)

ApFrostMageTalents = MageTalents(
    arcane_instability=True,
    piercing_ice=True
)

WcFrostMageTalents = MageTalents(
    winters_chill=True,
    piercing_ice=True
)
    
SMRuin = WarlockTalents(
    # affliction
    suppression=3,
    improved_corruption=5,
    improved_curse_of_agony=3,
    nightfall=2,
    shadow_mastery=5,

    # destruction
    improved_shadow_bolt=5,
    bane=5,
    devastation=5,
    ruin=1,
)

DSRuin = WarlockTalents(
    # affliction
    suppression=2,
    improved_corruption=5,

    # demonology
    demonic_sacrifice=1,

    # destruction
    improved_shadow_bolt=5,
    bane=5,
    devastation=5,
    ruin=1,
)
```

Simulation defaults assume Curse of Elements and Shadow are permanently on, you can turn it off by passing the appropriate argument to the constructor
```
class Simulation:
    def __init__(self,
                 characters: List[Character] = None,
                 permanent_coe: bool = True,
                 permanent_cos: bool = True,
                 permanent_nightfall: bool = False):
```
no consumables are assumed otherwise, you need to factor those in your total sp/crit

You can also enable permanent nightfall proc using 
```
sim = Simulation(permanent_nightfall=True)
```

## Rotations
All rotations include a random initial delay of 0-2 seconds. You can disable this by passing the delay=0 parameter

Some currently supported rotations are:


* spam_scorch()

* spam_fireballs()

* spam_frostbolts()

1 scorch + 9 fireballs (repeated)
* one_scorch_then_fireballs()  

 1 scorch + 1 pyro + 6 fireballs (repeated)
* one_scorch_one_pyro_then_fb() 

1 scorch + 1 frostbolt + 8 fireballs (repeated)
* one_scorch_one_frostbolt_then_fb()  

 cast scorch if less than 5 imp.scorch stacks 
 else cast fireball
* smart_scorch()  

* spam_shadowbolt()

* agony_corruption_immolate_shadowbolt()

* cos_corruption_immolate_shadowbolt()
     

You can pass as arguments to each rotation when you want each mage to attempt
to activate their cooldowns. For example `mage1.one_scorch_one_pyro_then_fb(cds=CooldownUsages(arcane_power=5, power_infusion=6, mqg=7))
` will tell the first mage to attempt to activate arcane_power at 5 seconds, power_infusion at 6 seconds and mqg at 7 seconds.

Available cooldowns are:
```
class CooldownUsages:
    combustion: Optional[float] = None
    arcane_power: Optional[float] = None
    power_infusion: Optional[float] = None
    presence_of_mind: Optional[float] = None
    toep: Optional[float] = None
    mqg: Optional[float] = None
    berserking30: Optional[float] = None
    berserking20: Optional[float] = None
    berserking10: Optional[float] = None
```
