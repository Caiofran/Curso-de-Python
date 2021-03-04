from datetime import datetime
from locale import setlocale,LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m')) # ultimo dia do mês
formartacao1 = dt.strftime('%A, %d de %B de %Y')
formartacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formartacao1)
print(formartacao2)

print(mes_atual, mdays[mes_atual])