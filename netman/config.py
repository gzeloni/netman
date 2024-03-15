CONNECTION_TYPES = ['ssh', 'telnet', 'snmp']

CONFIGURATIONS = [
    {"name": "-sh", "dest": "host", "type": str, "required": True, "help": "Switch IP address or hostname"},
    {"name": "-u", "dest": "username", "type": str, "required": True, "help": "Username for authentication"},
    {"name": "-p", "dest": "password", "type": str, "nargs": "?", "const": None, "help": "Password for authentication"},
    {"name": "-t", "dest": "connection", "choices": CONNECTION_TYPES, "help": "Specify the type of connection (ssh, telnet or snmp)"},
    {"name": "--option", "dest": "gw", "type": str, "required": False, "help": "SNMP Get or Walk"},
    {"name": "--community", "dest": "community", "type": str, "required": False, "help": "SNMP Community"},
    {"name": "--oid", "dest": "oid", "type": str, "required": False, "help": "SNMP MiB or OID"},
]