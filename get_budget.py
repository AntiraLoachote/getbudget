from datetime import date, timedelta
from dataclasses import dataclass
from typing import Dict

DAY_OF_MONTH = { 9: 30, 10: 31, 11: 30, 12: 31 }


@dataclass
class Period:
    first_day: date
    last_day: date

    def range_of_month(self):
        return self.last_day.month - self.first_day.month

    def range_of_day(self):
        first_day_of_period = 1
        return (self.last_day - self.first_day).days + first_day_of_period


@dataclass
class Budget:
    budgets: Dict[int, int]

    def per_day(self, month):
        return self.budgets[month] / DAY_OF_MONTH[month]


def get_budget_of_full_month(budgets, period):
    budget_of_full_month = 0
    month = period.first_day.month
    range_of_month = period.range_of_month()

    while range_of_month > 0:
        budget_of_full_month += budgets[month]
        month += 1
        range_of_month -= 1

    return budget_of_full_month


def get_budget(first_day, last_day):
    raw_budget = { 9: 1000, 10: 500, 11: 300, 12: 1000 }

    budgets = Budget(budgets=raw_budget)
    period = Period(first_day=first_day, last_day=last_day)

    if period.range_of_month() > 0:
        budget_of_full_month = get_budget_of_full_month(budgets.budgets, period)

        budget_per_day_of_last_month = budgets.per_day(last_day.month)
        budget = budget_of_full_month + budget_per_day_of_last_month * last_day.day
    else:
        budget_per_day_of_first_month = budgets.per_day(first_day.month)
        budget = budget_per_day_of_first_month * period.range_of_day()

    return round(budget, 2)
