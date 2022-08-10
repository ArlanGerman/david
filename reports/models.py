from typing import List
from david.models import BaseModel
from django.db import models
from django.contrib.auth.models import User

class DailyReportsModel(BaseModel):
    date_created = models.DateTimeField(blank=False, null=False, auto_now=True)
    title = models.TextField(blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    @staticmethod
    def get_fields() -> List[str]:
        return BaseModel.get_fields() +  ['title', 'body', 'author']