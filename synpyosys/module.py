class Module:
    def __init__(self, name):
        self.name = name
        self.muxes = []

    def addMux(self, name, select, inputs, outputs, **kwargs):
        self.muxes.append({
            "name": name,
            "select": select,
            "inputs": inputs,
            "outputs": outputs,
            "extra": kwargs
        })

    def describe(self):
        print(f"Module: {self.name}")
        for mux in self.muxes:
            print(f"  Mux: {mux['name']} — sel: {mux['select']}, in: {mux['inputs']}, out: {mux['outputs']}")
