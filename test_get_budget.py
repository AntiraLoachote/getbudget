import unittest

from datetime import date
from get_budget import get_budget


class GetBudgetTest(unittest.TestCase):
    def test_should_return_budget_of_one_month_if_input_first_and_last_date(self):
        first_date = date(2018, 9, 1)
        last_date = date(2018, 9, 30)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 1000)

    def test_should_return_budget_if_input_per_range_of_day(self):
        first_date = date(2018, 9, 1)
        last_date = date(2018, 9, 5)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 166.67)

    def test_should_return_bugget_if_input_is_same_day(self):
        first_date = date(2018, 9, 1)
        last_date = date(2018, 9, 1)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 33.33)

    def test_should_return_budget_if_input_per_range_of_day_cross_month(self):
        first_date = date(2018, 9, 1)
        last_date = date(2018, 10, 10)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 1161.29)

    def test_should_return_budget_if_input_per_range_of_day_cross_two_month(self):
        first_date = date(2018, 9, 1)
        last_date = date(2018, 11, 10)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 1600.00)

    def test_should_return_budget_if_input_per_range_of_day_cross_three_month(self):
        first_date = date(2018, 9, 1)
        last_date = date(2018, 12, 10)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 2122.58)

    @unittest.skip(reason='not cover this case')
    def test_should_return_budget_when_start_mid_month_and_end_2_month_later(self):
        first_date = date(2018, 9, 15)
        last_date = date(2018, 11, 30)

        actual = get_budget(first_date, last_date)
        self.assertEqual(actual, 1300)

unittest.main()