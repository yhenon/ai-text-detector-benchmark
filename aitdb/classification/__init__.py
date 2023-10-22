from abc import ABC, abstractmethod


class TextClassifier(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def classify(self, text: str) -> float:
        raise NotImplementedError
