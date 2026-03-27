from abc import ABC, abstractmethod

# Command Base Class
from src.context.shared_kernel.application.command.commands import ICommand


class ICommandHandler(ABC):
    @abstractmethod
    def handle(self, command: ICommand):
        pass
