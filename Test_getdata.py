import unittest

class Test_get_data(unittest.TestCase):

        #Тест-кейс для тестирования (пустой)
    # @unittest.skip("demonstrating skipping")
    # def test_nothing(self):
    #     self.fail("shouldn't happen")

    #Тест-кейс на некорректный ввод данных (указан 20 месяц)
    def test_wrong_insert(self):
        self.getData = Reminder.Reminder.getData()
        self.assertEqual(self.getData("20 20"), "Некорректные данные")

    #Тест-кейс на корректный ввод данных
    def test_correct_insert(self):
        self.getData = Reminder.Reminder.getData()
        self.assertIsNotNone(self.getData("12 12", "12 12", "qwert", "qwert"))


if __name__ == '__main__':
    unittest.main()
