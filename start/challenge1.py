# import random
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# steps = int(input("how many steps? "))
# Dimensions = int(input("how many dimensions? "))

# Dimensions_value=[0] * Dimensions
# Direction = [0] * 3

# x_value = [0]
# y_value = [0]
# z_value = [0]

# for _ in range(steps):
#     random_dimension = random.randrange(Dimensions)
#     random_step = random.randrange(-1,2)
#     Dimensions_value[random_dimension] += random_step 
#     print(f"dimension: {random_dimension}, step: {random_step}, D_value: {Dimensions_value}")

#     if Dimensions == 2:
#         x_value.append(Dimensions_value[0])
#         y_value.append(Dimensions_value[1])
#     elif Dimensions ==3:
#         x_value.append(Dimensions_value[0])
#         y_value.append(Dimensions_value[1])
#         z_value.append(Dimensions_value[2])



# print(Dimensions_value)

# if Dimensions == 1:
#     y = [Dimensions_value[0]] * steps
#     plt.plot(y, c="b")
#     plt.xlabel('steps')
#     plt.ylabel('progres')
#     plt.title('1D graph')
#     plt.show()   
#  

# elif Dimensions == 2:
#     plt.scatter(x_value, y_value, c='red', alpha= 0.1)
#     plt.plot(x_value, y_value, marker='o', c='b')
#     plt.xlabel('X (Dimension 1)')
#     plt.ylabel('Y (Dimension 2)')
#     plt.title('2D graph')
#     plt.grid(True)
#     plt.show()
    

# elif Dimensions == 3:
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
    
#     ax.plot(x_value, y_value, z_value, c='r', marker = "o", alpha = 0.3)
#     ax.set_xlabel('Dimension 1')
#     ax.set_ylabel('Dimension 2')
#     ax.set_zlabel('Dimension 3')
#     plt.title('3D Line Plot')
#     plt.grid(True)
#     plt.show()

# else:
#     print("no graph for more then 3 dimension")







import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def random_walk(steps, dimensions):
    walk = np.zeros((steps + 1, dimensions))
    for i in range(1, steps + 1):
        dimension = random.randrange(dimensions)
        step = random.randrange(-1, 2)
        walk[i] = walk[i-1]
        walk[i, dimension] += step
        print(f"צעד {i}: ממד {dimension}, גודל צעד {step}, מיקום: {walk[i]}")
    return walk

def plot_walk(walk):
    dimensions = walk.shape[1]
    
    if dimensions == 1:
        plt.plot(walk[:, 0], range(len(walk)), c="b")
        plt.xlabel('התקדמות')
        plt.ylabel('צעדים')
        plt.title('גרף חד-ממדי')
    
    elif dimensions == 2:
        plt.scatter(walk[:, 0], walk[:, 1], c='red', alpha=0.1)
        plt.plot(walk[:, 0], walk[:, 1], marker='o', c='b')
        plt.xlabel('ממד 1')
        plt.ylabel('ממד 2')
        plt.title('גרף דו-ממדי')
    
    elif dimensions == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(walk[:, 0], walk[:, 1], walk[:, 2], c='r', marker="o", alpha=0.3)
        ax.set_xlabel('ממד 1')
        ax.set_ylabel('ממד 2')
        ax.set_zlabel('ממד 3')
        plt.title('גרף תלת-ממדי')
    
    else:
        print("אין אפשרות להציג גרף עבור יותר מ-3 ממדים")
        return
    
    plt.grid(True)
    plt.show()

def main():
    steps = int(input("כמה צעדים? "))
    dimensions = int(input("כמה ממדים? "))
    
    walk = random_walk(steps, dimensions)
    plot_walk(walk)


main()















# elif Dimensions == 3:
#     # גרף תלת-ממדי
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
    
#     x = np.arange(steps)
#     y = [Dimensions_value[0] for _ in range(steps)]
#     z = [Dimensions_value[1] for _ in range(steps)]
#     w = [Dimensions_value[2] for _ in range(steps)]
    
#     ax.scatter(y, z, w, c='r', marker='o')
#     ax.set_xlabel('Dimension 1')
#     ax.set_ylabel('Dimension 2')
#     ax.set_zlabel('Dimension 3')
#     plt.title('3D Plot')
#     plt.show()

