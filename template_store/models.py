from django.db import models

# Create your models here.
class Template(models.Model):
    title = models.CharField('Template Title', max_length =30)
    description = models.TextField()
    image_url = models.CharField('Template Image Url', max_length = 300)
    color = models.CharField('Template Color', max_length = 10, default=None, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None, null=True)

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
    review_title = models.CharField('Review Title', max_length=30, default=None)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField('Score')
    comment = models.CharField('Review Comment', max_length=300)
    
    def __str__(self):
        return self.review_title
