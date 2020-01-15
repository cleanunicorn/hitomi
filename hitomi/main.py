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

    parser.add_argument(
        "node",
        nargs="?",
        help="connect to this node (supports http, https, ws, ipc)",
        default="http://localhost:8545",
    )

    args = parser.parse_args()

    # Init web3 object
    web3 = init_web3(node=args.node)

    start_repl(node=args.node, local_vars=locals())


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


def start_repl(node: str, local_vars: dict):
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
        banner="""Connected to {node}.

Hitomi {version}.

""".format(
            version=__version__, node=node
        )
    )
