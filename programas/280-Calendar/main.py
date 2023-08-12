# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar
import locale

# coloca o sistema na ligua que o sistema operacional esta usando
locale.setlocale(locale.LC_ALL, ('pt_BR.utf8'))
# print(locale.getlocale())
# busca a idioma do sistema operacional -> pt_BR

# mostra o calendario do mes desejado
calendario_mes = (calendar.month(2022, 12))
# mostra o calendario do ano desejado
calendario_ano = (calendar.calendar(2022))
# mostra o primerio dia da semana no mês e o ultimo dia do mês
# segunda(0), terça(1), quarta(2),
# quinta(3), sexta(4), sabado(5), domingo(6)
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# lista dos dias sa semana (0=segunda ... 6=domingo)
list_dias_semana = list(enumerate(calendar.day_name))
# mostra o dia da semana do primeiro dia do mes
dia_semana_1_dia_mes = calendar.day_name[numero_primeiro_dia]
# mostra o dia da semana da data desejada
dia_semana_data = calendar.day_name[calendar.weekday(2023, 3, 13)]
# dias do mes agrupado por semana
semanas_mes = calendar.monthcalendar(2022, 12)

print(semanas_mes)
print(dia_semana_data)
print(dia_semana_1_dia_mes)
print(list_dias_semana)
print(numero_primeiro_dia, ultimo_dia)
print(calendario_mes)
print(calendario_ano)
