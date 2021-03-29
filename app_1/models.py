from django.db import models


class URL(models.Model):
    url = models.CharField(max_length=256)
    slug = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return f'{self.slug}'
