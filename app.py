import preprocessor as pp
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer

class Application:
    def __init__(self):
        self.source_data = []
        self.import_model_vocabulary()
        self.preprocessor = pp.Preprocessor()
        self.vectorizer = CountVectorizer(vocabulary=self.vocabulary)

    def import_model_vocabulary(self):
        with open('model.pickle', 'rb') as file:
            self.model = pickle.load(file)
            
        with open('vocabulary.pickle', 'rb') as file:
            self.vocabulary = pickle.load(file)

    def get_user_input(self):
        self.source_data = []
        self.source_data.append(input('Put your text here: '))

    def print_menu(self):
        print(50 * '-')
        print('Welcome to spam recognizer! Type in any text and let the model decide whether its SPAM or HAM')
        print('To exit, just type exit()')
        print(50 * '-')
    
    def normalize_user_input(self):
        self.user_input_df = pd.DataFrame(self.source_data, columns=['message'])
        self.preprocessed_data = self.preprocessor.clean_column_containing_text(self.user_input_df, 'message')
        self.vectorized = self.vectorizer.transform(self.preprocessed_data['message'])

    def rate_user_input(self):
        self.rating = self.model.predict(self.vectorized)
        return self.rating 

if __name__ == '__main__':
    app = Application()
    app.print_menu()
    while (True):
        app.get_user_input()
        if ('exit()' in app.source_data): 
            break
        app.normalize_user_input()
        result = app.rate_user_input()

        if (result == 0):
            print('---HAM---')
        else:
            print('---SPAM---')
        print()
    print('Bye!')