import json
import os


class ERC20:
    abi = None

    def __init__(self, web3) -> None:
        self.web3 = web3
        with open(
            "{dir}/{file}".format(dir=os.path.dirname(__file__), file="abi.json")
        ) as f:
            self.abi = json.load(f)
