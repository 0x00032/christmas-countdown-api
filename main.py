from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

def dateDiffInSeconds(date1, date2):
  timeDelta = date2 - date1
  return timeDelta.days * 24 * 3600 + timeDelta.seconds

def countdown(timeSeconds):
    minutes, seconds = divmod(timeSeconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    timeFormatted = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, minutes, seconds)
    return timeFormatted

@app.get("/")
def start():
    christmasDate = datetime.strptime('2022-12-25 12:00:00', '%Y-%m-%d %H:%M:%S')
    currentDate = datetime.now()
    secondsDelta = dateDiffInSeconds(currentDate, christmasDate)
    return countdown(secondsDelta)