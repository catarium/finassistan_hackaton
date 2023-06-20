from tortoise import fields, models
from tortoise.validators import MinValueValidator, MaxValueValidator


class TestModel(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)


class User(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    telegram_id = fields.BigIntField(null=False, unique=True)
    incomes: fields.ReverseRelation['Income']

    class Meta:
        table = 'users'


class Income(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
    sum = fields.BigIntField(null=False)
    user = fields.ForeignKeyField('models.User', related_name='incomes')
    date = fields.DateField(null=False)

    class Meta:
        table = 'incomes'


