import preprocessor as pp
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer

class Application:
    def __init__(self):
        self.import_model()
        self.import_vocabulary()
        self.preprocessor = pp.Preprocessor()
        self.vectorizer = CountVectorizer(vocabulary=self.vocabulary)

    def import_model(self):
        with open('model.pickle', 'rb') as file:
            self.model = pickle.load(file)

    def import_vocabulary(self):
        with open('vocabulary.pickle', 'rb') as file:
            self.vocabulary = pickle.load(file)

    def get_user_input(self):
        self.user_inputs = []
        user_input = input('Put your text here: ')
        self.user_inputs.append(user_input)

    def print_menu(self):
        print(50 * '-')
        print('Welcome to spam recognizer! Type in any text and let the model decide whether its SPAM or HAM')
        print('To exit, just type exit()')
        print(50 * '-')
    
    def normalize_user_input(self):
        self.user_input_df = pd.DataFrame(self.user_inputs, columns=['message'])
        self.preprocessed_data = self.preprocessor.clean_column_containing_text(self.user_input_df, 'message')
        self.vectorized_inputs = self.vectorizer.transform(self.preprocessed_data['message'])

    def rate_user_input(self):
        self.rating = self.model.predict(self.vectorized_inputs)
        return self.rating 

if __name__ == '__main__':
    app = Application()
    app.print_menu()
    while (True):
        app.get_user_input()
        if ('exit()' in app.user_inputs): 
            break
        app.normalize_user_input()
        result = app.rate_user_input()

        if (result == 0):
            print('---HAM---')
        else:
            print('---SPAM---')
        print()
    print('Bye!')