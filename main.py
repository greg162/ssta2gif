import requests
from datetime import date, timedelta

d1 = date(2008, 8, 15)  # start date
d2 = date(2008, 9, 15)  # end date

delta = d2 - d1         # timedelta

for i in range(delta.days + 1):
  sampleDate = str(d1 + timedelta(i))
  