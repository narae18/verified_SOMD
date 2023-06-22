from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
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
    admins = models.ManyToManyField(User, related_name="somd_admins")
    admin = models.ForeignKey(User, related_name="somd_admin", on_delete=models.CASCADE, blank=False, null=False, default=1)
    bookmark = models.ManyToManyField(User, related_name='bookmark', blank=True)

    def __str__(self):
        return self.name
    
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    somds = models.ManyToManyField(SOMD, related_name="members", blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    somd = models.ForeignKey(SOMD, null=False, blank=False, on_delete=models.CASCADE,related_name='somds')
    content = models.TextField()
    scrap = models.ManyToManyField(User, related_name='scrap', blank=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.content) > 65:
            return self.content[:65]+'...'
        else:
            return self.content
        

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="post/", blank=True, null=True)    

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title+" : "+self.content[:20]
    
class JoinRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title =  models.CharField(max_length=50,blank=False,null=False)
    motivation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.user.username}'