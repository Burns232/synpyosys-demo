# SynPYosys Capstone Demo

This demo illustrates a simplified logic synthesis flow using Yosys and ABC, wrapped in a Python-based modular architecture called **SynPYosys**. While actual `pyosys` bindings and gate-level visualization are replaced with placeholders, this project simulates the structure, control, and extension points that a full SynPYosys system would support.

---

## Project Overview

This project demonstrates:
- Synthesis and optimization flow using **Yosys**
- Technology mapping with **ABC**
- A Python abstraction architecture mimicking **SynPYosys**
- Placeholder support for **LLM integration** and **graphical output**

---

## 🧱 Project Structure

```bash
CapstoneDemo/
├── run_demo.py                # Main entry point for the demo
├── synpyosys/                 # Python abstraction layer (mock version)
│   ├── __init__.py
│   ├── api.py                 # High-level orchestration API
│   ├── bindings.py            # Calls Yosys/ABC via subprocess
│   ├── llm.py                 # Placeholder for AI chatbot
│   ├── design.py              # Placeholder Design class
│   └── module.py              # Placeholder for Verilog module logic
├── flows/
│   └── example_flow.ys        # Yosys synthesis script
├── test_circuits/
│   └── example.v              # Verilog circuit used in the demo
└── output/                    # Final synthesized output goes here
```

---

## Flow Summary

When you run:
```bash
python3 run_demo.py
```
You’ll see a full logic synthesis pipeline printed to the terminal. The process includes:

### Step 1: Verilog Parsing
- Yosys reads `test_circuits/example.v`
- Converts Verilog to AST, then to RTLIL IR
- Module: `example`

### Step 2: Hierarchy Resolution
- Handles module linking and top-level identification

### Step 3: Process Conversion (`PROC` passes)
- Converts `always` blocks to logic structures
- Creates multiplexers, flip-flops, and logic gates

### Step 4: Optimization Passes (`OPT`)
- Constant folding
- Removal of unused wires/cells
- DFF and mux optimizations

### Step 5: FSM Extraction
- Detects and optimizes finite state machines (FSMs)

### Step 6: ABC Technology Mapping
- Converts RTL logic to mapped gates (mocked here)
- In the demo, ABC finds nothing to map due to circuit simplicity

### Step 7: Verilog Backend
- Outputs final synthesized Verilog to `output/`

### Step 8: LLM Mock Response
- Demonstrates placeholder chatbot output:
  ```
  [LLM MOCK] Prompt: 'Was this circuit optimized for area or delay?' 
  Response: [This is a placeholder response]
  ```

---

## SynPYosys Architecture Explained

This demo skips real C++ bindings, but mimics the actual **SynPYosys** design showing how each module from abc and yosys is run in SynPYosys:

### 1. `bindings.py`
> Simulates a wrapper around Yosys/ABC command-line tools.
- Runs `.ys` scripts using `subprocess`
- Would be replaced with real `pyosys` calls in full version

### 2. `api.py`
> Python API to run and orchestrate synthesis flows.
- Combines design loading, synthesis, and mock chatbot response

### 3. `llm.py`
> Placeholder for LLM/chatbot support
- In the full version, this would use PyTorch or OpenAI APIs

### 4. `design.py` & `module.py`
> Internal representations of hardware modules
- Currently mocked with print statements
- `show()` displays structure textually (e.g. muxes and ports)

---

## 🔍 Sample Output Snippet

```text
-- Executing script file `flows/example_flow.ys' --
...
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Don't call ABC as there is nothing to map.
...
[LLM MOCK] Prompt: 'Was this circuit optimized for area or delay?'
Response: [This is a placeholder response]
=== Demo Complete ===
```

---

## What's Missing (but planned in full SynPYosys)
- **Real C++/Python bindings** using `pyosys`
- **Gate-level visualization** (SynPYosys does this, so once implemented this will be solved.)
- **Automatic RTL generation** from user requirements

---
