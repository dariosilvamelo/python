try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e1:
    print(e1.__class__.__name__)
    print(e1)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as e2:
    print('TypeError + IndexError')
    print('MSG:', e2)
    print('Nome:', e2.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')