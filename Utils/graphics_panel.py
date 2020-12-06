import tkinter as tk
from Utils.point import Point


class GraphicsPanel:
    def __init__(self, tiles, scale):
        self.tiles = tiles
        self.rects = {}
        self.root = tk.Tk()
        self.canvas = None
        self.text_component = None
        self.scale = scale

    @staticmethod
    def create_empty_panel(x_dim, y_dim, scale):
        tile_map = {}
        for x in range(0, x_dim):
            for y in range(0, y_dim):
                tile_map[Point(x, y)] = "black"
        return GraphicsPanel(tile_map, scale)

    def reset(self):
        for point in self.tiles.keys():
            self.update_canvas(point, "black")

    def update_canvas_with_offset(self, point, color, x_offset, y_offset):
        normalised_point = Point(x_offset + point.x, y_offset + point.y)
        self.update_canvas(normalised_point, color)

    def update_canvas(self, point, color):
        rect = self.rects.get(point)
        if rect is None:
            rect = self.canvas.create_rectangle(point.x * self.scale, point.y * self.scale,
                                                point.x * self.scale + self.scale,
                                                point.y * self.scale + self.scale, fill=color)
            self.rects[point] = rect
        else:
            self.canvas.itemconfigure(rect, fill=color)

    def paint_canvas(self):
        self.root.update_idletasks()
        self.root.update()

    def init_canvas(self):
        x_dimension = (max(list(map(lambda position: position.x, self.tiles.keys()))) + 1) * self.scale
        y_dimension = (max(list(map(lambda position: position.y, self.tiles.keys()))) + 1) * self.scale

        self.canvas = tk.Canvas(self.root, width=x_dimension, height=y_dimension)
        self.canvas.pack()

        for point in self.tiles.keys():
            color = self.tiles.get(point)
            self.update_canvas(point, color)

    def add_text(self, text, color):
        self.text_component = self.canvas.create_text(self.scale * 2, self.scale * 2, fill=color,
                                font="Courier " + str(self.scale - self.scale // 2), anchor="w",
                                text=text)

    def update_text(self, text):
        self.canvas.itemconfigure(self.text_component, text=text)
