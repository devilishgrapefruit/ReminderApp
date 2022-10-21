from Reminder import Reminder


def main():

    print('Для создания напоминания введите 1, для отмены введите 0')
    way = str(input())
    if way == "1":
        Reminder.getData()
        Reminder.calculateTime(Reminder.month, Reminder.day, Reminder.hour, Reminder.minute)
        Reminder.notification()
    else:
        print("Завершение работы")


if __name__ == '__main__':
    main()
