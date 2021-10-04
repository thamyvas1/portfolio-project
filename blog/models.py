from django.db import models

# Create A Blog Models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = image = models.ImageField(upload_to='images/')

# Create a migration

# Migrate

# Add to the admin
