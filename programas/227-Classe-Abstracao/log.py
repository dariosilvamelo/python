from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt' # CAMINHO DA PASTA DO EXECUTAVEL


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a',encoding='utf8') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    
    LogPrint = LogPrintMixin()
    LogPrint.log_error('qualquer coisa')
    LogPrint.log_success('Que legal')

    LogFile = LogFileMixin()
    LogFile.log_error('Qualquer coisa')
    LogFile.log_success('Que legal')