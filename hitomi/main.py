import os, atexit, readline, rlcompleter, code
import argparse

from web3 import Web3

from hitomi.version import __version__


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

    # Display info about the connected node
    parser.add_argument(
        "--noinfo",
        help="do not display information banner about the connected node",
        default=False,
        action="store_true",
    )

    args = parser.parse_args()

    # Init web3 object
    web3 = init_web3(node=args.node)

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
    w3 = None

    if os.path.exists(node):
        w3 = Web3(Web3.IPCProvider(ipc_path=node, timeout=timeout))
    elif node.startswith("https://"):
        w3 = Web3(Web3.HTTPProvider(node, request_kwargs={"timeout": 60}))
    elif node.startswith("http://"):
        w3 = Web3(Web3.HTTPProvider(node, request_kwargs={"timeout": 60}))
    elif node.startswith("ws://"):
        w3 = Web3(Web3.WebsocketProvider(node, websocket_kwargs={"timeout": 60}))

    return w3


def get_info_banner(web3: Web3) -> str:
    return """Chain ID: {chainId}
Block number: {blockNumber}
Mining: {mining} ({hashrate} hash rate)
Syncing: {syncing}
""".format(
        chainId=web3.eth.chainId,
        blockNumber=web3.eth.blockNumber,
        mining=web3.eth.hashrate > 0,
        hashrate=web3.eth.hashrate,
        syncing=web3.eth.syncing,
    )
