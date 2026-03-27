from abc import ABC, abstractmethod

# from collections.abc import Callable


class IMessageBroker(ABC):
    @abstractmethod
    def publish(self, topic: str, message: dict) -> None:
        pass

    # @abstractmethod
    # def subscribe(self, topic: str, callback: Callable[[dict], None]) -> None:
    #     pass
