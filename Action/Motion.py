from src.processing.processing import processing
from src.postProcessing.postProcessing import postProcessing


class ActionConte:
    def __int__(self, Input: str, Output: str, output_name: str = None, isImage: bool = True,
                models: list or tuple or set = None, stabilization: int = 0, pruning: float = 0):
        self.Input = Input
        self.Output = Output
        self.filename = output_name
        self.isImage = isImage
        self.models = models
        self.stabilization = stabilization
        self.pruning = pruning

    # 开始计算
    def doAction(self) -> bool:
        motions = processing.processing(self.Input, self.isImage)
        if not self.isImage:
            motions = postProcessing(motions, self.stabilization)
