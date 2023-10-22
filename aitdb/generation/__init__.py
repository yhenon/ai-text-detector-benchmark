from abc import ABC, abstractmethod


class TextGenerator(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
