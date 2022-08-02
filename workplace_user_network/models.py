from django.db import models

# Create your models here.
class User(models.Model):        
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Division(models.Model):        
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Interaction(models.Model):        
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Department(models.Model):        
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class WorkplaceUserNetwork(models.Model):
    from_user = models.ForeignKey('User', related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey('User', related_name='to_user', on_delete=models.CASCADE)
    posting_division = models.ForeignKey('Division', related_name='posting_division', on_delete=models.CASCADE)
    comment_division = models.ForeignKey('Division', related_name='comment_division', on_delete=models.CASCADE)
    interaction = models.ForeignKey('Interaction', on_delete=models.CASCADE)
    posting_department = models.ForeignKey('Department', related_name='posting_department', on_delete=models.CASCADE)
    comment_department = models.ForeignKey('Department', related_name='comment_department', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.from_user.name