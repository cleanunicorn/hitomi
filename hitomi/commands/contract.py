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
