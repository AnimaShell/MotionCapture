import numpy as np


def stabilize(objict: object, source: dict, arg: int):
    return objict.stabilize(source, arg)


class Stabilizer(object):
    def stabilize(self, source: list, size: int):
        pass


class AVG(Stabilizer):
    def stabilize(self, source: list, size: int):
        queueSize = 2 * size + 1
        count = 0
        queue = []
        ans = []

        for value in source:
            queue.append(value)
            if count < queueSize:
                count += 1
            else:
                queue.pop(0)
            if count > size:
                ans.append(np.mean(queue))
        return ans
