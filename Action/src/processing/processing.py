import os
import cv2
import motionCapture.capture as capture
from motionCapture.capture import MilKu
import resolution


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


def processing(path: str, isImage: bool):
    if isImage:
        img = readImage(path)
        img = resolution.adapt(img)
        motions = capture.doPs(MilKu, [img * 3])
    else:
        motions = []
        video = readVideo(path)
        queue = [0]
        while True:
            s, img = video.read()
            if s:
                img = resolution.adapt(img)
                queue.pop(0)
                while len(queue) < 3:
                    queue.append(img)
                motions.append(capture.doPs(MilKu, queue))
    return motions
