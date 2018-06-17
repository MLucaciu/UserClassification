from sklearn.neural_network import MLPClassifier
from FileReader import FileReader


class StereotypeMLP:
    classes = []
    attributes = []
    classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)

    def __init__(self):
        reader = FileReader
        self.classes = reader.readClasses('classes.txt')
        self.attributes = reader.readAttributes('dataset.txt')
        self.classifier.fit(self.attributes, self.classes)

