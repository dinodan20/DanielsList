from django.db import models

# Create your models here.

class SonicRing(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    material = models.CharField(default='gold', max_length=100, null=True)
    shape = models.CharField(default='round', max_length=100, null=True)
    # owner = models.ForeignKey('auth.User', related_name='sonicring', on_delete=models.CASCADE, null=True)



    class Meta:
        ordering = ['created']
