class Checksum:
    def __init__(self, web3) -> None:
        self.web3 = web3

    def __call__(self, address) -> str:
        return self.web3.toChecksumAddress(address)
