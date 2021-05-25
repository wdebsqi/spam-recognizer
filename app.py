class Application:
    def __init__(self):
        self.source_data = []

    def get_user_input(self):
        self.source_data = []
        self.source_data.append(input('Put your text here: '))

    def print_menu(self):
        print(50 * '-')
        print('Welcome to spam recognizer! Type in any text and let the model decide whether its SPAM or HAM')
        print('To exit, just type exit()')
        print(50 * '-')
        
if __name__ == '__main__':
    app = Application()
    app.print_menu()
    while ('exit()' not in app.source_data):
        app.get_user_input()
    print('Bye!')