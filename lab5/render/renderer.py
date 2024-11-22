from utils.color_config import ColorConfig

class Renderer:
    """
    Клас Renderer

    Призначення:
        Використовується для проєкції, обробки та візуалізації тривимірних об'єктів у вигляді ASCII-графіки.

    Атрибути:
        resolution (int): Роздільна здатність рендера.
        foco (int): Фокусна відстань для проєкції.
        y_distorter (float): Спотворення по осі Y.
        left_right (float): Зміщення по горизонталі (X).
        up_down (float): Зміщення по вертикалі (Y).

    Методи:
        project(cube):
            Проєктує тривимірні точки об'єкта на двовимірну площину.

            Параметри:
                cube (list[tuple]): Список координат вершин об'єкта (x, y, z).

            Повертає:
                list[tuple]: Список координат після проєкції (x, y).
        
        get_lines(proj):
            Створює лінії між проєктованими точками, що формують рендеринг об'єкта.

            Параметри:
                proj (list[tuple]): Список двовимірних координат точок.

            Повертає:
                list[list[tuple]]: Список ліній як наборів координат точок.

        interpolate(x0, y0, x1, y1):
            Інтерполює координати між двома точками, формуючи пряму.

            Параметри:
                x0, y0 (int): Координати початкової точки.
                x1, y1 (int): Координати кінцевої точки.

            Повертає:
                list[tuple]: Список координат точок на прямій.

        render(proj, lins, cube_color):
            Візуалізує об'єкт у вигляді ASCII-графіки.

            Параметри:
                proj (list[tuple]): Список проєктованих точок.
                lins (list[list[tuple]]): Лінії, які формують каркас об'єкта.
                cube_color (str): Колір об'єкта.

            Повертає:
                str: ASCII-графіка об'єкта.

    Обробка виключень:
        Усі методи обробляють помилки та повертають відповідне повідомлення, якщо виникають проблеми під час виконання.
    """

    def __init__(self, resolution, foco, y_distorter, left_right, up_down):
        try:
            self.resolution = resolution
            self.foco = foco
            self.y_distorter = y_distorter
            self.left_right = left_right
            self.up_down = up_down
        except Exception as e:
            print(f"Error initializing renderer: {e}")

    def project(self, cube):
        try:
            return [(round(2 * point[0] * self.foco / (self.foco + point[2])),
                     round(point[1] * self.foco / ((self.foco + point[2]) * self.y_distorter)))
                    for point in cube]
        except Exception as e:
            print(f"Error during projection: {e}")
            return []  

    def get_lines(self, proj):
        try:
            connected_points = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4), (2, 6), 
                                (3, 5), (3, 6), (7, 6), (7, 5), (7, 4)]
            return [self.interpolate(proj[point0][0], proj[point0][1], proj[point1][0], proj[point1][1])
                    for point0, point1 in connected_points]
        except Exception as e:
            print(f"Error during line calculation: {e}")
            return []  

    def interpolate(self, x0, y0, x1, y1):
        try:
            alpha = (y1 - y0 + 0.001) / (x1 - x0 + 0.001)
            beta = y0 - (alpha * x0)
            if alpha > 1 or alpha < -1:
                return [((round((y - beta) / (alpha + 0.001))), y) for y in range(int(min(y1, y0)), int(max(y1, y0) + 1))]
            else:
                return [(x, (round(x * alpha + beta))) for x in range(int(min(x1, x0)), int(max(x1, x0)) + 1)]
        except Exception as e:
            print(f"Error during interpolation: {e}")
            return []
        
    def render(self, proj, lins, cube_color):
        ascii_art = []
        color_code = ColorConfig.get_color_code(cube_color)
        reset_code = ColorConfig.COLORS["Reset"]

        for j in range(self.resolution):
            line = ""
            for i in range(self.resolution * 3):
                if (i - self.resolution * self.left_right, 
                    j - self.resolution * self.up_down) in proj:
                    line += f"{color_code}#{reset_code}"
                elif any((i - self.resolution * self.left_right, 
                          j - self.resolution * self.up_down) in lin for lin in lins):
                    line += f"{color_code}*{reset_code}"
                else:
                    line += " "
            ascii_art.append(line)
            print(line)
        return "\n".join(ascii_art)
