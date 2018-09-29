from datetime import date, timedelta


def get_budget(first_day, last_day):
    day_of_month = { 9: 30, 10: 31, 11: 30, 12: 31 }
    budgets = { 9: 1000, 10: 500, 11: 300, 12: 1000 }

    range_of_day = (last_day - first_day).days + 1

    if range_of_day == 30 or range_of_day == 31:
        return budgets.get(first_day.month)
    else:
        range_of_month = last_day.month - first_day.month
        if range_of_month > 0:
            budget_of_full_month = 0
            month_number = first_day.month
            while range_of_month > 0:
                budget_of_full_month += budgets.get(month_number)
                month_number += 1
                range_of_month -= 1

            budget_month_of_last = budgets.get(last_day.month)
            day_of_month_of_last = day_of_month.get(last_day.month)

            budget_per_day_of_last = (budget_month_of_last/round(day_of_month_of_last, 2))
            return round(budget_of_full_month + budget_per_day_of_last*last_day.day, 2)

        elif range_of_month == 0:
            budget = (budgets.get(first_day.month)/round(30, 2))*range_of_day
            return round(budget, 2)


        # if last_day.month - first_day.month == 1:
        #     budget_of_month_of_first = budgets.get(first_day.month)

        #     budget_month_of_last = budgets.get(last_day.month)
        #     day_of_month_of_last = day_of_month.get(last_day.month)

        #     budget_per_day_of_last = (budget_month_of_last/round(day_of_month_of_last, 2))
        #     return round(budget_of_month_of_first + budget_per_day_of_last*last_day.day, 2)

        # elif last_day.month - first_day.month == 2:
        #     budget_of_month_of_first = budgets.get(first_day.month)
        #     budget_of_month_of_seccond = budgets.get(first_day.month + 1)

        #     budget_month_of_last = budgets.get(last_day.month)
        #     day_of_month_of_last = day_of_month.get(last_day.month)

        #     budget_per_day_of_last = (budget_month_of_last/round(day_of_month_of_last, 2))
        #     return round(
        #         budget_of_month_of_first +
        #         budget_of_month_of_seccond +
        #         budget_per_day_of_last*last_day.day, 2
        #         )
        # elif last_day.month - first_day.month == 0:
        #     budget = (budgets.get(first_day.month)/round(30, 2))*range_of_day
        #     return round(budget, 2)
