# APOLLOSim Inter-Layer Interoperability Contract
Version: 0.1.0-draft

## Schema Boundary Map
```
[Device/Material]  --device.schema.json-->  [Circuit]
[Circuit]          --circuit.schema.json--> [Uarch]
[Photonic Device]  --photonic.schema.json-> [Photonic Circuit] --> [Uarch]
[RRAM/FeFET]       --memory.schema.json-->  [Circuit] + [Uarch]
[Uarch]            --uarch.schema.json-->   [System]
[System]           --system.schema.json-->  [Workload]
[Workload]         --workload.schema.json-> [Analysis]
```

## Common Envelope (all schemas inherit)
```json
{
  "apollosim_schema_version": "0.1.0",
  "layer": "<layer_name>",
  "tool": "<adapter_name>",
  "fidelity_level": "ANALYTICAL|SURROGATE|PHYSICS",
  "session_id": "<uuid>",
  "timestamp_utc": "<ISO8601>",
  "parameter_snapshot": {},
  "metrics": {},
  "uncertainties": {},
  "provenance": {"input_ids":[], "tool_version":"", "config_hash":""}
}
```

## Key Metric Fields (v0.1)

### device.schema.json
vth (V), ss (mV/dec), ioff (A/um), ion (A/um), cgg (F/um),
thermal_resistance (K/W), variability: {sigma_vth, sigma_ioff}

### memory.schema.json
lrs (Ω), hrs (Ω), set_voltage (V), reset_voltage (V),
retention_time (s), endurance_cycles, conductance_levels[],
cycle_to_cycle_variability (Ω), device_to_device_variability (Ω),
fefet_remnant_polarization Pr (µC/cm²)

### photonic.schema.json
insertion_loss (dB), extinction_ratio (dB), bandwidth_3db (GHz),
s_parameters (complex, freq-indexed), neff, group_index,
half_wave_voltage Vpi (V), responsivity (A/W)

### circuit.schema.json
propagation_delay (ps), power_dynamic (mW), power_static (µW),
snr (dB), bandwidth (GHz), area (µm²), noise_figure (dB)

### uarch.schema.json
throughput (TOPS), energy_per_op (fJ/op), area (mm²),
memory_bandwidth (GB/s), latency (ns), utilization (fraction)

### system.schema.json
system_throughput (TOPS), system_power (W), system_area (mm²),
memory_capacity (GB), interconnect_bandwidth (TB/s), thermal_design_power (W)

### workload.schema.json
model_name, operator_graph (ONNX JSON), total_ops (GOps),
total_memory_accesses (GB), arithmetic_intensity (ops/byte),
execution_time (ms), energy (mJ)

## Feedback Envelope
```json
{
  "feedback_type": "CONSTRAINT|PARAMETER_UPDATE",
  "source_layer": "", "target_layer": "",
  "violated_metric": "", "required_value": null,
  "implied_constraint": {
    "parameter": "", "direction": "TIGHTEN|RELAX",
    "suggested_range": [null, null]
  },
  "payload": {}
}
```
