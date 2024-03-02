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

    return args
