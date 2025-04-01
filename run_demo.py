from synpyosys import bindings, api, llm
import os

def main():
    print("\n=== SynPYosys Test Demo ===\n")

    # Simulate C-to-Python binding
    bindings.yosys_c_call("abc -fast")

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Run Yosys + ABC flow
    success = api.run_yosys_flow("flows/example_flow.ys")

    # Simulate LLM integration
    if success:
        llm.query_llm("Was this circuit optimized for area or delay?")
    else:
        print("[ERROR] Synthesis failed. LLM not called.")

    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
