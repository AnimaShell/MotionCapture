import json
import os
from Action.src.log.writeLog import Log

default_output = "../../output"
default_filename = "Miku_desu"


def save(source: dict, inputPath: str, outputDir: str = None, outfileName: str = None):
    if outputDir is None:
        outputDir = default_output
    # 创建输出路径
    if not os.path.isdir(outputDir):
        os.makedirs(outfileName)
    # 获取输出文件名
    if outfileName is None and inputPath is not None:
        outfileName = inputPath.split("/")[-1].split(".")[0]
    elif outfileName is None:
        outfileName = default_filename
    count = 1
    while os.path.isfile(outputDir + outfileName + str(count) + ".json"):
        count += 1
    outfileName += str(count)
    # 尝试将source写入
    try:
        with open(outputDir + outfileName + ".json", "w") as out:
            json.dump(source, out)
        return outputDir + outfileName + ".json"
    except TypeError:
        Log.write("Error", "尝试写入json文件的字典错误，请检查其是否传入且正确\n  ERROR at Action/src/save/saveFile.py")
