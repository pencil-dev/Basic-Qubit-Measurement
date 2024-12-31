# Simple Qubit Measurement

A minimal quantum circuit implementation that creates and measures a single qubit in the computational basis.

## Requirements
```
pennylane>=0.19.0
```

## Description
This program:
- Initializes a single qubit quantum device
- Creates a quantum circuit
- Measures the qubit in computational basis (|0⟩,|1⟩)
- Returns measurement probabilities

## Expected Output
- |0⟩: 1.0 (100% probability)
- |1⟩: 0.0 (0% probability)

## Usage
```python
python simple_qubit.py
```

## Quantum Circuit Details
- Initial state: |0⟩
- No gates applied
- Measurement: Computational basis