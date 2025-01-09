import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


while True:
    try:
        steps = int(input("how many steps? "))
        Dimensions = int(input("how many dimensions? "))
        break
    except ValueError:
        print("ValueError, right only a full number")


Dimensions_value=[0] * Dimensions
Direction = [0] * 3

x_value = [0]
y_value = [0]
z_value = [0]

for _ in range(steps):
    random_dimension = random.randrange(Dimensions)
    random_step = random.randrange(-1,2)
    Dimensions_value[random_dimension] += random_step 
    print(f"dimension: {random_dimension}, step: {random_step}, D_value: {Dimensions_value}")

    if Dimensions == 2:
        x_value.append(Dimensions_value[0])
        y_value.append(Dimensions_value[1])
    elif Dimensions ==3:
        x_value.append(Dimensions_value[0])
        y_value.append(Dimensions_value[1])
        z_value.append(Dimensions_value[2])



print(Dimensions_value)


if Dimensions == 1:
    y = [Dimensions_value[0]] * steps
    plt.plot(y, c="b")
    plt.xlabel('steps')
    plt.ylabel('progres')
    plt.title('1D graph')
    plt.show()   
 

elif Dimensions == 2:
    plt.scatter(x_value, y_value, c='red', alpha= 0.1)
    plt.plot(x_value, y_value, marker='o', c='b')
    plt.xlabel('X (Dimension 1)')
    plt.ylabel('Y (Dimension 2)')
    plt.title('2D graph')
    plt.grid(True)
    plt.show()
    

elif Dimensions == 3:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot(x_value, y_value, z_value, c='r', marker = "o", alpha = 0.3)
    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')
    ax.set_zlabel('Dimension 3')
    plt.title('3D Line Plot')
    plt.grid(True)
    plt.show()

else:
    print("no graph for more then 3 dimension")