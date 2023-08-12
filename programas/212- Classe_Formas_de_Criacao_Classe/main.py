# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        c = cls()
        c.user = user
        c.password = password
        return c

    @staticmethod
    def log(msg):
        print('LOG:', msg)

print('Exemplo 01: ')
c1 = Connection()
print(c1.host)
print(c1.user)
print(c1.password)

c1.set_user('Dário')
c1.set_password('1234')
print('')
print(c1.host)
print(c1.user)
print(c1.password)
c1.set_user('Dário')
print('')

print('Exemplo 02: ')
c2 = Connection.create_with_auth('Dário', '1234')
print(c2.host)
print(c2.user)
print(c2.password)






