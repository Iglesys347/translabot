""""
This module handles the parsing of the arguements in a message.

It contains one class:
- MessageParser
"""

import re


class MessageParser:
    """
    Class representing the message parser.

    Attributes
    ----------
    msg : str
        The message to parse.

    Methods
    -------
    parse()
        Parse the message and returns the parsed message and arguments.
    parse_args()
        Parse the message and returns the arguments.
    parse_msg()
        Parse the message and returns the message.
    """

    def __init__(self, msg) -> None:
        """
        Class constructor.

        Parameters
        ----------
        msg : str
            The message to parse.
        """
        self._msg = msg

    def parse(self):
        """
        Parse the message and returns the parsed message and arguments.

        Returns
        -------
        msg : str
            The message parsed.
        arg_dict : dict
            A dictionnary containing the different arguments.
            The dictionnary looks as follows :
                {
                    "arg_key": "arg_value",
                    ...
                }
            The arg_key can take the values described in field "name" of the
            constant `ARGS_VALUES`.

        See Also
        --------
        ARGS_VALUES : list of possible arguments values and their abbreviations.
        """
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

    def parse_args(self):
        """
        Parse the message and returns the parsed arguments.

        Returns
        -------
        arg_dict : dict
            A dictionnary containing the different arguments.
            The dictionnary looks as follows :
                {
                    "arg_key": "arg_value",
                    ...
                }
            The arg_key can take the values described in field "name" of the
            constant `ARGS_VALUES`.

        See Also
        --------
        ARGS_VALUES : list of possible arguments values and their abbreviations.
        """
        _, args = self.parse()
        return args

    def parse_msg(self):
        """
        Parse the message and returns the parsed message and the arguments.

        Returns
        -------
        msg : str
            The message parsed.
        """
        msg, _ = self.parse()
        return msg


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
    message, arguments = mp.parse()
    print(f"Message : {message}")
    print(f"Args : {arguments}")
