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

        print("Для создания напоминания понадобится ввести данные.\n")

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

        print(f'\nНапоминае о дне рождении {Reminder.name}')
        print(f'создано на {Reminder.hour:0>2}:{Reminder.minute:0>2} {Reminder.day:0>2}.{Reminder.month:0>2}')
        print(f'Примечание: {Reminder.message}\n')


    def calculateTime(month, day, hour, minute):
       
        current_date_and_time = datetime.datetime.today()
        desired_date_and_time = datetime.datetime(2022, month, day, hour, minute)
        period =  desired_date_and_time - current_date_and_time

        mm, ss = divmod(period.seconds, 60)
        hh, mm = divmod(mm, 60)

        print('\nУведомление сработает через: {} дней {} часа {} минут.'.format(period.days, hh, mm))
        print("\n")

        Reminder.tseconds = period.total_seconds()


    def show_notify(name, message):

        toast = ToastNotifier()
        toast.show_toast(name, message, duration=20, icon_path="icon.ico")
    

    def notification():

        time.sleep(abs(Reminder.tseconds))
        Reminder.show_notify(f'\nНапоминае о дне рождении {Reminder.name}', f'Заметка: {Reminder.message}')
