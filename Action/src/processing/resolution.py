import cv2


def adapt(source, size: list):
    if source is not None:
        MAX_LENGTH, MAX_WIDTH, CHANNELS = size[0], size[1], size[2]
        if CHANNELS == 1:
            # 转为灰度图
            source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
        # 进行图像缩放
        scale = min(MAX_LENGTH / source.shape[0], MAX_WIDTH / source.shape[1])
        source = cv2.resize(source, (0, 0), fx=scale, fy=scale)
        # 图像边缘填充
        border_width_l = int((MAX_LENGTH - source.shape[0]) / 2) + (0 if int((MAX_LENGTH - source.shape[0]) / 2) % 2 == 0 else 1)
        border_width_r = int((MAX_LENGTH - source.shape[0]) / 2)
        border_width_t = int((MAX_WIDTH - source.shape[1]) / 2) + (0 if int((MAX_WIDTH - source.shape[1]) / 2) % 2 == 0 else 1)
        border_width_b = int((MAX_WIDTH - source.shape[1]) / 2)
        source = cv2.copyMakeBorder(src=source,
                                    top=border_width_t,
                                    bottom=border_width_b,
                                    left=border_width_l,
                                    right=border_width_r,
                                    borderType=cv2.BORDER_CONSTANT,
                                    value=0)
    return source

