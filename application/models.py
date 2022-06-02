from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# profile of the user.
class Profile(models.Model):
  profile_photo= CloudinaryField('image')
  bio = models.TextField()
  contact = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  # save profile method
  def save_profile(self):
    self.save()
    
  # Save profile method
  def delete_profile(self):
    self.delete()
  
  def __str__(self):
    return self.bio