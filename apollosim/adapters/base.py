"""
apollosim/adapters/base.py
Abstract base class for all external tool adapters.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any


class FidelityLevel(Enum):
    ANALYTICAL = "ANALYTICAL"
    SURROGATE  = "SURROGATE"
    PHYSICS    = "PHYSICS"


@dataclass
class LayerOutput:
    """Canonical inter-layer output. Must be validated against the layer JSON schema."""
    schema_version: str
    layer: str
    tool: str
    fidelity_level: FidelityLevel
    session_id: str
    metrics: dict[str, Any]
    uncertainties: dict[str, Any]
    provenance: dict[str, Any]
    raw: dict[str, Any] | None = None


class AdapterBase(ABC):
    """Abstract base for all APOLLOSim tool adapters."""

    LAYER: str = ""
    TOOL_NAME: str = ""
    FIDELITY: FidelityLevel = FidelityLevel.PHYSICS

    @abstractmethod
    def run(self, config: dict, input_data: LayerOutput | None) -> LayerOutput: ...

    @abstractmethod
    def validate_input(self, input_data: LayerOutput | None) -> bool: ...

    @abstractmethod
    def estimate_cost(self, config: dict) -> float: ...

    def get_fidelity_level(self) -> FidelityLevel:
        return self.FIDELITY

    def get_layer(self) -> str:
        return self.LAYER

    def get_tool_name(self) -> str:
        return self.TOOL_NAME
