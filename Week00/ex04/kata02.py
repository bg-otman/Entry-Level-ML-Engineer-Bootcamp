import datetime

kata = (2019, 9, 25, 3, 30)

date = datetime.datetime.now()

print(date.replace(kata[0], kata[1], kata[2], kata[3], kata[4]).strftime('%m/%d/%Y %H:%M'))