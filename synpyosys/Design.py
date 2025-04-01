from synpyosys.module import Module

class Design:
    def __init__(self):
        self.modules = []

    def read_verilog(self, filepath):
        print(f"[READ MOCK] Reading Verilog from: {filepath}")
        mod = Module(name="top")
        self.modules.append(mod)

    def top_module(self):
        return self.modules[0]

    def show(self):
        print("[SHOW MOCK] No graphical output. Printing module structure:")
        for mod in self.modules:
            mod.describe()
