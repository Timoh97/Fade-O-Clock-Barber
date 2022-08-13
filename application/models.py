from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.utils import timezone


# user = User.objects.create_user(
#     'username',
#     password='password',
#     last_login=timezone.now(),
#     email='email'
#     # Whatever other attributes you want:
# )
# user.save()

# profile of the user.
class Profile(models.Model):
  profile_photo= CloudinaryField('image')
  bio = models.TextField()
  username = models.CharField(max_length=50)
  email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
  contact = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  # save profile method
  def save_profile(self):
    self.save()
    
  # Save profile method
  def delete_profile(self):
    self.delete()
  
  def __str__(self):
    return self.bio

class Appointment(models.Model):
  
  description = models.TextField()
  username = models.CharField(max_length=50)
  contact = models.CharField(max_length=50)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  admin_approved = models.BooleanField(default=False)
  
  
   # save profile method
  def save_appointment(self):
    self.save()
    
  # Save profile method
  def delete_appointment(self):
    self.delete()
    
    
  def __str__(self):
    return self.description