from classes.Vector import Vector

class Body:
    
    def __init__(self, x, y, mass, radius, color, velocity) -> None:
        
        # mass must be in kilograms
        # radius must be in meters
        
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.velocity = velocity
        
        
    def apply_force(self, force: Vector, coeff: float = 1.0) -> None:
        self.x += force.x / self.mass * coeff
        self.y += force.y / self.mass * coeff
        
        
        
        
