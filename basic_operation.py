# this module defines rotate operations

from component import FacetOrientation as fo

class Dict_ConvOri:
    yx = {
            fo.Back: fo.Right,
            fo.Right: fo.Front,
            fo.Front: fo.Left,
            fo.Left: fo.Back,
            fo.Up: fo.Up,
            fo.Down: fo.Down
        }
    xy = {
            fo.Back: fo.Left,
            fo.Right: fo.Back,
            fo.Front: fo.Right,
            fo.Left: fo.Front,
            fo.Up: fo.Up,
            fo.Down: fo.Down
        }
    zx = {
            fo.Back: fo.Up,
            fo.Up: fo.Front,
            fo.Front: fo.Down,
            fo.Down: fo.Back,
            fo.Left: fo.Left,
            fo.Right: fo.Right
        }
    xz = {
            fo.Back: fo.Down,
            fo.Up: fo.Back,
            fo.Front: fo.Up,
            fo.Down: fo.Front,
            fo.Left: fo.Left,
            fo.Right: fo.Right
        }
    zy = {
        fo.Front: fo.Front,
        fo.Back: fo.Back,
        fo.Up: fo.Right,
        fo.Right: fo.Down,
        fo.Down: fo.Left,
        fo.Left: fo.Up
    }
    yz = {
        fo.Front: fo.Front,
        fo.Back: fo.Back,
        fo.Up: fo.Left,
        fo.Right: fo.Up,
        fo.Down: fo.Right,
        fo.Left: fo.Down
    }

class RotUpper:
    ChangeDim = (0, 1)     # dimension (x, y)
    FixLayer = (2, 1)      # (dimision-z, z=1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.yx

class RotUpperPrime:
    ChangeDim = (0, 1)     # dimension (x, y)
    FixLayer = (2, 1)      # (dimision-z, z=1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.xy

class RotDown:
    ChangeDim = (0, 1)     # dimension (x, y)
    FixLayer = (2, -1)      # (dimision-z, z=-1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.xy

class RotDownPrime:
    ChangeDim = (0, 1)     # dimension (x, y)
    FixLayer = (2, -1)      # (dimision-z, z=-1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.yx

class Rot_udMid:
    ChangeDim = (0, 1)     # dimension (x, y)
    FixLayer = (2, 0)      # (dimision-z, z=0)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.yx

class Rot_udMidPrime:
    ChangeDim = (0, 1)     # dimension (x, y)
    FixLayer = (2, 0)      # (dimision-z, z=0)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.xy

class RotLeft:
    ChangeDim = (0, 2)     # dimension (x, z)
    FixLayer = (1, -1)      # (dimision-y, y=-1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.zx

class RotLeftPrime:
    ChangeDim = (0, 2)     # dimension (x, z)
    FixLayer = (1, -1)      # (dimision-y, y=-1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.xz

class RotRight:
    ChangeDim = (0, 2)     # dimension (x, z)
    FixLayer = (1, 1)      # (dimision-y, y=1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.xz

class RotRightPrime:
    ChangeDim = (0, 2)     # dimension (x, z)
    FixLayer = (1, 1)      # (dimision-y, y=1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.zx

class Rot_lrMid:
    ChangeDim = (0, 2)     # dimension (x, z)
    FixLayer = (1, 0)      # (dimision-y, y=1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.xz

class Rot_lrMidPrime:
    ChangeDim = (0, 2)     # dimension (x, z)
    FixLayer = (1, 0)      # (dimision-y, y=1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.zx

class RotFront:
    ChangeDim = (1, 2)      # dimension (y, z)
    FixLayer = (0, 1)       # (dimision-x, x=1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.zy

class RotFrontPrime:
    ChangeDim = (1, 2)      # dimension (y, z)
    FixLayer = (0, 1)       # (dimision-x, x=1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.yz    

class RotBack:
    ChangeDim = (1, 2)      # dimension (y, z)
    FixLayer = (0, -1)       # (dimision-x, x=-1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.yz

class RotBackPrime:
    ChangeDim = (1, 2)      # dimension (y, z)
    FixLayer = (0, -1)       # (dimision-x, x=-1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.zy

class Rot_fbMid:
    ChangeDim = (1, 2)      # dimension (y, z)
    FixLayer = (0, 0)       # (dimision-x, x=1)
    RotMat = [[0, 1], [-1, 0]]
    Conv_FacetOri = Dict_ConvOri.zy

class Rot_fbMidPrime:
    ChangeDim = (1, 2)      # dimension (y, z)
    FixLayer = (0, 0)       # (dimision-x, x=1)
    RotMat = [[0, -1], [1, 0]]
    Conv_FacetOri = Dict_ConvOri.yz