import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QWidget
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

        main_layout.addWidget(self.canvas)

        button_layout = QVBoxLayout()

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText('Enter operations')
        self.input_box.returnPressed.connect(self.handle_input)
        button_layout.addWidget(self.input_box)

        self.allOperations = ''
        self.text_box = QTextEdit(self)
        self.text_box.setReadOnly(True)
        button_layout.addWidget(self.text_box)

        self.button0 = QPushButton('Reset Cube')
        self.button0.clicked.connect(self.ResetCube)
        button_layout.addWidget(self.button0)
        
        self.button1 = QPushButton('R')
        # self.button1.clicked.connect(self.operation_R)
        self.button1.clicked.connect(lambda: ButtonAction.Act(self, 'R'))
        button_layout.addWidget(self.button1)

        self.button2 = QPushButton('U')
        self.button2.clicked.connect(self.operation_U)
        button_layout.addWidget(self.button2)

        self.button3 = QPushButton('F')
        self.button3.clicked.connect(self.operation_F)
        button_layout.addWidget(self.button3)

        self.button4 = QPushButton('z90')
        self.button4.clicked.connect(self.operation_z90)
        button_layout.addWidget(self.button4)

        main_layout.addLayout(button_layout)

        self.show()

    def ResetCube(self):
        self.cube = MagicCube()
        self.allOperations = ''
        self.text_box.setPlainText(self.allOperations)
        self.plot_cube()

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

    def operation_R(self):
        self.cube.Operate('R')
        self.plot_cube()

    def operation_U(self):
        self.cube.Operate('U')
        self.plot_cube()

    def operation_F(self):
        self.cube.Operate('F')
        self.plot_cube()
        
    def operation_z90(self):
        self.cube.Operate('z90')
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
        self.ax.view_init(elev=30, azim=30)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CubeApp()
    sys.exit(app.exec_())