import unittest
from time_of_day0 import *

from datetime import datetime

# Bad example of test to test poorly writtern testable code


# class Test(unittest.TestCase):
#
#     def test(self):
#
#         # Setup: change system time to 6AM
#
#         time_of_day = get_time_of_day()
#
#         self.assertEqual("Afternoon", time_of_day)




# Good examples of test for testable code


class Test(unittest.TestCase):


    def test_morning(self):

        time_of_day = get_time_of_day(datetime(2020, 7, 15, 6, 00, 00))

        self.assertEqual("Morning", time_of_day)


    def test_afternoon(self):

        time_of_day = get_time_of_day(datetime(2020, 7, 15, 14, 12, 54))

        self.assertEqual("Afternoon", time_of_day)


    def test_evening(self):

        time_of_day = get_time_of_day(datetime(2029, 7, 15, 23, 59, 59))

        self.assertEqual("Evening", time_of_day)


    def test_night(self):

        time_of_day = get_time_of_day(datetime(2020, 7, 15, 2, 30, 00))

        self.assertEqual("Night", time_of_day)



if __name__ == '__main__':
    unittest.main()
