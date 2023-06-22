from bot.db.models import Operation, Income, Expense, Category


async def data_months(year, user):
    data = []
    for m in range(1, 13):
        d = []
        for o in await Operation.filter(date__year=year, date__month=m, user=user).all():
            if o.operation_type == 'income':
                print(o.operation_id)
                d.append((await Income.filter(id=o.operation_id).first()).sum)
            else:
                d.append((await Expense.filter(id=o.operation_id).first()).sum)
        if d:
            data.append(sum(d))
        else:
            data.append(0)
    return data


async def data_days_categories(month, user):
    expenses = await Expense.filter(date__month=month, user=user).all()
    categories = await Category.all()
    data = {c.name: 0 for c in categories}
    for e in expenses:
        data[(await e.category.first()).name] += e.sum
    data = {k: data[k] / 100 for k in data}
    return data
