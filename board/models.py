from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Programmer Name: Elijah Rei Sabay
# I created this category for searching purposes, feel nako lisod if di sha iseparate entity
class Category(models.Model):
    category_name = models.CharField(max_length=30,unique=True)
    category_description = models.TextField(max_length=100)

    def __str__(self):
        return str(self.category_name)
    
class Board(models.Model):
    board_name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    BOARD_TYPES = (
        ('simple', 'Simple Board'),
        ('project', 'Project Board')
    ) 
    board_type = models.CharField(max_length=10, choices=BOARD_TYPES, default='simple')
    THEME = (
        ('white', 'Default (White)'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('pink', 'Pink') 
    )
    board_theme = models.CharField(max_length=10, choices=THEME, default='white')
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')
    date_created = models.DateField(auto_now_add=True)

    # according do documentation standard of many to many is plural
    users = models.ManyToManyField(User)
    user_count = models.IntegerField(default=1) 