"""Fidelity level definitions and ordering."""
from apollosim.adapters.base import FidelityLevel

FIDELITY_ORDER = [FidelityLevel.ANALYTICAL, FidelityLevel.SURROGATE, FidelityLevel.PHYSICS]

def fidelity_rank(level: FidelityLevel) -> int:
    return FIDELITY_ORDER.index(level)
