from Action.src.log.writeLog import Log


def pruningMethod(source: dict, cut: float):
    try:
        for bone in source.keys():
            for key in source[bone]["data"].keys():
                sbd = []
                for index in range(len(source[bone]["data"][key])):
                    if index > 0 and abs(source[bone]["data"][key][index-1] + source[bone]["data"][key][index+1] - 2 * source[bone]["data"][index]) < cut:
                        sbd.append(source[bone]["data"][key][index])
                source[bone]["data"][key] = sbd
    except TypeError:
        Log.write("Error", "pruning的参数有误，请确认其调用\n  ERROR at Action/src/postProcessing/pruning.py")
    finally:
        return source
