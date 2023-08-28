from django.db import models
import string
import random

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url

    @staticmethod
    def generate_unique_short_code():
        length = 6
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters) for _ in range(length))
            if not ShortenedURL.objects.filter(short_code=short_code).exists():
                return short_code