from tortoise import fields, models
from tortoise.validators import MinValueValidator, MaxValueValidator


class TestModel(models.Model):
    id = fields.BigIntField(pk=True, null=False, unique=True, index=True)
