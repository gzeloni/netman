import argparse
import getpass
from netman.config import CONFIGURATIONS

def create_parser():
    parser = argparse.ArgumentParser(description="NetMan - Streamlining switch configurations.")

    for config in CONFIGURATIONS:
        name = config.pop("name")
        parser.add_argument(name, **config)

    args = parser.parse_args()

    args.password = getpass.getpass("Enter password: ") if args.password is None else args.password

    valid_connection_types = ['telnet', 'ssh']
    if args.connection and args.connection.lower() not in valid_connection_types:
        parser.error(f"Invalid connection type. Use {', '.join(valid_connection_types)}.")

    return args
