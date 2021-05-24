import argparse

from hitomi.version import __version__
from hitomi.network.web3 import Web3
from hitomi.console.__main__ import Console


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Connect to an Ethereum node.",
        epilog="Version {version}".format(version=__version__),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # What node to connect to
    parser.add_argument(
        "node",
        nargs="?",
        help="connect to this node (supports http, https, ws, ipc)",
        default="http://localhost:8545",
    )

    # Timeout for requests
    parser.add_argument(
        "-t",
        "--timeout",
        help="timeout for requests",
        type=float,
        default=10,
    )

    # Display info about the connected node
    parser.add_argument(
        "--noinfo",
        help="do not display information banner about the connected node",
        default=False,
        action="store_true",
    )

    args = parser.parse_args()

    # Init web3 object
    web3 = Web3()
    web3.connect(node=args.node, timeout=args.timeout)

    # Get info banner about the node
    info_banner = ""
    if args.noinfo is False:
        info_banner = get_info_banner(
            web3=web3, node_uri=args.node, version=__version__
        )

    # Start REPL console
    repl_shell = Console(vars=dict({"web3": web3}), web3=web3)
    repl_shell.interact(banner=info_banner)


def get_info_banner(web3: Web3, version: str, node_uri: str) -> str:
    nodeVersion: str = ""
    protocolVersion: int = 0
    chainId: int = 0
    blockNumber: int = 0
    hashrate: int = 0
    syncing: bool = False

    try:
        nodeVersion = web3.clientVersion
    except Exception:
        pass

    try:
        protocolVersion = web3.eth.protocolVersion
    except Exception:
        pass

    try:
        chainId = web3.eth.chainId
    except Exception:
        pass

    try:
        blockNumber = web3.eth.blockNumber
    except Exception:
        pass

    try:
        hashrate = web3.eth.hashrate
    except Exception:
        pass

    try:
        syncing = web3.eth.syncing
    except Exception:
        pass

    return """Starting Hitomi {version}.

Connected to {node_uri}.

Node version: {nodeVersion}
Enode path: {enode}
Protocol version: {protocolVersion}
Chain ID: {chainId}
Block number: {blockNumber}
Mining: {mining} ({hashrate} hash rate)
Syncing: {syncing}
""".format(
        version=version,
        node_uri=node_uri,
        nodeVersion=nodeVersion,
        enode=web3.enode,
        protocolVersion=protocolVersion,
        chainId=chainId,
        blockNumber=blockNumber,
        mining=hashrate > 0,
        hashrate=hashrate,
        syncing=syncing,
    )
