from paramiko import SSHClient
from telnetlib import Telnet

class CommandExec:
    def __init__(self, connection):
        self.connection = connection
        self.command_methods = {
            Telnet: self._execute_telnet_command,
            SSHClient: self._execute_ssh_command
        }

        if type(connection) not in self.command_methods:
            raise ValueError("Unsupported connection type")

    def _execute_telnet_command(self, command):
        self.connection.write(command.encode('ascii') + b"\n")
        output = self.connection.read_until(b">")
        return output.decode('ascii')

    def _execute_ssh_command(self, command):
        stdin, stdout, stderr = self.connection.exec_command(command)
        output = stdout.read()
        return output.decode('utf-8')

    def exec_command(self, command):
        return self.command_methods[type(self.connection)](command)