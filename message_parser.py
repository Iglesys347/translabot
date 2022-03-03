import re


class MessageParser:
    def __init__(self, msg) -> None:
        self._msg = msg

    def parse(self):
        msg_list = self._msg.split()
        arg_dict = {}
        to_remove = []
        for elt in msg_list:
            if elt.startswith(("-", "--")):
                arg = re.search(r"-{1,2}(.+)=", elt).group(1)
                for args_vals in ARGS_VALUES:
                    if arg in args_vals["abbreviations"]:
                        arg_dict[args_vals["name"]] = elt.split("=")[1]
                        to_remove.append(elt)
        for elt in to_remove:
            msg_list.remove(elt)
        return " ".join(msg_list), arg_dict


ARGS_VALUES = [
    {
        "name": "target",
        "abbreviations": ["t", "target", "tgt"]
    },
    {
        "name": "source",
        "abbreviations": ["s", "source", "src"]
    }
]

if __name__ == "__main__":
    mp = MessageParser("Test message -t=test --source=foo")
    message, args = mp.parse()
    print(f"Message : {message}")
    print(f"Args : {args}")
