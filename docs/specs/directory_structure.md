# APOLLOSim Directory Structure Specification
Version: 0.1.0-draft

## Design Principles
1. Tool-agnostic core: apollosim/core and apollosim/schema have zero simulator dependency
2. Adapter isolation: each tool lives in its own subpackage
3. Schema-first interoperability: all inter-layer data validated against JSON Schema
4. DSE and feedback are first-class framework components
5. Config-driven: all invocations driven by YAML in configs/

## Adapter Base Contract
Each adapter implements AdapterBase (apollosim/adapters/base.py):
- run(config, input_data) -> LayerOutput
- validate_input(input_data) -> bool
- estimate_cost(config) -> float
- get_fidelity_level() -> FidelityLevel

## Multi-fidelity Selection Criteria
- accuracy_tolerance: per-metric user spec (e.g. ±5% power)
- compute_budget: wall-clock or CPU-hour cap
- surrogate_confidence: GP uncertainty or NN ensemble variance
- exploration_phase: PHYSICS required at final validation

## Feedback Modes
MANUAL | AUTOMATED | CONSTRAINT — selectable per layer-pair per run
