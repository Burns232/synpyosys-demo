import subprocess

def run_yosys_flow(script_path):
    try:
        print("[API] Launching Yosys synthesis flow...")
        result = subprocess.run(["yosys", "-s", script_path], capture_output=True, text=True)
        print(result.stdout)
        return True
    except Exception as e:
        print(f"[API ERROR] {e}")
        return False
