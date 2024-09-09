from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    portraits = (
        ('1','Steve'),
        ('2','Lisa'),
        ('3','Erik'),
        ('4','Daphne'),
        ('5','Patricia'),
        ('6','Andy'),
    )
    avatar = models.CharField(blank=True, max_length=20, choices=portraits)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.user.username
        return name