# else:
#     # אם יש יותר מ-3 ממדים, לא נציג גרף
#     print("No plot for more than 3 dimensions.")


# import matplotlib.pyplot as plt
# import numpy as np

# def plot_contour(Dimensions_value, steps):
#     x = np.linspace(0, Dimensions_value[0], steps)
#     y = np.linspace(0, Dimensions_value[1], steps)
#     X, Y = np.meshgrid(x, y)
#     Z = X * np.exp(-X**2 - Y**2)  # Example function
    
#     plt.figure()
#     contour = plt.contourf(X, Y, Z, cmap='viridis')
#     plt.colorbar(contour)
    
#     plt.xlabel('Dimension 1')
#     plt.ylabel('Dimension 2')
#     plt.title('Contour Plot')
#     plt.show()




# import random
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# from collections import Counter
# from matplotlib.animation import FuncAnimation

# steps = int(input("כמה צעדים? "))
# Dimensions = 3  # קבענו ל-3 ממדים

# Dimensions_value = [0] * Dimensions
# x_value = [0]
# y_value = [0]
# z_value = [0]

# for _ in range(steps):
#     random_dimension = random.randrange(Dimensions)
#     random_step = random.randrange(-1, 2)
#     Dimensions_value[random_dimension] += random_step
#     x_value.append(Dimensions_value[0])
#     y_value.append(Dimensions_value[1])
#     z_value.append(Dimensions_value[2])

# # ספירת מספר הביקורים בכל נקודה
# visit_count = Counter(zip(x_value, y_value, z_value))

# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')

# scatter = ax.scatter([], [], [], c=[], s=[], cmap='viridis', alpha=0.6)
# line, = ax.plot([], [], [], c='gray', alpha=0.3)
# double_visit_line, = ax.plot([], [], [], c='red', alpha=0.5, linewidth=2)

# ax.set_xlim(min(x_value), max(x_value))
# ax.set_ylim(min(y_value), max(y_value))
# ax.set_zlim(min(z_value), max(z_value))

# ax.set_xlabel('X (Dimension 1)')
# ax.set_ylabel('Y (Dimension 2)')
# ax.set_zlabel('Z (Dimension 3)')
# ax.set_title('הליכה אקראית תלת-ממדית')

# def update(frame):
#     current_x = x_value[:frame+1]
#     current_y = y_value[:frame+1]
#     current_z = z_value[:frame+1]
    
#     current_count = Counter(zip(current_x, current_y, current_z))
    
#     colors = [current_count[(x, y, z)] for x, y, z in zip(current_x, current_y, current_z)]
#     sizes = [20 + 30 * (current_count[(x, y, z)] - 1) for x, y, z in zip(current_x, current_y, current_z)]
    
#     scatter._offsets3d = (current_x, current_y, current_z)
#     scatter.set_array(np.array(colors))
#     scatter.set_sizes(sizes)
    
#     line.set_data(current_x, current_y)
#     line.set_3d_properties(current_z)
    
#     # מציאת קטעים עם ביקורים כפולים
#     double_visit_x = []
#     double_visit_y = []
#     double_visit_z = []
#     for i in range(len(current_x) - 1):
#         if current_count[(current_x[i], current_y[i], current_z[i])] > 1 and \
#            current_count[(current_x[i+1], current_y[i+1], current_z[i+1])] > 1:
#             double_visit_x.extend([current_x[i], current_x[i+1], None])
#             double_visit_y.extend([current_y[i], current_y[i+1], None])
#             double_visit_z.extend([current_z[i], current_z[i+1], None])
    
#     double_visit_line.set_data(double_visit_x, double_visit_y)
#     double_visit_line.set_3d_properties(double_visit_z)
    
#     return scatter, line, double_visit_line

# anim = FuncAnimation(fig, update, frames=steps+1, interval=50, blit=False, repeat=False)

# cbar = plt.colorbar(scatter, label='מספר ביקורים')
# cbar.set_ticks(range(1, max(visit_count.values()) + 1))

# plt.grid(True)
# plt.show()

# # אם תרצה לשמור את האנימציה כקובץ:
# # anim.save('random_walk_3d_visits.gif', writer='pillow', fps=30)

# # אם תרצה לשמור את האנימציה כקובץ:
# # anim.save('random_walk_3d_visits.gif', writer='pillow', fps=30)