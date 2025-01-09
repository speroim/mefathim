from PIL import Image
import numpy as np

def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    rgb_array = np.array(image)
    grayscale_array = np.dot(rgb_array[..., :3], [0.2989, 0.5870, 0.1140])
    binary_array = (grayscale_array >= 128).astype(int)
    print(binary_array)
convert_to_grayscale("./mazes/maze1.jpg")


class PixelNode:
    def __init__(self, x, y, color=None):
        self.visited = False
        self.distance = float("inf")
        self.x = x
        self.y = y
        self.color = color

    def __lt__(self, other):
        return self.distance < self.other



class PriorityQueue:
    def __init__(self):

        self.heap = []
        
    def insert(self, node):

        self.heap.append(node)
        self._heapify_up(len(self.heap)-1)

        """
        Insert a PixelNode into the priority queue.

        :param node: The PixelNode to be inserted
        """

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