import telnetlib
import paramiko
from netman.config import CONFIGURATIONS

def telnet(host, username, password):
    print(f"Trying Telnet connection to {host} with username {username} and password {password}")
    ...

def ssh(host, username, password):
    print(f"Trying SSH connection to {host} with username {username} and password {password}")
    ...
    
def connect(args):
    host = args.host
    username = args.username
    password = args.password
    
    telnet(host, username, password)
    ssh(host, username, password)