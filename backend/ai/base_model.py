from abc import ABC, abstractmethod

class BaseAIModel(ABC):
    @abstractmethod
    def predict(self, file):
        pass