# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta

# data = datetime(2021, 2, 26, 10, 23, 20)
# print(data.strftime('%d/%m/%Y-%H:%M:%S'))

# data = datetime.strptime('26/02/2021', '%d/%m/%Y')
# print(data.timestamp())

# data = datetime.fromtimestamp(1614308400.0)
# print(data)

# strptime(str, fmt)
# .strftime(fmt)
# timestamp
# fromtimestamp()

# data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# # print(data.strftime('%d/%m/%Y-%H:%M:%S'))
# data = data + timedelta(days=5, seconds=59)
# print(data.strftime('%d/%m/%Y-%H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1

print(dif)