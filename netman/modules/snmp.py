import subprocess as sub
import shutil as sh


class Snmp:
    def __init__(self, addr: str, community: str) -> None:
        self.addr = addr
        self.community = community
    
    def _construct_command(self, operation: str, oid: str = None, mib: str = None) -> str:
        if oid is not None:
            return f'snmp{operation} -v 2c -c "{self.community}" {self.addr} {oid}'
        elif mib is not None:
            return f'snmp{operation} -v 2c -c "{self.community}" {self.addr} {mib}'

    def get(self, oid: str = None, mib: str = None) -> list:
        command = self._construct_command("get", oid, mib)
        result = sub.run(command, capture_output=True, text=True, shell=True, executable=sh.which("snmpget")).stdout
        return result.split('\n')

    def walk(self, oid: str = None, mib: str = None) -> list:
        command = self._construct_command("walk", oid, mib)
        result = sub.run(command, capture_output=True, text=True, shell=True, executable=sh.which("snmpwalk")).stdout
        return result.split('\n')
