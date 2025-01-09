from PIL import Image
import numpy as np




"""
Assignment: Solve a Maze using Dijkstra's Algorithm

Objective:
In this assignment, you will implement Dijkstra's algorithm to find the shortest path in a maze represented as an RGB image. You will write custom data structures, including a PixelNode class and a priority queue, while ensuring efficient pathfinding.

Problem Description:
You are given an RGB image of a maze where:
- White pixels (all channels ≈ 255) represent valid paths.
- Non-white pixels (one or more channels < 255) represent obstacles.

Your goal is to find the shortest path between a start pixel and an end pixel, given their coordinates, by:
1. Converting the RGB maze image to a grayscale representation for simplicity.
2. Implementing a custom PixelNode class for maze pixels.
3. Building and utilizing a priority queue with a decrease_key operation for efficient pathfinding.
4. Using Dijkstra's algorithm to traverse the maze and determine the shortest path.

---

Tasks:

1. Grayscale Conversion
Write a function to convert the RGB maze image into grayscale using the formula:
  Gray = 0.2989 * R + 0.5870 * G + 0.1140 * B

Task:
Implement a function `convert_to_grayscale(image)` that:
- Takes the RGB image as input.
- Converts it to grayscale using the formula.
- Returns the grayscale image as a 2D array.

"""


def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    rgb_array = np.array(image)
    print(rgb_array)
    pixel = rgb_array[0, 0]
    print(f"RGB values of top-left pixel: {pixel}")
convert_to_grayscale("./mazes/maze1.jpg")


"""
    Convert an RGB image to grayscale.

    :param image: Input RGB image as a 3D NumPy array
    :return: Grayscale image as a 2D NumPy array
    """
    


"""
2. Pixel Representation
Create a class `PixelNode` to represent each pixel in the maze. It should include:
- x and y: Coordinates of the pixel.
- distance: Shortest known distance from the start pixel (initialize to infinity).
- visited: Boolean indicating whether the pixel has been processed.
- color: Optional attribute for the grayscale intensity value.
- heap_index: The index of the PixelNode in the priority queue. This is essential for efficient decrease_key operations.

Additionally:
- Implement comparison operators (e.g., __lt__) to make PixelNode objects compatible with a min-heap.

"""





class PixelNode:
    def __init__(self, x, y, color=None):
        """
        Initialize a PixelNode object.

        :param x: X-coordinate of the pixel
        :param y: Y-coordinate of the pixel
        :param color: Grayscale intensity of the pixel
        """
        pass

    def __lt__(self, other):
        """
        Comparison operator for PixelNode based on distance.
        """
        pass


"""
3. Priority Queue
Write a class `PriorityQueue` for managing PixelNode objects. Use a min-heap for efficient operations. Include the following methods:
- insert(node): Add a new PixelNode to the queue and update its heap_index.
- extract_min(): Remove and return the PixelNode with the smallest distance while maintaining the heap property.
- decrease_key(node, new_distance): Update the distance of an existing node and adjust its position in the heap. Update its heap_index.

Hint:
Use the heap_index attribute of PixelNode objects to keep track of their position in the heap. This allows decrease_key to access nodes efficiently.
"""


class PriorityQueue:
    def __init__(self):

        """
        Initialize an empty priority queue.
        """
        pass

    def insert(self, node):
        """
        Insert a PixelNode into the priority queue.

        :param node: The PixelNode to be inserted
        """
        pass

    def extract_min(self):
        """
        Extract and return the PixelNode with the smallest distance.

        :return: The PixelNode with the smallest distance
        """
        pass

    def decrease_key(self, node, new_distance):
        """
        Update the distance of a node and reheapify.

        :param node: The PixelNode whose distance is to be updated
        :param new_distance: The new distance value
        """
        pass


"""
4. Dijkstra's Algorithm
Implement Dijkstra's algorithm to find the shortest path from the start pixel to the end pixel.
"""


def dijkstra(image, start, end):
    """
    Perform Dijkstra's algorithm to find the shortest path in a maze.

    :param image: 2D NumPy array representing the grayscale maze
    :param start: Tuple (x, y) of the start pixel's coordinates
    :param end: Tuple (x, y) of the end pixel's coordinates
    :return: List of (x, y) tuples representing the shortest path
    """
    pass

# Notes:
# - Ensure all data structures are used efficiently to minimize runtime.
# - Use helper functions where necessary to keep the code modular.
# - Test your implementation with various mazes and start/end points to ensure correctness.
#
# ---
# Submission:
# Submit your completed Python file with all the required functions and classes implemented. Include comments explaining your code where necessary.
