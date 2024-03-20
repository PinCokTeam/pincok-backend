from django.db import models

class Crew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    master = models.IntegerField(default=0)
    
    class Meta:
        db_table = "crews"
        app_label = "crew"
