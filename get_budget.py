from datetime import date, timedelta


def get_range_of_day(first_day, last_day):
    first_day_of_period = 1
    return (last_day - first_day).days + first_day_of_period


def get_budget(first_day, last_day):
    day_of_month = { 9: 30, 10: 31, 11: 30, 12: 31 }
    budgets = { 9: 1000, 10: 500, 11: 300, 12: 1000 }

    range_of_day = get_range_of_day(first_day, last_day)

    range_of_month = last_day.month - first_day.month
    if range_of_month > 0:
        budget_of_full_month = 0
        month_number = first_day.month
        while range_of_month > 0:
            budget_of_full_month += budgets[month_number]
            month_number += 1
            range_of_month -= 1

        budget_month_of_last = budgets[last_day.month]
        day_of_month_of_last = day_of_month[last_day.month]

        budget_per_day_of_last = (budget_month_of_last/round(day_of_month_of_last, 2))
        return round(budget_of_full_month + budget_per_day_of_last*last_day.day, 2)
    else:
        budget = (budgets[first_day.month]/round(day_of_month[first_day.month], 2))*range_of_day
        return round(budget, 2)
