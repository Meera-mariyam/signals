from pyexpat import model
from django.db import models
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from datetime import date, datetime
import json

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)


    def __str__(self) :
        return self.name

class Taskdate(models.Model):
    task =models.ForeignKey(Task,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

class History(models.Model):
    historical =models.TextField(default='{}')

'''
def task_handler(sender,instance,**kwargs):
    print('New Task')
    print(instance)
    print(instance.name)
pre_save.connect(task_handler,sender=Task)'''


@receiver(pre_save,sender=Task)
def task_handler(sender,instance,**kwargs):
    print('2nd way')

@receiver(post_save,sender=Task)
def task_handler_post(sender,instance,**kwargs):
    Taskdate.objects.create(task=instance,date=datetime.now())
    print(date)


@receiver(pre_delete,sender=Task)
def task_handler(sender,instance,**kwargs):
    print('2nd way')

@receiver(post_delete,sender=Task)
def task_handler_post(sender,instance,**kwargs):
    data = {'task' : instance.name,'desc':instance.description}
    History.objects.create(historical=json.dumps(data))
