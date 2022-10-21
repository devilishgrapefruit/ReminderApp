import unittest
import Reminder


class Test_calculator(unittest.TestCase):

    #Тест-кейс на корректный расчет времени (строго относительно указанного времени во время написания теста)
    def test_correct_calc(self):
        self.calculateTim = Reminder.Reminder.calculateTime(12, 12, 12, 12)
        self.assertEqual(self.calculateTim(), "Уведомление сработает через: 52 дней 11 часа 23 минут")


    # Тест-кейс на некоррекный ввод (передачу) данных для расчета (указан 13 месяц)
    def test_wrong_calc(self):
        self.calculateTim = Reminder.Reminder.calculateTime(13, 11, 11, 11)
        self.assertRaises(self.calculateTim(), ValueError)


if __name__ == '__main__':
    unittest.main()
