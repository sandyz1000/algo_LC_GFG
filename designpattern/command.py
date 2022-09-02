"""
Command pattern:
When you wanted to execute macro operation i.e execute a set of command or maintain a history of command this pattern
help you to achieve this.
Advantages:
1. It can be used if you wanted to maintain history of command
2. When the creating of request and executing are not dependent on each other.
3. This pattern help in term of extensibility you can add new command without modifying the existing code.
"""
from abc import ABCMeta, abstractmethod
import os


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TouchCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.create_file()

    def undo(self):
        self.receiver.remove_file()


class LSCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.show_files()

    def undo(self):
        pass


class RmCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.delete_file()

    def undo(self):
        self.receiver.undo()


class TouchReceiver(object):
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        """Actual implementation of unix touch command."""
        with open(self.filename, 'a'):
            os.utime(self.filename, None)

    def remove_file(self):
        """Undo unix touch command. Here we simply delete the file."""
        if os.path.isfile(self.filename):
            os.remove(self.filename)


class LsReceiver(object):
    def show_files(self):
        current_dir = "/"
        files = [filename for filename in os.listdir(current_dir) if
                 os.path.isfile(os.path.join(current_dir, filename))]
        return "".join(files)


class RmReceiver(object):
    def __init__(self, filename):
        self.filename = filename
        self.backup_name = None

    def delete_file(self):
        """To introduce the undo rename the current filename with ."""
        self.backup_name = "." + self.filename
        os.rename(self.filename, self.backup_name)

    def undo(self):
        if self.backup_name:
            os.rename(self.backup_name, self.filename)
        self.backup_name = None


class Invoker(object):
    def __init__(self, create_file_commands, delete_file_commands):
        self.history = []
        self.create_file_commands = create_file_commands
        self.delete_file_commands = delete_file_commands

    def create_file(self):
        for command in self.create_file_commands:
            command.execute()
            self.history.append(command)

    def delete_file(self):
        for command in self.delete_file_commands:
            command.execute()
            self.history.append(command)

    def undo_all(self):
        print('Undo all...')
        for command in reversed(self.history):
            command.undo()
        print('Undo all finished.')


if __name__ == '__main__':
    filename = "temp_file.txt"
    touch_command = TouchCommand(TouchReceiver(filename))
    rm_command = RmCommand(RmReceiver(filename))
    ls_command = LSCommand(LsReceiver())

    invoker = Invoker([ls_command, touch_command, ls_command], [ls_command, rm_command, ls_command])
    invoker.create_file()
    invoker.delete_file()
    invoker.undo_all()
