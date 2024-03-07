from django.db import models

# Create your models here.


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'member'  # DB 테이블 명
        app_label = 'member'
