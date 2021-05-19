from classes.Body import Body
from random import randint 

def get_random_color() -> tuple:
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def get_random_body() -> Body:
    return Body(randint(0, 650), randint(0, 650), randint(1, 100), randint(1, 100), get_random_color(), 0)