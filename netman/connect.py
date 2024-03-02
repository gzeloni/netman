import telnetlib
import paramiko
import platform
import subprocess
import logging as log
from netman.config import CONFIGURATIONS

def ping(host: str) -> bool:
    try:
        flag = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        cmd = f"ping {flag} {host}"
        need_sh = platform.system().lower() != "windows"
        return subprocess.run(cmd, shell=need_sh, capture_output=True, check=True).returncode == 0
    except Exception as e:
        log.error(f"{host}: {e}")
        return False

def telnet(host: str, username: str, password: str) -> telnetlib.Telnet:
    print(f"Trying Telnet connection to {host} with username {username} and password {password}")
    try:
        client = telnetlib.Telnet(host)
        client.write(username.encode('ascii') + b"\n")
        if password:
            client.write(password.encode('ascii') + b"\n")
        return client
    except Exception as e:
        log.error(f"Telnet connection to {host} failed: {e}")
        return None

def ssh(host: str, username: str, password: str) -> paramiko.SSHClient:
    print(f"Trying SSH connection to {host} with username {username} and password {password}")
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password, timeout=5)
        return client
    except Exception as e:
        log.error(f"SSH connection to {host} failed: {e}")
        return None
    
def connect(args) -> None:
    host, username, password = args.host, args.username, args.password
    if not ping(host):
        log.error(f"Failed to connect to {host}")
        return
    
    connect_functions = [telnet, ssh]
    for connect_func in connect_functions:
        connection = connect_func(host, username, password)
        if connection:
            print(f"{connect_func.__name__.capitalize()} connection successful")
            return

    log.error(f"Failed to connect to {host}")
