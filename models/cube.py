from math import cos, sin, radians
from numpy import dot
import re

class Cube:
    def __init__(self, size_x=10, size_y=10, size_z=10, angle_x=0, angle_y=0, scale=1, color="White"):
        self.corners = [[-size_x, -size_y, -size_z], [size_x, -size_y, -size_z],
                        [-size_x, -size_y, size_z], [-size_x, size_y, -size_z],
                        [size_x, -size_y, size_z], [size_x, size_y, -size_z],
                        [-size_x, size_y, size_z], [size_x, size_y, size_z]]
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.scale = scale
        self.color = color

    def rotate(self):
        x_rotator = [[1, 0, 0],
                     [0, cos(radians(self.angle_x)), sin(radians(self.angle_x))],
                     [0, -sin(radians(self.angle_x)), cos(radians(self.angle_x))]]
        y_rotator = [[cos(radians(self.angle_y)), 0, -sin(radians(self.angle_y))],
                     [0, 1, 0],
                     [sin(radians(self.angle_y)), 0, cos(radians(self.angle_y))]]
        rotated_cube = [dot(dot(point, x_rotator), y_rotator) for point in self.corners]
        return self.scale_cube(rotated_cube)

    def scale_cube(self, cube):
        return [[point[0] * self.scale, point[1] * self.scale, point[2] * self.scale] for point in cube]

    def set_rotation(self, angle_x, angle_y):
        self.angle_x = max(-360, min(360, angle_x))
        self.angle_y = max(-360, min(360, angle_y))

    def set_scale(self, scale):
        if 1 <= scale <= 5:
            self.scale = scale
        else:
            print("Invalid scale. It must be between 1 and 5.")
    
    def save_to_file(self, filename, rendered_ascii):
            # Видалення всіх ANSI-кодів (форматування, кольори, стилі)
            clean_ascii = re.sub(r'\033\[\d+;?\d*;?\d*m', '', rendered_ascii)  
            with open(f"{filename}.txt", "w") as file:
                file.write(clean_ascii)
            print(f"Cube saved to {filename}.txt")
