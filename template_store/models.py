from django.db import models

# Create your models here.
class Theme(models.Model):
    title = models.CharField('Theme Title', max_length =30)
    description = models.CharField('Theme Description', max_length = 300)
    image_url = models.CharField('Theme Image Url', max_length = 30)

    def mean_rating(self):
        self.reviews.all() # get all ratings
        
    def __str__(self):
        return self.title

        # then compute mean rating and return it
        
class User(models.Model):
    name = models.CharField("User's Name", max_length=30)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField('Theme Score')
    comment = models.CharField('Review Comment', max_length=300)
    
    def __str__(self):
        return self.theme
