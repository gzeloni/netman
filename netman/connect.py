import telnetlib
import paramiko
import platform
import subprocess
import logging as log
from netman.config import CONFIGURATIONS


def icmp_ping(host: str) -> bool:
    try:
        flag = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        cmd = f"ping {flag} {host}"
        need_sh = platform.system().lower() != "windows"
        return subprocess.run(cmd, shell=need_sh, capture_output=True, check=True).returncode == 0
    except Exception as e:
        log.error(f"{host}: {e}")
        return False

def telnet(host: str, username: str, password: str) -> None:
    print(f"Trying Telnet connection to {host} with username {username} and password {password}")
    ...

def ssh(host: str, username: str, password: str):
    print(f"Trying SSH connection to {host} with username {username} and password {password}")
    ...
    
def connect(args) -> None:
    host, username, password = args.host, args.username, args.password
    if icmp_ping(host):
        try:
            telnet(host, username, password)
            ssh(host, username, password)
        except Exception as e:
            log.error(f"{host}: {e}")