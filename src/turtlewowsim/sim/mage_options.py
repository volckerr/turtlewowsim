from dataclasses import dataclass

@dataclass(kw_only=True)
class MageOptions:
    fullt2: bool = False

    drop_suboptimal_ignites: bool = False  # cast pyroblast if scorch/fireblast in ignite to drop ignite
    remaining_ticks_for_ignite_extend: int = 1  # min remaining ticks to extend ignite
    extend_ignite_with_fire_blast: bool = False  # extend ignite with fire blast (prio over scorch)
    extend_ignite_with_scorch: bool = False  # extend ignite with scorch
    pyro_on_t2_proc: bool = True
