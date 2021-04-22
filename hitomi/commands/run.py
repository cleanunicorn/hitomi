import sys


class Run:
    def __init__(self):
        pass

    def __call__(self, filename: str):
        try:
            exec(open(filename).read())
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
