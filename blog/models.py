from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('mental_health', 'Mental Health'),
        ('heart_disease', 'Heart Disease'),
        ('covid19', 'Covid19'),
        ('immunization', 'Immunization'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blogs"
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs/", null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
