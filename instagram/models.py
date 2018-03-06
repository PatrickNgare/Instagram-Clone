from django.db import models
from django.contrib.auth.models import User

#model profile to store user profile
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='avatars/',blank=True,null=True)
    bio=models.TextField(max_length=250)
    user=models.ForeignKey(User)
    update_time = models.DateTimeField(auto_now_add=True, null=True)


    def save_profile(self):
        
        self.save() 
    @classmethod
    def get_profile(cls):
        
        profile=Profile.objects.all()

        return profile


#comment model to store comments data 
class Comment(models.Model):
    
    comment=models.TextField(max_length=300)
    timecomment=models.DateTimeField(auto_now_add=True,null=True)
     

    class Meta:
        ordering=['comment']
        
               
    
#image models to store image data   
class Image(models.Model):
    image=models.ImageField(upload_to= 'gallery/',blank=True,null=True)
    image_name=models.CharField(max_length=60)
    image_caption=models.CharField(max_length=200)
    profile=models.ForeignKey(Profile,null=True,blank=True)
    likes=models.IntegerField(default=0)
    postdate=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, null=True)
    comment=models.ForeignKey(Comment,null=True)
    

    
    class Meta:
        ordering=['image']

    @classmethod
    def my_images(cls):
        
        images = cls.objects.all()
        return images

    def save_image(self):
        
        self.save()   

    @classmethod
    def get_image_by_id(cls,image_id):
        
        images=cls.objects.get(id=image_id)

        return images 

    @classmethod
    def search_by_user(cls,search_term):
        
        images=cls.objects.filter(image_icontains=search_term)
        return images


    @classmethod
    def delete_image():    
       pass


    @classmethod
    def update_caption():   
       pass

