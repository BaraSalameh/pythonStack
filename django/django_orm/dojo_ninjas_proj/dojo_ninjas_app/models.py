from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True)

    def get_id():
        variable = Dojo.objects.all()
        id_list = []
        for i in variable:
            id_list.append(i.id)
        return id_list

    def dojo_all():
        return Dojo.objects.all()

    def set_dojo(name,city,state):
        Dojo.objects.create(name = name,city=city,state=state)
    
        

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(Dojo, related_name= 'ninjas', on_delete=models.CASCADE)

    def ninja_all():
        return Ninja.objects.all()

    def set_ninja(fn,ln,did):
        newNinjaDojo = Dojo.objects.get(id = did)
        Ninja.objects.create(first_name = fn, last_name = ln, dojo_id = newNinjaDojo)

    
