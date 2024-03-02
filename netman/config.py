CONFIGURATIONS = [
    {"name": "-sh", "dest": "host", "type": str, "required": True, "help": "Switch IP address or hostname"},
    {"name": "-u", "dest": "username", "type": str, "required": True, "help": "Username for authentication"},
    {"name": "-p", "dest": "password", "type": str, "nargs": "?", "const": None, "help": "Password for authentication"},
    {"name": "-c", "dest": "connection", "choices": ['telnet', 'ssh'], "help": "Specify the type of connection (telnet or ssh)"}
]
