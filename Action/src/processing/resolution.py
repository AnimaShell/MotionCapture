import cv2

MAX_LENGTH = 480
MAX_WIDTH = 360


def adapt(source):
    if source is not None:
        scale = min(MAX_LENGTH / source.shape[0], MAX_WIDTH / source.shape[1])
        source = cv2.resize(source, (0, 0), fx=scale, fy=scale)
        border_width_l, border_width_w = int((MAX_LENGTH - source.shape[0]) / 2), int((MAX_WIDTH - source.shape[1]) / 2)
        source = cv2.copyMakeBorder(src=source,
                                    top=border_width_w,
                                    bottom=border_width_w,
                                    left=border_width_l,
                                    right=border_width_l,
                                    borderType=cv2.BORDER_CONSTANT,
                                    value=0)
    return source

