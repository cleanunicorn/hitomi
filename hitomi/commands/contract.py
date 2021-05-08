from web3.contract import Contract


class ContractInit:
    def __init__(self, web3) -> None:
        self.web3 = web3

    def __call__(self, address: str, *args, **kwargs) -> Contract:
        return self.web3.eth.contract(
            address=self.web3.toChecksumAddress(address),
            *args,
            **kwargs,
        )

    def calculateAddress(self, address: str, nonce: int = None) -> str:
        """
        Calculates the next address a contract will have based on the
        account deploying it and its nonce
        """
        address = self.web3.toChecksumAddress(address)

        if nonce is None:
            nonce = self.web3.eth.getTransactionCount(address)

        return self.web3.keccak(rlp.encode([bytes.fromhex(address[2:]), nonce]))[
            12:
        ].hex()
