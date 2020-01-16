import os, atexit, readline, rlcompleter, code
import argparse

from hitomi.version import __version__
from hitomi.network.web3 import Web3


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Connect to an Ethereum node.",
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
        "-t", "--timeout", help="timeout for requests", type=float, default=10,
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
        info_banner = get_info_banner(web3)

    start_repl(node=args.node, info_banner=info_banner, local_vars=locals())


def start_repl(node: str, local_vars: dict, info_banner: str = ""):
    # Load history
    history_path = os.path.join(os.environ["HOME"], ".hitomi_history")
    if os.path.isfile(history_path):
        readline.read_history_file(history_path)

    # Trigger history save on exit
    atexit.register(readline.write_history_file, history_path)

    # Load variables
    vars = globals()
    vars.update(locals())
    vars.update(local_vars)

    # Start REPL
    readline.set_completer(rlcompleter.Completer(vars).complete)
    readline.parse_and_bind("tab: complete")
    code.InteractiveConsole(vars).interact(
        banner="""Hitomi {version}.

Connected to {node}.
{info_banner}""".format(
            version=__version__, node=node, info_banner=info_banner,
        )
    )


def init_web3(node: str, timeout: int = 10) -> Web3:
    w3 = Web3()
    w3.connect(node=node, timeout=timeout)

    return w3


def get_info_banner(web3: Web3) -> str:
    chainId = None
    blockNumber = None
    mining = None
    hashrate = None
    syncing = None

    try:
        chainId = web3.eth.chainId
    except Exception:
        pass

    blockNumber = web3.eth.blockNumber
    hashrate = web3.eth.hashrate
    syncing = web3.eth.syncing

    return """Chain ID: {chainId}
Block number: {blockNumber}
Mining: {mining} ({hashrate} hash rate)
Syncing: {syncing}
""".format(
        chainId=chainId,
        blockNumber=blockNumber,
        mining=hashrate > 0,
        hashrate=hashrate,
        syncing=syncing,
    )
