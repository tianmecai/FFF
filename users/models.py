from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(
                            max_length=20,
                            primary_key=True
                            )
    summary = models.TextField(
                               blank=True,
                               null=True
                               )
    def __unicode__(self):
        return self.name
    
class User(models.Model):
    phone = models.CharField(max_length=18,primary_key=True)
    password = models.CharField(max_length=25)
    
    GenderChoices=(
                   ('F','Male'),
                   ('M','Female'),
                   ('N','Unknown')
                   )
    gender = models.CharField(max_length=2,
                              choices=GenderChoices,
                              default='N')    
    nickname = models.CharField(max_length=20,
                                blank=True,
                                null=True)
    nation = models.CharField(max_length=20,
                                blank=True,
                                null=True)
    province = models.CharField(max_length=20,
                                blank=True,
                                null=True)
    city = models.CharField(max_length=20,
                                blank=True,
                                null=True)
    birthdate = models.DateTimeField(blank=True,null=True)
    introduction = models.TextField(blank=True,null=True)
    status = models.TextField(blank=True,null=True)
    hobbies = models.ManyToManyField(Hobby,blank=True,null=True)
    def __unicode__(self):
        return self.phone

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    longitude = models.FloatField(blank=True,
                                    null=True)
    latitude = models.FloatField(blank=True,
                                   null=True)
    
    def __unicode__(self):
        return str(self.id)+':'+self.name    

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    time = models.DateTimeField()
    hobbies = models.ManyToManyField(Hobby,
                                     blank=True,
                                     null=True)
    place = models.ForeignKey(Place,related_name='activity_place',
                              blank=True,
                              null=True)
    num_participant = models.IntegerField(default=0)
    num_limit = models.IntegerField(default=100) 
    summary = models.TextField(blank=True,null=True)  
    starter = models.ForeignKey(User,related_name='starter_user')     
    participant = models.ManyToManyField(User,name='participant_user') 
    
    # for many to many relationship between Place and Activity 
    place_record = models.ManyToManyField(Place,
                                          name='placerecord_user',
                                           blank=True,
                                             null=True)
    def __unicode__(self):
        return str(self.id)+':'+self.name



class Remark(models.Model):
    id = models.AutoField(primary_key=True)
    remark = models.TextField()
    author = models.ForeignKey(User)
    place = models.OneToOneField(Place)
    