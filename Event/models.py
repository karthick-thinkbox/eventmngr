from django.db import models
import datetime
class user_data(models.Model):
    name=models.CharField(max_length=150)
    mobile=models.CharField(null=True,blank=True,max_length=100,unique=True)
    email=models.EmailField(null=True,blank=True,max_length=100)
    idcard_img=models.ImageField(null=True,blank=True,)
    ticket_count=models.PositiveIntegerField(null=True,blank=False)
    reg_choice=(('SF','Self'),('GRP','Group'),('CRP','Corporate'),('Other','Other'),)
    reg_type=models.CharField(max_length=10,choices=reg_choice)
    Event=models.CharField(max_length=50,null=False,blank=False)
    regnum=models.BigIntegerField(null=True,blank=True) 
    
    def save(self, *args, **kwargs):
        if not self.regnum:
            now = datetime.datetime.now()
            self.regnum=str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
            
        super(user_data, self).save(*args, **kwargs) 
    
    


class event_info(models.Model):
    Event_name=models.CharField(max_length=150,unique=True)
    Event_date=models.DateField(null=True,blank=True)
    Location=models.CharField(max_length=150)
    Event_type=models.CharField(max_length=150,null=True,blank=True,)
    
    
    def __str__(self):
        return self.Event_name
        