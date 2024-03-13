from django.db import models

# Create your models here.


class Contents(models.Model):
    id = models.AutoField(primary_key=True)
    # member_id = models.ForeignKey(to='Member', on_delete=models.CASCADE)
    # crew_id = models.ForeignKey(to='Crew', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    detail = models.TextField(verbose_name='내용')
    pos_x = models.FloatField()
    pos_y = models.FloatField()

    class Meta:
        app_label = 'contents'
