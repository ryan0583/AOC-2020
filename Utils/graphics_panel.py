import tkinter as tk


class GraphicsPanel:
    def __init__(self, tiles):
        self.tiles = tiles
        self.rects = {}
        self.root = tk.Tk()
        self.canvas = None
        self.text_component = None

    def update_canvas(self, point, color):
        rect = self.rects.get(point)
        if rect is None:
            rect = self.canvas.create_rectangle(point.x * GAME_SCALE, point.y * GAME_SCALE,
                                                point.x * GAME_SCALE + GAME_SCALE,
                                                point.y * GAME_SCALE + GAME_SCALE, fill=color)
            self.rects[point] = rect
        else:
            self.canvas.itemconfigure(rect, fill=color)

    def paint_canvas(self):
        self.root.update_idletasks()
        self.root.update()

    def init_game(self):
        def init_canvas():
            for point in self.tiles.keys():
                color = self.tiles.get(point)
                self.update_canvas(point, color)
            self.paint_canvas()

        x_dimension = (max(list(map(lambda position: position.x, self.tiles.keys()))) + 1) * GAME_SCALE
        y_dimension = (max(list(map(lambda position: position.y, self.tiles.keys()))) + 1) * GAME_SCALE

        self.canvas = tk.Canvas(self.root, width=x_dimension, height=y_dimension)
        self.canvas.pack()
        init_canvas()

    def add_text(self, text, color):
        self.text_component = self.canvas.create_text(GAME_SCALE * 2, GAME_SCALE * 2, fill=color,
                                font="Arial " + str(GAME_SCALE - GAME_SCALE // 2), anchor="w",
                                text=text)

    def update_text(self, text):
        self.canvas.itemconfigure(self.text_component, text=text)


GAME_SCALE = 20
