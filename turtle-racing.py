import turtle
import time
import random
COLORS = ['red','blue','green','yellow','pink']
WIDTH, HEIGHT = 500, 500
def get_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric. Try Again.")   
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Numebr is not in given range(2-10).")

def init_turtle():   
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing.")
    

racers_count = get_racers() 
init_turtle()
racer = turtle.Turtle()

turtle.done()