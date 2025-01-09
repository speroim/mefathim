import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




def show_walk(step_map):
    if dimensions == 1:
        for people in step_map:
            plt.plot(people)
        
        print(people)      
        plt.show()
    if dimensions == 2:
        pass
    elif dimensions == 3:
        pass
    else:
        #panda
        pass
    



def take_step(step_map):
    dims = len(step_map)
    steps = len(step_map[0])
    
    for step in range(1, steps):
        chosen_dim = random.randint(0, dims - 1) 
        step_direction = random.choice([1, -1])  
        step_map[chosen_dim][step] = step_map[chosen_dim][step - 1] + step_direction

    show_walk(step_map)

def random_step(peoples, dimensions, steps):
    directions = [[[0] * (steps+1) for _ in range(dimensions)] for _ in range(peoples)] 
    
    for step_map in (directions):
        take_step(step_map)

try:
    peoples = int(input("numbers of peoples:"))
    assert peoples > 0
    dimensions = int(input("numbers of dimensions:"))
    assert dimensions > 0
    steps = int(input("numbers of steps:"))
    assert steps > 0
except AssertionError:
    print("only positive number")


random_step(peoples, dimensions, steps)