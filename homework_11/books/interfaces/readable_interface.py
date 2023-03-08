# Interface, Abstraction

from abc import ABC, abstractmethod


class IReadable(ABC):

    @abstractmethod
    def _start_reading(self): ...

    @abstractmethod
    def _stop_reading(self): ...

    @abstractmethod
    def read(self): ...
