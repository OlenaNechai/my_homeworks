# Interface, Abstraction

from abc import ABC, abstractmethod


class IMeaningful(ABC):

    @abstractmethod
    def _pick_the_book(self): ...

    @abstractmethod
    def _enjoying(self): ...
