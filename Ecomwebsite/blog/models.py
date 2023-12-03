from django.db import models

# Create your models here.

# We can add models here, in autofield don't forget to put primary_key=True
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    head1 = models.CharField(max_length=3000)
    text1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=5000, default="")
    text2 = models.CharField(max_length=5000, default="")
    head3 = models.CharField(max_length=5000, default="")
    text3 = models.CharField(max_length=5000, default="")
    head4 = models.CharField(max_length=5000, default="")
    text4 = models.CharField(max_length=5000, default="")
    about = models.CharField(max_length=5000, default="")
    details = models.CharField(max_length=5000, default="")
    more = models.CharField(max_length=5000, default="")
    publish_date = models.DateField()
    images = models.ImageField(upload_to="blog/images", default="")


    def __str__(self):
        return self.title