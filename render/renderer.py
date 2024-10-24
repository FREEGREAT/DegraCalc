class Renderer:
    def __init__(self, resolution, foco, y_distorter, left_right, up_down):
        self.resolution = resolution
        self.foco = foco
        self.y_distorter = y_distorter
        self.left_right = left_right
        self.up_down = up_down

    def project(self, cube):
        return [(round(2 * point[0] * self.foco / (self.foco + point[2])), 
                 round(point[1] * self.foco / ((self.foco + point[2]) * self.y_distorter))) 
                for point in cube]

    def get_lines(self, proj):
        connected_points = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4), (2, 6), 
                            (3, 5), (3, 6), (7, 6), (7, 5), (7, 4)]
        return [self.interpolate(proj[point0][0], proj[point0][1], proj[point1][0], proj[point1][1])
                for point0, point1 in connected_points]

    def interpolate(self, x0, y0, x1, y1):
        alpha = (y1 - y0 + 0.001) / (x1 - x0 + 0.001)
        beta = y0 - (alpha * x0)
        if alpha > 1 or alpha < -1:
            return [((round((y - beta) / (alpha + 0.001))), y) for y in range(int(min(y1, y0)), int(max(y1, y0) + 1))]
        else:
            return [(x, (round(x * alpha + beta))) for x in range(int(min(x1, x0)), int(max(x1, x0)) + 1)]

    def render(self, proj, lins):
        ascii_art = []
        for j in range(self.resolution):
            line = ""
            for i in range(self.resolution * 3):
                if (i - self.resolution * self.left_right, 
                    j - self.resolution * self.up_down) in proj:
                    line += "#"
                elif any((i - self.resolution * self.left_right, 
                          j - self.resolution * self.up_down) in lin for lin in lins):
                    line += "*"
                else:
                    line += " "
            ascii_art.append(line)
            print(line)
        return "\n".join(ascii_art)
