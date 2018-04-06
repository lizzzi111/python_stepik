import datetime
inp = datetime.datetime.strptime(input(), "%Y %m %d")
inp += datetime.timedelta(days=int(input()))
print(f'{inp.year} {inp.month} {inp.day}')
