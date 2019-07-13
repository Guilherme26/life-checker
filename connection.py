import poplib
from credentials import credentials


class Connection():
    def __init__(self):
        self.connection = self.get_connection()
    
    def get_connection(self):
        connection = poplib.POP3_SSL('pop.gmail.com')
        connection.user(credentials['username'])
        connection.pass_(credentials['password'])

        return connection
    
    def close_connection(self):
        self.connection.quit()
