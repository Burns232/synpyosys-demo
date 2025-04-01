# SynPYosys Core Modules

This folder contains the core Python API abstraction for interacting with Yosys.

### Files
- `Design.py`: Represents an entire Verilog design. Responsible for loading, managing, and visualizing modules.
- `Module.py`: Represents individual modules and their logic. Used for component-level access or injection.
- `api.py`: High-level interface to coordinate flows, input files, and output results.
- `bindings.py`: Handles low-level interaction with Yosys CLI (acts as a placeholder for PyBind11 bindings).
- `llm.py`: Placeholder for the AI assistant module (currently mocked).
