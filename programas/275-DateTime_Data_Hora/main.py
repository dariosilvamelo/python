# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

d0 = datetime(2022, 4, 20, 7, 49, 23)
print(d0)
print('========================================')
d1 = '2022-04-20 07:49:23'
d1f = '%Y-%m-%d %H:%M:%S'
data1 = datetime.strptime(d1, d1f)
print(data1)
print('========================================')
d2 = '2022/04/20 07:49:23'
d2f = '%Y/%m/%d %H:%M:%S'
data2 = datetime.strptime(d2, d2f)
print(data2)
print('========================================')
d3 = '20/04/2022'
d3f = '%d/%m/%Y'
data3 = datetime.strptime(d3, d3f)
print(data3)
print('========================================')
d4 = datetime.now()
print(d4)
print('========================================')
d5 = datetime.now(timezone('America/Sao_Paulo'))
print(d5)
print('========================================')
d5 = datetime.now(timezone('Asia/Tokyo'))
print(d5)  # Olhar documentação para saber a hora em outro pais
print('========================================')
d5 = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
print(d5)  # formatar datetime -> timezone
print('========================================')
d6 = datetime.now()
d6_milisegundos = d6.timestamp()
print(d6_milisegundos)
print(datetime.fromtimestamp(d6_milisegundos))
print('========================================')
# usado para converte str em data no formato desejado
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
# apos a conversão a função strftime formata para o padrao que quisermos
# e também faz a separacao de ano, mes e dia caso necessario
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print('')
print(data.strftime('%Y'))
print(data.strftime('%d'))
print(data.strftime('%m'))
print(data.strftime('%H') + ' <- a hora esta no formato 00')
print(data.strftime('%M'))
print(data.strftime('%S'))
print('')
print('Retorna as datas como Inteiro')
print('')
print(data.year)
print(data.day)
print(data.month)
print(str(data.hour) + ' <- a hora esta como inteiro só tem um alcarismo')
print(data.minute)
print(data.second)
print('========================================')
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('01/12/2022 08:20:20', fmt)
print(data_fim > data_inicio)
print(data_fim < data_inicio)
print(data_fim == data_inicio)
# Essa variavel chamos de time delta
delta = data_fim - data_inicio
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
# adicionar 10 dias e 2 horas ums data
delta = timedelta(days=10)
print('Minha '+str(data_fim)+' + 10 dias: ' + str(data_fim+delta))
delta = timedelta(days=10, hours=2)
print('Minha '+str(data_fim)+' + 10 dias + 2 horas: ' + str(data_fim+delta))
delta = timedelta(days=2)
print('Minha '+str(data_fim)+' - 2 dias: ' + str(data_fim-delta))
print('========================================')
print('Pacote: dateutil.relativedelta')
print('')
print(data_fim + relativedelta(seconds=60, minutes=10))
d = relativedelta(data_fim, data_inicio)
print(d.days, d.years)
