from typing import Union
import telnetlib
import paramiko
import platform
import subprocess
from netman.config import CONFIGURATIONS
from netman.modules.snmp import Snmp

def ping(host: str) -> bool:
    try:
        flag = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        cmd = f"ping {flag} {host}"
        need_sh = platform.system().lower() != "windows"
        return subprocess.run(cmd, shell=need_sh, capture_output=True, check=True).returncode == 0
    except subprocess.CalledProcessError:
        return False

def telnet(host: str, username: str, password: str) -> Union[telnetlib.Telnet, None]:
    try:
        client = telnetlib.Telnet(host, timeout=2)
        if password:
            client.write(f"{username}\n{password}\n".encode('ascii'))
        return client
    except Exception:
        return None

def ssh(host: str, username: str, password: str) -> Union[paramiko.SSHClient, None]:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.load_system_host_keys()
            client.connect(hostname=host, username=username, timeout=5, allow_agent=False)
        except paramiko.AuthenticationException:
            try:
                client.connect(hostname=host, username=username, password=password, timeout=5)
            except Exception:
                return None

        return client if client.get_transport().is_authenticated() else None
    except Exception:
        return None

def snmp(host: str, community: str, oid: str) -> Union[paramiko.SSHClient, None]:
    try:
        client = Snmp(addr=host, community=community)

def connect(args) -> Union[telnetlib.Telnet, paramiko.SSHClient, None]:
    host, username, password = args.host, args.username, args.password

    if not ping(host):
        raise Exception("Host unreachable.")

    connection_type = args.connection.lower() if args.connection else None
    connect_functions = [telnet, ssh]

    if connection_type:
        connect_functions = [func for func in connect_functions if func.__name__.lower() == connection_type]

    for connect_func in connect_functions:
        connection = connect_func(host, username, password)
        if connection:
            print(f"\n{connect_func.__name__.capitalize()} connection successful")
            return connection
        else:
            print("....", end="", flush=True)

    print(f"Failed to connect to {host}")
    return None
