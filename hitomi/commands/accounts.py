from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

from hitomi.network.web3 import Web3


class Accounts(list):
    def __init__(self, web3) -> None:
        self.web3 = web3
        self.refresh()

    def refresh(self):
        self._cache = dict({"accounts": self.web3.eth.accounts})

    def _accounts(self) -> list:
        return self._cache["accounts"]

    def __iter__(self) -> Iterator:
        return iter(self._accounts())

    def __getitem__(self, key: int) -> Any:
        accounts = self._accounts()
        return accounts[key]

    def __delitem__(self, key: int) -> None:
        accounts = self._accounts()
        del accounts[key]

    def __len__(self) -> int:
        return len(self._accounts())
