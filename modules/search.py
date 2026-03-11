import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import os
from .frame import Frame_create
from .load_img import ImageLoad


class Block_search:
    def __init__(self, parent):
        self.LAYOUT = widgets.QHBoxLayout()
        self.LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.block_parent = Frame_create(self.LAYOUT, width = 790, height = 40, color = "transparent")
        parent.addWidget(self.block_parent)
        layiut_sett = widgets.QHBoxLayout()
        layiut_sett.setContentsMargins(0, 0, 0, 0)
        frame_settings = Frame_create(layiut_sett, 175, 36)

        self.button = widgets.QPushButton(parent= frame_settings)
        self.button.setStyleSheet("border-radius: 4px; background-color: rgba(0, 0, 0, 51)")
        self.button.setFixedSize(36, 36)
        self.path_img2 = os.path.abspath(os.path.join(__file__, "..", "..", "media", "settings.png"))
        self.ICON_BUTTON2 = gui.QIcon(self.path_img2)
        self.button.setIcon(self.ICON_BUTTON2)
        layiut_sett.addWidget(self.button)
        self.LABEL = widgets.QLabel(parent=frame_settings, text= "Налаштування")
        self.LABEL.setStyleSheet("font-size: 14px")
        layiut_sett.addWidget(self.LABEL)
        
        self.SEARCH_LAYOUT = widgets.QHBoxLayout()
        self.SEARCH_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.SEARCH_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignVCenter)
        self.FRAME = Frame_create(self.SEARCH_LAYOUT, width = 281, height = 40)
        self.FRAME.setStyleSheet("border-radius: 4px; background-color: rgba(0, 0, 0, 51)")
        self.LAYOUT.addWidget(frame_settings)
        self.LAYOUT.addStretch()
        self.LAYOUT.addWidget(self.FRAME)
        self.IMAGE = ImageLoad(25, 25, self.FRAME, 'search.png')
        self.IMAGE.setStyleSheet("background-color: transparent")
        self.SEARCH_BOX = widgets.QLineEdit(self.FRAME)
        self.SEARCH_BOX.setFixedSize(245, 42)
        self.SEARCH_BOX.setPlaceholderText('Пошук')
        self.SEARCH_BOX.setStyleSheet("color: white; font-size: 22px; background-color: transparent")
        self.SEARCH_LAYOUT.addStretch()
        self.SEARCH_LAYOUT.addWidget(self.SEARCH_BOX, core.Qt.AlignmentFlag.AlignLeft)

    def reset_search(self):
        self.block_parent.setParent(None)