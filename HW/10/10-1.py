class Indenter:
    def __init__(self):
        self.indent = -1
    
    def print(self, text):
        print(self.indent*"    " + text)
        
    def __enter__(self):
        self.indent += 1
        return self
    
    def __exit__(self, *args, **kwargs):
        self.indent -= 1


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the Code…")
        indent.print("Hey You!")
    indent.print("Torvalds")