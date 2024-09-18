class Outer:
    def __init__(self) -> None:
        self.inner_demo = self.Inner().demo()
    
    class Inner:
        def __init__(self) -> None:
            pass

        def demo(self):
            return "Message recieved"

    
o1 = Outer()
print(o1.inner_demo)