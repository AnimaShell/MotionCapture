import json
import copy
import os
from Action.src.log.writeLog import Log


bones_config = "bones-config.json"
bones_parent = "bones-parent-config.json"
bones_mapper = "bonesName-mapper.json"


# 将source分装为字典
def bottling(source: list = None, model: str = None):
    # 定位模型配置文件
    if os.path.isdir("../../config/bones/" + model):
        path = "../../config/bones/" + model + "/"
    else:
        path = "../../config/bones/default/"
    # 读取模型配置文件
    try:
        with open(path + bones_config, "r") as bc:
            bonesConfig = json.load(bc)
        with open(path + bones_parent, "r") as bp:
            bonesParent = json.load(bp)
        with open(path + bones_mapper, "r") as bm:
            bonesName = json.load(bm)
    except [FileNotFoundError, TypeError]:
        Log.write("Error", "Json载入失败\n  ERROR at Action/src/postProcessing/bottling.py\n  Json in Action/config/bones")
    else:
        # 生成空的帧字典
        motions = dict()
        for boneName in bonesParent.keys():
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
            Log.write("Error", "数据分装为字典时下标越界，请确保网络输出元素个数与bones除parent外所需参数的个数一致\n  ERROR at Action/src/postProcessing/bottling.py")
        except TypeError:   # 捕捉错误，没有接收到网络模型的输出
            Log.write("Error", "bottling没有得到参数，请确保网络正确向postProcessing传递参数\n  ERROR at Action/src/postProcessing/bottling.py")
        else:
            return motions
