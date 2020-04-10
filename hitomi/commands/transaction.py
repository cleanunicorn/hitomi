from web3.datastructures import AttributeDict

import rlp

from web3 import Web3

from eth_keys.datatypes import Signature
from eth_keys.backends.native import NativeECCBackend


class Transaction:
    def __init__(self, tx) -> None:
        self.tx = tx

    def raw(self):

        txParts = [
            # nonce
            int(format(self.tx["nonce"], "x"), 16),
            # gasPrice
            int(format(self.tx["gasPrice"], "x"), 16),
            # gasLimit
            int(format(self.tx["gas"], "x"), 16),
            # to
            int(self.tx["to"][2:], 16),
            # value
            int(format(self.tx["value"], "x"), 16),
            # data
            int(self.tx["input"][2:] if len(self.tx["input"][2:]) > 2 else "0", 16),
            # v
            int(format(self.tx["v"], "x"), 16),
            # r
            int(self.tx["r"].hex()[2:], 16),
            # s
            int(self.tx["s"].hex()[2:], 16),
        ]

        return rlp.encode(txParts)

    def signature(self):
        return Signature(
            vrs=[
                int(format(self.tx["v"], "x"), 16),
                int(self.tx["r"].hex()[2:], 16),
                int(self.tx["s"].hex()[2:], 16),
            ],
        )

    def publicKey(self):
        return "0x" + self.signature().recover_public_key_from_msg(
            message=bytes.fromhex(self.raw().hex())
        ).to_bytes().hex()

    def recoverAddress(self):
        return Web3.sha3(hexstr=self.publicKey()).hex()
