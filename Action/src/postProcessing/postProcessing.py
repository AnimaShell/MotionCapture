import copy
import json
import stabilizer
from datetime import datetime
from stabilizer import AVG


bones_config = "../../../Action/config/bones-config.json"
bones_parent = "../../../Action/config/bones-parent-config.json"
bones_mapper = "../../../Action/config/bonesName-mapper.json"


def postProcessing(source: list, st: int = 0) -> dict:

    motions = bottling(source)

    if st > 0:
        for bone in motions.keys():
            for key in motions[bone].keys():
                motions[bone][key] = stabilizer.stabilize(AVG(), motions[bone][key], st)
    return motions


# 将source分装为字典
def bottling(source: list = None):
    # 读取模型配置文件
    try:
        with open(bones_config, "r") as bc:
            bonesConfig = json.load(bc)
        with open(bones_parent, "r") as bp:
            bonesParent = json.load(bp)
        with open(bones_mapper, "r") as bm:
            bonesName = json.load(bm)
    except FileNotFoundError:
        print("Json load Error")
    # 生成空的帧字典
    motions = dict()
    for boneName in bonesParent:
        if boneName in bonesName.keys():
            motions[bonesName[boneName]] = copy.deepcopy(bonesConfig["PRBone"] if boneName in {"bone0", "bone1"} else bonesConfig["RBone"])
            motions[bonesName[boneName]]["parent"] = bonesName[bonesParent[boneName][0]] if bonesParent[boneName][0] in bonesName.keys() else bonesParent[boneName][0]
        else:
            motions[boneName] = copy.deepcopy(bonesConfig["PRBone"] if boneName in {"bone0", "bone1"} else bonesConfig["RBone"])
            motions[boneName]["parent"] = bonesParent[boneName][0]
    # 将source的数据添加近帧字典
    try:
        for frame in range(len(source)):
            index = 0
            # frame的值依次附给motions
            for boneName in motions.keys():
                for key in motions[boneName]["data"].keys():
                    motions[boneName]["data"][key] = [source[index], frame]
                    index += 1
    except IndexError:  # 捕捉错误，网络模型的输出与骨骼模型不一致

        print("Index out of range, please check the model and bones-config")
    except TypeError:   # 捕捉错误，没有接收到网络模型的输出
        print("Post process No input")

    return motions


def pruning(source: dict, pt: float = 0):
    if pt > 0:
        for bone in source.keys():
            pass


if __name__ == "__main__":
    bottling()
