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



