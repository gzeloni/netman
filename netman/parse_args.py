import argparse
import getpass
from netman.config import CONFIGURATIONS

def parser():
    parser = argparse.ArgumentParser(description="NetMan - Streamlining switch configurations.")

    for config in CONFIGURATIONS:
        name = config["name"]
        config.pop("name")

        parser.add_argument(name, **config)

    args = parser.parse_args()

    if args.password is None:
        args.password = getpass.getpass("Enter password: ")
        
    if args.connection and args.connection.lower() not in ['telnet', 'ssh']:
        parser.error("Invalid connection type. Use 'telnet' or 'ssh'.")

    return args
