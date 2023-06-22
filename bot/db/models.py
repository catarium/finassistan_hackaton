from tortoise import fields, models
from tortoise.validators import MinValueValidator, MaxValueValidator


class TestModel(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)


class User(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    telegram_id = fields.BigIntField(null=False, unique=True)
    incomes: fields.ReverseRelation['Income']
    expenses: fields.ReverseRelation['Expense']

    class Meta:
        table = 'users'


class Category(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    name = fields.TextField(null=False)
    incomes: fields.ReverseRelation['Income']

    class Meta:
        table = 'categories'


class Income(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    sum = fields.BigIntField(null=False)
    date = fields.DatetimeField(null=False)
    user = fields.ForeignKeyField('models.User', related_name='incomes')

    class Meta:
        table = 'incomes'


class Expense(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    sum = fields.BigIntField(null=False)
    date = fields.DatetimeField(null=False)
    user = fields.ForeignKeyField('models.User', related_name='expenses')
    category = fields.ForeignKeyField('models.Category', related_name='incomes')

    class Meta:
        table = 'expenses'


class Operation(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    operation_type = fields.TextField(null=False)
    operation_id = fields.BigIntField(null=False)
    date = fields.DatetimeField(null=False)
    user = fields.ForeignKeyField('models.User', related_name='operations')

    class Meta:
        table = 'operations'


class Advice(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    content = fields.TextField(null=False)
