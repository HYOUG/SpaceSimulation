from classes.Body import Body
from classes.Vector import Vector
from math import sqrt


G = 0.00000000006674

def get_distance(body_a: Body, body_b: Body):
    return sqrt((body_b.x - body_a.x)**2 + (body_b.y - body_a.y)**2)

def get_vector(body_a: Body, body_b: Body):
    return Vector(body_b.x - body_a.x, body_b.y - body_a.y)

def get_gvector(body_a: Body, body_b: Body):
    vector_ab = get_vector(body_a, body_b)
    return vector_ab.multiply(-G * ((body_a.mass * body_b.mass) / get_distance(body_a, body_b)))
            

