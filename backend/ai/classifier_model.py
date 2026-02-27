from backend.ai.base_model import BaseAIModel

class SimpleClassifier(BaseAIModel):
    def predict(self, file):
        return {
            "prediction" : "Normal",
            "confidence" : 0.85
        }