from models.cube import Cube
from render.renderer import Renderer
from controllers.user_input import UserInput
import os
import time

if __name__ == "__main__":
    user_input = UserInput(None)

    size_x, size_y, size_z = user_input.get_initial_size()
    cube = Cube(size_x, size_y, size_z)
    user_input.cube = cube  
    
    renderer = Renderer(resolution=40, foco=40, y_distorter=1.1, left_right=1.5, up_down=0.5)

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            rotated_cube = cube.rotate()
            projection = renderer.project(rotated_cube)
            lines = renderer.get_lines(projection)
            rendered_ascii = renderer.render(projection, lines, cube.color)
            time.sleep(0.5)
            action = user_input.get_next_action()

            if action == "1":
                user_input.get_rotation_input()
            elif action == "2":
                user_input.change_color()
            elif action == "3":
                user_input.get_scale_input()
            elif action == "4":
                filename = input("Enter filename to save the cube: ")
                cube.save_to_file(filename, rendered_ascii)
            elif action == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("Program interrupted.")
