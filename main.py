
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import *

def plot_demo(cube):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for n in range(len(cube.Pieces[i][j][k].Facets)):
                    poly3d = cube.Pieces[i][j][k].Facets[n].Verts
                    color = cube.Pieces[i][j][k].Facets[n].Color
                    ax.add_collection3d(Poly3DCollection([poly3d], facecolors=color, linewidths=1, edgecolors='k'))

    # Set the aspect ratio to be equal
    ax.set_box_aspect([1, 1, 1])

    # Set the axis limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Interactive rotation
    ax.view_init(elev=30, azim=30)

    plt.show()

def main():
    cube = MagicCube()
    cube.Operate("R'")
    # cube.Operate("fbM'")
    plot_demo(cube)

main()