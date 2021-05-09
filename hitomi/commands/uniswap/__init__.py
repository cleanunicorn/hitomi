import os
import json


class UniswapPair:
    abi = None

    def __init__(self, web3) -> None:
        self.web3 = web3

        # Load ABI
        with open(
            "{dir}/{file}".format(dir=os.path.dirname(__file__), file="pair_abi.json")
        ) as f:
            self.abi = json.load(f)
