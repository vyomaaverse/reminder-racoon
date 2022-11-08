import datetime
import discord

class Reminder:
    def __init__(self, messageauthor):
       
        self.dates = dict.fromkeys(range(7), [])
        self.messageauthor = messageauthor
        print(self.dates)

    def add(self, day, hour, minute):
        self.dates[day].append(datetime.time(hour, minute))