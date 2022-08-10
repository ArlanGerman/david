from typing import List
from django.db import models

class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True

    @staticmethod
    def get_fields() -> List[str]:
        return ['id']