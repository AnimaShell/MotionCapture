import os
import cv2
import json
import motionCapture.capture as capture
import resolution
from Action.src.log.writeLog import Log


def readImage(path: str):
    if path is not None and os.path.isfile(path):
        img = cv2.imread(path)
        return img
    return None


def readVideo(path: str):
    if path is not None and os.path.isfile(path):
        video = cv2.VideoCapture(path)
        if video.isOpened():
            return video
    return None


def process(path: str, isImage: bool = True, model: str = None):
    # 载入模型输入信息
    try:
        with open("../../config/models/modelsInfo-config.json", "r") as c:
            cfg = json.load(c)
            if model in cfg.keys():
                cfg = cfg[model]["input"]
            else:
                cfg = cfg["default"]["input"]
    except TypeError:
        Log.write("Error", "modelsInfo-config.json载入失败\n  ERROR at Action/src/processing/processing.py")
    except FileNotFoundError:
        Log.write("Error", "未找到modelsInfo-config.json\n  ERROR at Action/src/processing/processing.py")
    else:
        if isImage:
            # 读取图片
            img = readImage(path)
            # 将图片分辨率处理为预设大小
            img = resolution.adapt(img, cfg)
            motions = capture.doPs([img * 2], model)
        else:
            motions = []
            # 读取视频
            video = readVideo(path)
            queue = [0]
            while True:
                # 读取视频中的每一帧
                s, img = video.read()
                if s:
                    # 将读取到的每一帧图像处理为预设大小
                    img = resolution.adapt(img, cfg)
                    queue.pop(0)
                    while len(queue) < 2:
                        queue.append(img)
                    motions.append(capture.doPs(queue, model))
        return motions
