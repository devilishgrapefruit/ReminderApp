import time
from win10toast import ToastNotifier
import datetime


class Reminder:

    def __init__(self):
        
        self.month = 0
        self. day = 0
        self.hour = 0
        self.minute = 0
        self.name = ""
        self.message = ""
        tseconds = 0


    def getData():
        Reminder.day, Reminder.month = input('Введите дату (в формате dd mm)\t').split()
        Reminder.day, Reminder.month = int(Reminder.day), int(Reminder.month)
        if Reminder.month > 12 or Reminder.day > 31:
            print("Некорректные данные")
            exit()
        Reminder.hour, Reminder.minute = input('Введите время (В формате hh mi)\t').split()
        Reminder.hour, Reminder.minute = int(Reminder.hour), int(Reminder.minute)
        if Reminder.hour > 24 or Reminder.minute > 59:
            print("Некорректные данные")
            exit()
        Reminder.name = str(input('Введите имя именинника\t'))

        Reminder.message = str(input('Введите примечание\t'))



    def calculateTime(month, day, hour, minute):
       
        pass


    def calculateTime():
       pass


    def show_notify():
        pass
    

    def notification():
        pass
