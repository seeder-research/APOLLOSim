# APOLLOSim

**A cross-layer co-design and simulation framework for AI/ML accelerators leveraging photonic interconnects and emerging memory-centric computing.**

APOLLOSim orchestrates external simulation tools across all abstraction layers — from device physics to workload execution — under a unified schema, multi-fidelity DSE engine, and bidirectional feedback controller.

## Framework Layers

| Layer | Scope | External Tools |
|---|---|---|
| Device / Material | Physics, compact models, RRAM/FeFET, photonic devices | Sentaurus, Silvaco ATLAS, QuantumATK, DEVSIM |
| Circuit | Analog/mixed-signal, memory array, photonic circuit | ngspice, Xyce, Spectre, HSPICE |
| Microarchitecture | CIM arrays, systolic, photonic NoC, memory hierarchy | gem5, Timeloop, CACTI, McPAT |
| System Architecture | SoC integration, chiplet, interconnect | gem5-Aladdin, STONNE, Accel-Sim |
| Workload Execution | DNN/ML workload mapping, dataflow | Custom mappers, ONNX front-end |
| Forward Prediction | Perf/power/area/bandwidth estimates | Analytical + surrogate models |
| Backward Feedback | Constraint propagation, automated optimization | Bayesian opt, RL, gradient-free |

## Multi-Physics Domains

- **Electrical**: drift-diffusion, SPICE-level circuit simulation
- **Optical/Photonic**: FDTD, eigenmode, interconnect S-parameters
- **RRAM / Ferroelectric**: resistive switching, polarization dynamics

## Design-Space Exploration

Multi-fidelity strategy: the DSE engine selects simulation fidelity (analytical → surrogate → full physics) per query, per layer, based on accuracy requirements and compute budget.

## Directory Structure

See [`docs/specs/directory_structure.md`](docs/specs/directory_structure.md).

## Status

🚧 Pre-alpha — specification and scaffold phase.
