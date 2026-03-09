import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
from .frame import Frame_create
from .load_img import ImageLoad


class Block_search:
    def __init__(self, parent):
        self.LAYOUT = widgets.QHBoxLayout()
        self.block_parent = Frame_create(self.LAYOUT, width = 790, height = 40, color = "red")
        self.LAYOUT.setContentsMargins(0, 0, 0, 0)
        # self.LAYOUT.setAlignment(core.Qt.AlignmentFlag.align)
        parent.addWidget(self.block_parent)
        layiut_sett = widgets.QHBoxLayout()
        frame_settings = Frame_create(layiut_sett, 150, 36)

        self.button = widgets.QPushButton("fffff")
        self.button.setFixedSize(36, 36)
        layiut_sett.addWidget(self.button)
        self.LABEL = widgets.QLabel(parent=frame_settings, text= "Налаштування")
        layiut_sett.addWidget(self.LABEL)
        self.LAYOUT.addWidget(frame_settings)
        
        self.SEARCH_LAYOUT = widgets.QHBoxLayout()
        self.FRAME = Frame_create(self.SEARCH_LAYOUT, width = 281, height = 40, color = "green")
        self.LAYOUT.addWidget(self.FRAME)
        self.IMAGE = ImageLoad(25, 22, self.FRAME, 'search.png')
        # self.SEARCH_LAYOUT.addWidget(self.IMAGE)
        self.SEARCH_BOX = widgets.QLineEdit(self.FRAME)
        self.SEARCH_BOX.setFixedSize(220, 22)
        self.SEARCH_BOX.setPlaceholderText('Пошук')
        self.SEARCH_LAYOUT.addWidget(self.SEARCH_BOX)
        self.SEARCH_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignVCenter)

    def reset_search(self):
        self.block_parent.setParent(None)