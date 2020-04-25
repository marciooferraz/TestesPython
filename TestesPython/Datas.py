import datetime

diaHoje = datetime.date.today()
print(diaHoje.strftime('%d %b %Y'))
print(diaHoje)

dataUser = input('Diga a porra da data, o merda!!! ')
outraData = datetime.datetime.strptime(dataUser, '%d/%m/%Y').date()

diasFaltantes = outraData - diaHoje

print(outraData.strftime('%d %b %Y'))
print(diasFaltantes.days)

# VER strftime.org
# VER babel.pocoo.org