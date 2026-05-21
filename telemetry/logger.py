import time


class Logger:
    @staticmethod
    def log(message):
        print(f"[{time.strftime('%H:%M:%S')}] {message}")