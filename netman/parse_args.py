import argparse
import getpass
from netman.config import *

def parse_args():
    parser = argparse.ArgumentParser(description='NetMan - Streamlining switch configurations.')

    for config in CONFIGURATIONS:
        name = config.pop('name')
        parser.add_argument(name, **config)

    args = parser.parse_args()
    
    if args.connection.lower() not in CONNECTION_TYPES:
        parser.error(f'Invalid connection type. Use {", ".join(CONNECTION_TYPES)}.')
        
    if args.connection.lower() == 'snmp':
        args.gw = input("Get or Walk?: ").lower()
        args.community = input("Enter SNMP Community: ")
        args.oid = input("Enter SNMP OID or MIB: ")
    
    args.password = getpass.getpass('Enter password: ') if args.password is None else args.password
    

    return args
