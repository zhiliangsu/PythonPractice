from django.db import models

# Create your models here.
class Topic(models.Model):
    """Theme for user study."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return models' string."""
        return self.text