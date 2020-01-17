import code
import atexit
import os
import readline
import rlcompleter

class Console(code.InteractiveConsole):
    def __init__(self, vars: dict):
        # Set history file
        history_path = os.path.join(os.environ["HOME"], ".hitomi_history")
        if os.path.isfile(history_path):
            readline.read_history_file(history_path)

        # Trigger history save on exit
        atexit.register(readline.write_history_file, history_path)

        # Setup autocomplete
        readline.set_completer(rlcompleter.Completer(vars).complete)
        readline.parse_and_bind("tab: complete")

        super().__init__(vars)

    def push(self, line):
        return super().push(line)

    def _console_write(self, obj):
        text = repr(obj)
        try:
            if obj and isinstance(obj, dict):
                text = color.pretty_dict(obj)
            elif obj and isinstance(obj, (tuple, list, set)):
                text = color.pretty_sequence(obj)
        except (SyntaxError, NameError):
            pass
        print(text)


    