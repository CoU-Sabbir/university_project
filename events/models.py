from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology & Science'),
        ('cultural', 'Cultural & Arts'),
        ('business', 'Business & Management'),
        ('media', 'Media & Journalism'),
        ('gaming', 'Gaming & Esports'),
        ('social', 'Environmental & Social Awareness'),
        ('sports', 'Sports & Fitness'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    registration_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
