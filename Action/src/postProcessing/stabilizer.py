import numpy as np
from Action.src.log.writeLog import Log


def stabilize(objict: object, source: dict, arg: int):
    try:
        return objict.stabilize(source, arg)
    except TypeError:
        Log.write("Error", "stabilizer的数据可能为空\n  ERROR at Action/src/postProcessing/stabilizer.py")
        return source
    except RuntimeWarning:
        Log.write("Error", "stabilizer的窗口大小设置错误\n  ERROR at Action/src/postProcessing/stabilizer.py")
        return source


class Stabilizer(object):
    def stabilize(self, source: list, size: int):
        pass


class AVG(Stabilizer):
    def stabilize(self, source: list, size: int = 0):
        opSize = 2 * size + 1
        queue = [source[0] for _ in range(opSize)]
        count = 0
        ans = []

        # 使用平均算子进行平滑
        for value in source:
            queue[count % opSize] = value
            ans.append(np.mean(queue))
            count += 1
        return ans


class tw_AVG(Stabilizer):
    def stabilize(self, source: list, size: int):
        opSize = 2 * size + 1
        queue = [source[0] * opSize for _ in range(opSize)]
        count = 0
        ans = []

        for value in source:
            queue[count % opSize] = value
            # 求出队列平均值
            avg = np.mean(queue)
            # 计算所需参数
            distance = abs(np.max(queue) - np.min(queue))
            op = [1 - (abs(queue[i] - avg) / distance) for i in range(opSize)]

            ans.append(np.mean([queue[i] * op[i] for i in range(opSize)]))
            count += 1
        return ans
