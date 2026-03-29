# APOLLOSim Framework Specification
Version: 0.1.0-draft | Status: Under review

## 1. Objectives
APOLLOSim is a cross-layer co-design orchestration framework. It invokes external simulation
tools via standardized adapters, enforces a canonical inter-layer data schema, manages
multi-fidelity simulation, and closes the design loop via backward feedback.

## 2. Layer Stack
```
Workload Execution
System Architecture
Microarchitecture
Circuit
Device / Material
     ↑ Backward Feedback   ↓ Forward Data
```
Multi-physics domains: Electrical | Optical/Photonic | RRAM/FeFET | Thermal

## 3. Interoperability
- All inter-layer data: JSON validated against apollosim/schema/*.schema.json
- Schema versioning: semver; adapters declare compatible versions
- Units: SI base units at schema boundaries

## 4. Multi-fidelity
| Level | Description | Typical latency |
|---|---|---|
| ANALYTICAL | Closed-form / LUT | < 1 ms |
| SURROGATE | ML model | < 100 ms |
| PHYSICS | Full external tool | seconds–hours |

Selection based on: accuracy_tolerance, compute_budget, surrogate_confidence, exploration_phase.

## 5. DSE Strategies (pluggable)
- BayesianStrategy (BoTorch/Ax)
- GradientFreeStrategy (CMA-ES, Nelder-Mead)
- RLStrategy (policy-gradient / model-based)
- GridStrategy (baseline)

## 6. Feedback Modes
| Mode | Trigger | Action |
|---|---|---|
| MANUAL | User request | Report; human adjusts |
| AUTOMATED | Metric violation | Optimizer updates params |
| CONSTRAINT | Metric violation | Push constraint to upstream layer |

## 7. Multi-physics Coupling
- Electrical–Thermal: self-heating in RRAM and photonic modulators
- Electrical–Optical: electro-optic modulator, photodetector boundaries
- Electrical–RRAM/FeFET: conductance state, variability, retention distributions

## 8. Open Questions (v0.2)
- [ ] HDF5 vs Arrow/Parquet for session store
- [ ] Distributed execution (local / HPC / cloud)
- [ ] Tight vs loose coupling for co-simulation
- [ ] Photonic-electronic netlist standard
- [ ] FeFET compact model standard (MFIS / IMEC / custom Verilog-A)
