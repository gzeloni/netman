from paramiko import SSHClient
from telnetlib import Telnet

class CommandExec:
    def __init__(self, connection):
        self.connection = connection
        self.command_methods = {
            Telnet: self._exec_telnet_command,
            SSHClient: self._exec_ssh_command
        }

        if type(connection) not in self.command_methods:
            raise ValueError("Unsupported connection type")

    def _exec_telnet_command(self, command):
        self.connection.write(f"{command}\n".encode('ascii'))
        output = self.connection.read_until(b">").decode('ascii')
        return output

    def _exec_ssh_command(self, command):
        stdin, stdout, stderr = self.connection.exec_command(command)
        output = stdout.read().decode('utf-8')
        return output

    def exec_command(self, command):
        return self.command_methods[type(self.connection)](command)
