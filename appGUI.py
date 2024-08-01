import sys
import re
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import *

class ButtonAction:
    @classmethod
    def Act(cls, app_instance, action):
        app_instance.cube.Operate(action)
        app_instance.allOperations += action + ", "
        app_instance.text_box.setPlainText(app_instance.allOperations)
        app_instance.plot_cube()

class CubeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magic Cube")
        self.setGeometry(100, 100, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        # layout.addWidget(self.canvas)
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.cube = MagicCube()
        self.plot_cube()

        main_layout.addWidget(self.canvas, stretch=5)

        operation_layout = QVBoxLayout()

        self.button_orient = QPushButton('Face Front')
        self.button_orient.clicked.connect(self.FaceFront)
        operation_layout.addWidget(self.button_orient)

        # input operation names, separated by space or comma
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText('Enter operations')
        self.input_box.returnPressed.connect(self.handle_input)
        operation_layout.addWidget(self.input_box)

        # show historical operations
        self.allOperations = ''
        self.text_box = QTextEdit(self)
        self.text_box.setReadOnly(True)
        operation_layout.addWidget(self.text_box)

        cubeSet_layout = QHBoxLayout()
        # recovery ordered cube
        self.button0 = QPushButton('Reset Cube')
        self.button0.clicked.connect(self.ResetCube)
        cubeSet_layout.addWidget(self.button0)
        # scramble to disorder
        self.messy_box = QLineEdit(self)
        self.messy_box.setPlaceholderText('# scramble')
        self.messy_box.returnPressed.connect(self.Scramble)
        cubeSet_layout.addWidget(self.messy_box)
        operation_layout.addLayout(cubeSet_layout)

        hint_layout = QHBoxLayout()
        self.button_revhint = QPushButton('Show Scramble')
        self.button_revhint.clicked.connect(self.RevealHint)
        hint_layout.addWidget(self.button_revhint)
        self.button_hidehint = QPushButton('Hide Scramble')
        self.button_hidehint.clicked.connect(self.HideHint)
        hint_layout.addWidget(self.button_hidehint)
        operation_layout.addLayout(hint_layout)

        self.hint_box = QTextEdit(self)
        self.hint_box.setReadOnly(True)
        operation_layout.addWidget(self.hint_box)
        
        optDict_layout = QVBoxLayout()
        optR_layout = QHBoxLayout()
        # Right
        self.button1a = QPushButton('R')
        self.button1a.clicked.connect(lambda: ButtonAction.Act(self, 'R'))
        optR_layout.addWidget(self.button1a)
        # Right Prime
        self.button1b = QPushButton("R'")
        self.button1b.clicked.connect(lambda: ButtonAction.Act(self, "R'"))
        optR_layout.addWidget(self.button1b)
        # Double Right
        self.button1c = QPushButton("R2")
        self.button1c.clicked.connect(lambda: ButtonAction.Act(self, "R2"))
        optR_layout.addWidget(self.button1c)
        optDict_layout.addLayout(optR_layout)

        optL_layout = QHBoxLayout()
        # Left
        self.button2a = QPushButton('L')
        self.button2a.clicked.connect(lambda: ButtonAction.Act(self, 'L'))
        optL_layout.addWidget(self.button2a)
        # Left Prime
        self.button2b = QPushButton("L'")
        self.button2b.clicked.connect(lambda: ButtonAction.Act(self, "L'"))
        optL_layout.addWidget(self.button2b)
        # Double Left
        self.button2c = QPushButton("L2")
        self.button2c.clicked.connect(lambda: ButtonAction.Act(self, "L2"))
        optL_layout.addWidget(self.button2c)
        optDict_layout.addLayout(optL_layout)

        optU_layout = QHBoxLayout()
        # Up
        self.button3a = QPushButton('U')
        self.button3a.clicked.connect(lambda: ButtonAction.Act(self, 'U'))
        optU_layout.addWidget(self.button3a)
        # Up Prime
        self.button3b = QPushButton("U'")
        self.button3b.clicked.connect(lambda: ButtonAction.Act(self, "U'"))
        optU_layout.addWidget(self.button3b)
        # Double Up
        self.button3c = QPushButton("U2")
        self.button3c.clicked.connect(lambda: ButtonAction.Act(self, "U2"))
        optU_layout.addWidget(self.button3c)
        optDict_layout.addLayout(optU_layout)

        optD_layout = QHBoxLayout()
        # Down
        self.button4a = QPushButton('D')
        self.button4a.clicked.connect(lambda: ButtonAction.Act(self, 'D'))
        optD_layout.addWidget(self.button4a)
        # Down Prime
        self.button4b = QPushButton("D'")
        self.button4b.clicked.connect(lambda: ButtonAction.Act(self, "D'"))
        optD_layout.addWidget(self.button4b)
        # Double Down
        self.button4c = QPushButton("D2")
        self.button4c.clicked.connect(lambda: ButtonAction.Act(self, "D2"))
        optD_layout.addWidget(self.button4c)
        optDict_layout.addLayout(optD_layout)

        optF_layout = QHBoxLayout()
        # Front
        self.button5a = QPushButton('F')
        self.button5a.clicked.connect(lambda: ButtonAction.Act(self, 'F'))
        optF_layout.addWidget(self.button5a)
        # Front Prime
        self.button5b = QPushButton("F'")
        self.button5b.clicked.connect(lambda: ButtonAction.Act(self, "F'"))
        optF_layout.addWidget(self.button5b)
        # Double Front
        self.button5c = QPushButton("F2")
        self.button5c.clicked.connect(lambda: ButtonAction.Act(self, "F2"))
        optF_layout.addWidget(self.button5c)
        optDict_layout.addLayout(optF_layout)

        optB_layout = QHBoxLayout()
        # Back
        self.button6a = QPushButton('B')
        self.button6a.clicked.connect(lambda: ButtonAction.Act(self, 'B'))
        optB_layout.addWidget(self.button6a)
        # Back Prime
        self.button6b = QPushButton("B'")
        self.button6b.clicked.connect(lambda: ButtonAction.Act(self, "B'"))
        optB_layout.addWidget(self.button6b)
        # Double Back
        self.button6c = QPushButton("B2")
        self.button6c.clicked.connect(lambda: ButtonAction.Act(self, "B2"))
        optB_layout.addWidget(self.button6c)
        optDict_layout.addLayout(optB_layout)

        optZ_layout = QHBoxLayout()
        # Z90
        self.button7a = QPushButton('Z90')
        self.button7a.clicked.connect(lambda: ButtonAction.Act(self, 'Z90'))
        optZ_layout.addWidget(self.button7a)
        # Z90 Prime
        self.button7b = QPushButton("Z90'")
        self.button7b.clicked.connect(lambda: ButtonAction.Act(self, "Z90'"))
        optZ_layout.addWidget(self.button7b)
        # Double Z90
        self.button7c = QPushButton("Z180")
        self.button7c.clicked.connect(lambda: ButtonAction.Act(self, "Z180"))
        optZ_layout.addWidget(self.button7c)
        optDict_layout.addLayout(optZ_layout)

        optY_layout = QHBoxLayout()
        # Y90
        self.button8a = QPushButton('Y90')
        self.button8a.clicked.connect(lambda: ButtonAction.Act(self, 'Y90'))
        optY_layout.addWidget(self.button8a)
        # Y90 Prime
        self.button8b = QPushButton("Y90'")
        self.button8b.clicked.connect(lambda: ButtonAction.Act(self, "Y90'"))
        optY_layout.addWidget(self.button8b)
        # Double Y90
        self.button8c = QPushButton("Y180")
        self.button8c.clicked.connect(lambda: ButtonAction.Act(self, "Y180"))
        optY_layout.addWidget(self.button8c)
        optDict_layout.addLayout(optY_layout)

        optX_layout = QHBoxLayout()
        # X90
        self.button9a = QPushButton('X90')
        self.button9a.clicked.connect(lambda: ButtonAction.Act(self, 'X90'))
        optX_layout.addWidget(self.button9a)
        # X90 Prime
        self.button9b = QPushButton("X90'")
        self.button9b.clicked.connect(lambda: ButtonAction.Act(self, "X90'"))
        optX_layout.addWidget(self.button9b)
        # Double X90
        self.button9c = QPushButton("X180")
        self.button9c.clicked.connect(lambda: ButtonAction.Act(self, "X180"))
        optX_layout.addWidget(self.button9c)
        optDict_layout.addLayout(optX_layout)

        operation_layout.addLayout(optDict_layout)

        # stretch setting no work
        operation_layout.setStretch(0, 2)   # ortate cordinate to face front
        operation_layout.setStretch(1, 2)   # enter operations
        operation_layout.setStretch(2, 5)   # text box of operation history
        operation_layout.setStretch(3, 2)   # recovery / scramble
        operation_layout.setStretch(4, 2)   # show / hide scramble hint
        operation_layout.setStretch(5, 5)   # text box of scramble history
        operation_layout.setStretch(5, 9)   # list of basic operations

        for button in [self.button1a, self.button1b, self.button1c,
                       self.button2a, self.button2b, self.button2c,
                       self.button3a, self.button3b, self.button3c,
                       self.button4a, self.button4b, self.button4c,
                       self.button5a, self.button5b, self.button5c,
                       self.button6a, self.button6b, self.button6c,
                       self.button7a, self.button7b, self.button7c,
                       self.button8a, self.button8b, self.button8c,
                       self.button9a, self.button9b, self.button9c,]:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setMinimumSize(0, 0)  # Explicitly set the minimum size

        main_layout.addLayout(operation_layout, stretch=3)

        self.show()

    def ResetCube(self):
        self.cube = MagicCube()
        self.allOperations = ''
        self.text_box.setPlainText(self.allOperations)
        self.plot_cube()

    def Scramble(self):
        input_number = int(self.messy_box.text())
        scrambles = [random.choice(list(OperateDict.keys())) for _ in range(input_number)]
        self.HintText = ', '.join(scrambles)
        for operation in scrambles:
            self.cube.Operate(operation)
        self.plot_cube()

    def RevealHint(self):
        self.hint_box.setPlainText(self.HintText)
        
    def HideHint(self):
        self.hint_box.setPlainText('')

    def FaceFront(self):
        self.ax.view_init(elev=30, azim=30)
        self.canvas.draw()

    def handle_input(self):
        input_text = self.input_box.text()
        self.process_input(input_text)
        self.input_box.clear()

    def process_input(self, command):
        command_list = re.split(r'[ ,]+', command)
        self.allOperations += ', '.join(command_list)
        self.allOperations += ', '
        for operate in command_list:
            self.cube.Operate(operate)
        self.text_box.setPlainText(self.allOperations)
        self.plot_cube()

    def plot_cube(self):
        self.ax.clear()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for n in range(len(self.cube.Pieces[i][j][k].Facets)):
                        poly3d = self.cube.Pieces[i][j][k].Facets[n].Verts
                        color = self.cube.Pieces[i][j][k].Facets[n].Color
                        self.ax.add_collection3d(Poly3DCollection([poly3d], facecolors=color, linewidths=1, edgecolors='k'))

        # Set the aspect ratio to be equal
        self.ax.set_box_aspect([1, 1, 1])

        # Set the axis limits
        self.ax.set_xlim([-2, 2])
        self.ax.set_ylim([-2, 2])
        self.ax.set_zlim([-2, 2])
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_zticklabels([])

        # Set labels
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        # Interactive rotation
        # self.ax.view_init(elev=30, azim=30)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CubeApp()
    sys.exit(app.exec_())