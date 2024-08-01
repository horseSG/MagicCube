
from basic_operation import *

OperateDict = {
        "U": RotUpper,
        "U'":RotUpperPrime,
        "U2": [RotUpper, RotUpper],
        "D": RotDown,
        "D'": RotDownPrime,
        "D2": [RotDown, RotDown],
        "L": RotLeft,
        "L'":RotLeftPrime,
        "L2": [RotLeft, RotLeft],
        "R": RotRight,
        "R'": RotRightPrime,
        "R2": [RotRight, RotRight],
        "F": RotFront,
        "F'": RotFrontPrime,
        "F2": [RotFront, RotFront],
        "B": RotBack,
        "B'": RotBackPrime,
        "B2": [RotBack, RotBack],
        # "udM": Rot_udMid,
        # "udM'": Rot_udMidPrime,
        # "lrM": Rot_lrMid,
        # "lrM'": Rot_lrMidPrime,
        # "fbM": Rot_fbMid,
        # "fbM'": Rot_fbMidPrime,
        "Z90": [RotUpperPrime, Rot_udMidPrime, RotDown],    # right hand spiral
        "Z90'": [RotUpper, Rot_udMid, RotDownPrime],
        "Z180": [RotUpper, RotUpper, Rot_udMid, Rot_udMid, RotDownPrime, RotDownPrime],
        "Y90": [RotRightPrime, Rot_lrMidPrime, RotLeft],
        "Y90'": [RotRight, Rot_lrMid, RotLeftPrime],
        "Y180": [RotRight, RotRight, Rot_lrMid, Rot_lrMid, RotLeftPrime, RotLeftPrime],
        "X90": [RotFrontPrime, Rot_fbMidPrime, RotBack],
        "X90'": [RotFront, Rot_fbMid, RotBackPrime],
        "X180": [RotFront, RotFront, Rot_fbMid, Rot_fbMid, RotBackPrime, RotBackPrime]
    }