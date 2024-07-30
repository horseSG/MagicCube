# centre piece locates at the Origin

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from component import *
from operation import *

class MagicCube:
    OperateDict = {
        "U": RotUpper(),
        "U'":RotUpperPrime()
    }
    def __init__(self):
        self.Pieces = []
        for i in range(3):
            tlayer = []
            for j in range(3):
                tcolumn = []
                for k in range(3):
                    tpiece = Piece(i-1, j-1, k-1)
                    tcolumn.append(tpiece)
                tlayer.append(tcolumn)
            self.Pieces.append(tlayer)

    def Operate(self, operateName):
        operate = self.OperateDict[operateName]
        locPairs = self.OldNewLocation(operate.ChangeDim, operate.FixLayer, operate.RotMat)
        self.BackupColors()
        for slocPair in locPairs:
            self.Swap_PairColor(slocPair, operate)

    def BackupColors(self):
        for xid in range(3):
            for yid in range(3):
                for zid in range(3):
                    self.Pieces[xid][yid][zid].BackupColors()


    def Swap_PairColor(self, slocPair, operate):
        [ox, oy, oz] = slocPair[0]
        [nx, ny, nz] = slocPair[1]
        for i in range(len(self.Pieces[ox][oy][oz].Facets)):
            oldOri = self.Pieces[ox][oy][oz].Facets[i].Orientation
            newOri = operate.Conv_FacetOri[oldOri]
            self.Pieces[nx][ny][nz].OriDict[newOri].RecvColor(self.Pieces[ox][oy][oz].Facets[i].OldColor)
        self.Pieces[ox][oy][oz].Send = True
        self.Pieces[nx][ny][nz].Recv = True

    # return [[oldLoc, newLoc]]; o/nLoc each has three elements being listID in [0, 1, 2]
    def OldNewLocation(self, changeDim, fixLayer, rotMat):
        OldNewPair = []     # dimension: n*2*3
        for dimA_Old in [-1, 0, 1]:
            for dimB_Old in [-1, 0, 1]:
                # result = rotMat @ [dimA_Old, dimB_Old]
                result = np.dot(rotMat, [dimA_Old, dimB_Old])
                dimA_New, dimB_New = result
                cordOld = [None] * 3
                cordNew = [None] * 3
                dimA = changeDim[0]
                dimB = changeDim[1]
                dimFix = fixLayer[0]
                cordOld[dimA] = dimA_Old + 1
                cordOld[dimB] = dimB_Old + 1
                cordOld[dimFix] = fixLayer[1] + 1
                cordNew[dimA] = dimA_New + 1
                cordNew[dimB] = dimB_New + 1
                cordNew[dimFix] = fixLayer[1] + 1
                OldNewPair.append([cordOld, cordNew])
        return OldNewPair
        
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
    cube.Operate("U")
    # cube.Operate("U'")
    plot_demo(cube)

main()

    


