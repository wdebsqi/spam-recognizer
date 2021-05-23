import requests
import pandas as pd

from kaggle_loader import KaggleLoader

class Loader:
    def load_source_data(self, path_to_file):
        try:
            source_data = self._load_from_csv(path_to_file)
        except FileNotFoundError:
            print('File not found on local machine.')
            print(f'Loading from remote url.')
            self._save_data_from_remote_to_local_machine(path_to_file)
        
        return source_data
        
    
    def _load_from_csv(self, path_to_file):
        return pd.read_csv(
            'spam.csv',
            names=['label', 'message'],
            index_col=False,
            header=0,
            encoding="ISO-8859-1")
    
    def _save_data_from_remote_to_local_machine(self, path_to_file):
        kaggle_loader = KaggleLoader()