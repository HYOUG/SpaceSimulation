class Vector:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def multiply(self, value) -> None:
        self.x *= value
        self.y *= value
        return self