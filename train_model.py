import loader

class ModelCreator:
    def __init__(self):
        self.source_data = None
        self.loader = loader.Loader()
    def create_model(self):
        self.source_data = self.loader.load_source_data(
            path_to_file='spam.csv')
        print(self.source_data)

if __name__ == '__main__':
    model_creator = ModelCreator()
    model_creator.create_model()