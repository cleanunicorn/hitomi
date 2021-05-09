import os

from web3 import Web3 as _web3
from web3 import IPCProvider, HTTPProvider, WebsocketProvider
from web3.middleware import geth_poa_middleware


class Web3(_web3):
    """
    Web3 wrapper class
    """

    enode = None

    def __init__(self) -> None:
        super().__init__(HTTPProvider("null"))

    def handleEnode(self) -> None:
        """
        Obtain enode path
        """
        connected = self.isConnected()

        if connected:
            if self.clientVersion.startswith("Parity"):
                self.enode = self.parity.enode()
            elif self.clientVersion.startswith("Geth"):
                self.enode = self.geth.admin.nodeInfo()["enode"]
            elif self.clientVersion.startswith("bor"):
                self.enode = self.geth.admin.nodeInfo()["enode"]

    def handleProofOfAuthorityChain(self) -> None:
        """
        Add PoA middleware because
        https://web3py.readthedocs.io/en/stable/middleware.html#why-is-geth-poa-middleware-necessary
        """
        connected = self.isConnected()

        if connected:
            if self.clientVersion.startswith("bor"):
                self.middleware_onion.inject(geth_poa_middleware, layer=0)

    def connect(self, node: str, timeout: int = 10) -> None:
        try:
            if os.path.exists(node):
                self.provider = IPCProvider(node)
                return
        except OSError:
            pass

        if node.startswith("https://") or node.startswith("http://"):
            self.provider = HTTPProvider(node, request_kwargs={"timeout": timeout})
        elif node.startswith("ws://") or node.startswith("wss://"):
            self.provider = WebsocketProvider(
                node, websocket_kwargs={"timeout": timeout}
            )
        else:
            raise ValueError(
                "The provided node is not valid. It must start with 'http://' or 'https://' or 'ws://' or a path to an IPC socket file."
            )

        try:
            self.handleEnode()
        except Exception:
            pass

        try:
            self.handleProofOfAuthorityChain()
        except Exception:
            pass
