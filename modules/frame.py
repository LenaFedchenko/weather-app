import PyQt6.QtWidgets as widgets

class Frame_create(widgets.QFrame):
    def __init__(self, layout, width = None, height= None, color= None):
        super().__init__()
        if color != None:
            self.setStyleSheet(f"background-color: {color}; ")
        if width != None and height != None:
            self.setFixedSize(width, height)
        self.setLayout(layout)