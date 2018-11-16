from django.db import models
from django.contrib.auth.models import User,BaseUserManager
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    
    profile_photo = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)
    user = models.OneToOneField(User, null = True, blank=True)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def search_user(cls,username):
        searched_user = User.objects.get(username = username)
        return searched_user

    # def __str__(self):
    #     return self.user.username


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', blank = True)
    image_title = models.CharField(max_length = 100, null=True, blank= True)
    image_caption = HTMLField()
    user_profile = models.ForeignKey(User,null=True,blank=True,on_delete = models.CASCADE)
    posted_on = models.DateTimeField(default=datetime.now)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    def update_caption(self,image_caption):
        self.image_caption = image_caption
        self.save()
    

    def __str__(self):
        return self.image_title

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image

class Comment(models.Model):

    photo = models.ForeignKey(Image,on_delete = models.CASCADE, blank = True)
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    comment = models.CharField(max_length = 400)


    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


    def get_comments_by_images(cls, id):
        comments = Comment.objects.filter(image_pk = id)
        return comments