import stabilizer
from pruning import pruningMethod
from stabilizer import AVG


def postProcessing(motions: dict, st: int = 0, cut: float = 0) -> dict:
    try:
        if st > 0:
            # 对数据进行平滑处理
            motions = stabilize(motions, st)
        if cut > 0:
            # 对数据进行剪枝处理
            motions = pruningMethod(motions, cut)
    finally:
        return motions


def stabilize(inputMotions: dict, size: int):
    for bone in inputMotions.keys():
        for key in inputMotions[bone].keys():
            inputMotions[bone][key] = stabilizer.stabilize(AVG(), inputMotions[bone][key], size)
    return inputMotions


if __name__ == "__main__":
    # bottling()
    pass
