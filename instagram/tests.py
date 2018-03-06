from django.test import TestCase
import datetime as dt
from .models import Image, Profile
from django.contrib.auth.models import User


class ImageTestClass(TestCase):
     
    def setUp(self):
         self.image=Image(image='imagelink',image_name="coding",image_caption="amazing laptop",likes="456",profile=patel)


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))


    def test_delete(self):
        self.image.save_image()
        images=Image.objects.all()
        self.image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)==0)



class ProfileTestClass(TestCase):


    def setUp(self):

        user =User(usrname='smith')
        self.profile=Profile(profile_photo='imgurl',bio="God is loving God",user=user,update_time='update_time')

    def test_save(self):
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profiles)>0)    


    def test_delete(self):

        self.profile.save_profile()

        profile=Profile.objects.all()

        self.profile.delete()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)==0)








