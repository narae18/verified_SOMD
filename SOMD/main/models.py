from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)

class SOMD(models.Model):
    name = models.CharField(max_length=30)
    profileimage = models.ImageField(upload_to="somd/", blank=True, null=True)
    backgroundimage = models.ImageField(upload_to="somd/", blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    intro = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(Tag, related_name='somds', blank=True)
    snslink = models.CharField(max_length=200, blank=True,null=True)
    admins = models.ManyToManyField(User, related_name="somd_admin")

    def __str__(self):
        return self.name
    
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    somds = models.ManyToManyField(SOMD, related_name="members", blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title+" : "+self.content[:20]