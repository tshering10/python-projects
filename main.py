import turtle
import random
import time

def get_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric. Try Again.")   
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in the given range (2-10).")

def init_turtle():
    WIDTH, HEIGHT = 500, 500
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def create_racers(num_racers):
    racers = []
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "grey"]
    
    for i in range(num_racers):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colors[i])  # Assign a color to each racer
        racer.penup()
        racer.goto(-230, 150 - i * 30) # Position each racer vertically
        racer.pendown()
        racers.append(racer)
    
    return racers

def race(racers):
    finish_line = 200
    winner = None
    
    while winner is None:
        for racer in racers:
            racer.forward(random.randint(1, 10))  # Move each racer a random distance
            
            # Check if any racer has crossed the finish line
            if racer.xcor() >= finish_line:
                winner = racer
                break
                
    return winner

def main():
    racers_count = get_racers()
    init_turtle()
    racers = create_racers(racers_count)
    winner = race(racers)
    
    print(f"The winner is the {winner.color()[0]} turtle!")
    time.sleep(2)  # Pause for a moment before closing

if __name__ == "__main__":
    main()
