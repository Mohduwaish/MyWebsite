from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class TechPost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    thumbnail = models.ImageField(upload_to='images', null=True)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField(blank= True, null= True)
    #content=models.TextField()
    tags = models.ManyToManyField('Tag')
    likes = models.ManyToManyField(User,related_name='tech_posts')
    #parent_category = models.ManyToManyField('Tag')


    def __str__(self):
        return self.title + " by " + self.author

    
class TechBlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, related_name='techblog_comments', on_delete=models.CASCADE)
    post=models.ForeignKey(TechPost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username        

