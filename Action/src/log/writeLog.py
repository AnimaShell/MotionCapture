import subprocess
import os
import time

editor = "C:/Windows/System32/notepad.exe"

log_info = set()


class Log:
    @staticmethod
    def write(msg_type: str, message: str):
        log_info.add(msg_type + "\n  " + message + "\n\n")

    @staticmethod
    def show():
        filename = "Log" + str(int(time.time())) + ".txt"
        if not os.path.isdir("../../log/"):
            os.makedirs("../../log/")
        with open("../../log/" + filename, "a") as f:
            for msg in log_info:
                f.write(msg)
        subprocess.run([editor, "../../log/" + filename])
        print(filename)

    @staticmethod
    def getLog():
        if len(log_info) > 0:
            return log_info
        else:
            return None


if __name__ == "__main__":
    try:
        i = []
        i.pop()
    except:
        Log.write("Error", "1")
    try:
        k = [1, 2, 3]
        i = k[3]
    except:
        Log.write("Error", "None")
    Log.show()
