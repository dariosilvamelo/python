# Abstração
# Herança - é um
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    
    l = LogPrintMixin()
    l._log('Mensagem')
    l.log_error('qualquer coisa')
    l.log_success('Que legal')

    l2 = LogFileMixin()
    l2._log('L2: mensagem')
    l2.log_error('L2: qualquer coisa')
    l2.log_success('L2: Que legal')