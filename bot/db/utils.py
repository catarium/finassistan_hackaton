from bot.db.models import Operation, Income, Expense, Category


async def data_months(year, user):
    up_data = []
    down_data = []
    for m in range(1, 13):
        up = await Income.filter(date__year=year, date__month=m, user=user).all()
        down = await Expense.filter(date__year=year, date__month=m, user=user).all()
        up_data.append(sum([income.sum for income in up]) / 100)
        down_data.append(sum([expense.sum for expense in down]) / 100)
    return (up_data, down_data)


async def data_days_categories(month, user):
    expenses = await Expense.filter(date__month=month, user=user).all()
    categories = await Category.all()
    data = {c.name: 0 for c in categories}
    for e in expenses:
        data[(await e.category.first()).name] += e.sum
    data = {k: data[k] / 100 for k in data}
    return data


async def data_months_categories(year, user):
    expenses = await Expense.filter(date__year=year, user=user).all()
    categories = await Category.all()
    data = {c.name: 0 for c in categories}
    for e in expenses:
        data[(await e.category.first()).name] += e.sum
    data = {k: data[k] / 100 for k in data}
    return data
