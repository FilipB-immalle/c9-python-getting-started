from datetime import datetime, timedelta
# print today's date
print(datetime.now())

# print yesterday's date
een_dag = timedelta(days=1)
print('Gisteren was het: ' + str(datetime.now() - een_dag))

# ask a user to enter a date
datum = input('Vul een datum in (dd/mm/yyyy). ')
datum = datetime.strptime(datum, '%d/%m/%Y')

# print the date one week from the date entered
weeklater = datum + timedelta(weeks=1)
print(str(weeklater))
