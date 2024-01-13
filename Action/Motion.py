from src.processing.processing import process
from src.postProcessing.postProcessing import postProcessing
from datetime import datetime
from src.save.saveFile import save
from src.log.writeLog import Log
from src.postProcessing.bottling import bottling


class ActionConte:
    def __int__(self, Input: str, isImage: bool, Output: str = None, model: str = None, stabilization: int = 1, pruning: float = 0, output_name: str = None):
        self.Input = Input
        self.Output = Output
        self.isImage = isImage
        self.model = model
        self.filename = output_name
        self.stabilization = stabilization
        self.pruning = pruning

    # 开始计算
    def doCapture(self):
        try:
            # 对输入数据进行处理
            motions = process(self.Input, self.isImage, self.model)
            # 将模型生成的数据分装为规定格式的字典
            motions = bottling(motions, self.model)
        except:
            Log.write("Error", "模型错误")
        else:
            # 数据分装成功，源数据已生成
            if motions is not None:
                if not self.isImage:
                    # 对数据进行后处理操作（平滑， 剪枝）
                    motions = postProcessing(motions, self.stabilization)
                # 将数据写入文件
                outputDir = save(motions, self.Input, self.Output, self.filename)
                if outputDir is not None:
                    Log.write("Success", "写入成功\n  时间:" + str(datetime.now()) + "\n  文件路径:" + outputDir + "\n\n")
            else:
                Log.write("Error", "分装失败，数据未生成")
        finally:
            return Log.getLog()
