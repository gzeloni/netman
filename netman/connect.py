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
    print(f"Trying Telnet connection to {host}")
    try:
        client = telnetlib.Telnet(host, timeout=2)
        if password:
            client.write(username.encode('ascii') + b"\n")
            client.write(password.encode('ascii') + b"\n")
        return client
    
    except Exception as e:
        log.error(f"Telnet connection to {host} failed: {e}")
        return None


def ssh(host: str, username: str, password: str) -> paramiko.SSHClient:
    print(f"Trying SSH connection to {host}")
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.load_system_host_keys()
            client.connect(hostname=host, username=username, password=password, timeout=5, allow_agent=False)
            if client.get_transport().is_authenticated():
                return client
            else:
                return None
        except paramiko.AuthenticationException:
            try:
                client.connect(hostname=host, username=username, password=password, timeout=5)
                if client.get_transport().is_authenticated():
                    return client
                else:
                    return None
            except Exception as e:
                log.error(f"SSH connection to {host} failed: {e}")
                return None

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
            return connection

    log.error(f"Failed to connect to {host}")
