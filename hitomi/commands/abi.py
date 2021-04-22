import json


class Abi:
    def __init__(self):
        pass

    def fromFile(self, filename: str) -> object:
        with open(filename, "r") as f:
            abi_object = json.load(f)

        return abi_object
