import code
import atexit
import os
import readline
import rlcompleter
import pprint

from web3.datastructures import AttributeDict
from hitomi.commands.accounts import Accounts
from hitomi.network.web3 import Web3


class Console(code.InteractiveConsole):
    def __init__(self, vars: dict, web3: Web3):
        # Set history file
        history_path = os.path.join(os.environ["HOME"], ".hitomi_history")
        if os.path.isfile(history_path):
            readline.read_history_file(history_path)

        # Trigger history save on exit
        atexit.register(readline.write_history_file, history_path)

        # Setup autocomplete
        readline.set_completer(rlcompleter.Completer(vars).complete)
        readline.parse_and_bind("tab: complete")

        # Load commands
        local_commands = dict({"accounts": Accounts(web3)})
        vars.update(local_commands)

        super().__init__(vars)

    def push(self, line):
        return super().push(line)

    def runsource(self, source, filename="<input>", symbol="single"):
        try:
            code = self.compile(source, filename, "single")
        except (OverflowError, SyntaxError, ValueError):
            self.showsyntaxerror(filename)
            return False

        # Multiline code
        if code is None:
            return True

        try:
            self.compile(source, filename, "eval")
            code = self.compile(f"__ret_value__ = {source}", filename, "exec")
        except Exception:
            pass

        self.runcode(code)

        if "__ret_value__" in self.locals and self.locals["__ret_value__"] is not None:
            self._console_write(self.locals["__ret_value__"])
            del self.locals["__ret_value__"]

        return False

    def _console_write(self, obj):
        """
        Pretty print console output
        """
        text = pprint.pformat(obj, indent=4)
        try:
            if obj and isinstance(obj, AttributeDict):
                text = pprint.pformat(dict(obj), indent=4)
        except:
            pass

        print(text)
