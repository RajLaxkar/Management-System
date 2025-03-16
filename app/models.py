from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary =models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s " %(self.first_name,self.last_name,self.phone)
    



# Matlab agar aap kisi employee ka department ya role check karna chahein, toh uska reference Department aur Role tables me milega.
# on_delete=models.CASCADE ka Matlab
# on_delete batata hai ki jab ek parent record (Department ya Role) delete ho jaye, toh uske associated child records (Employee) par kya effect padega.
# models.CASCADE
# Agar koi Department delete hota hai, toh us department ke saare employees bhi delete ho jayenge.
# Example: dept = models.ForeignKey(Department, on_delete=models.CASCADE)
# Agar "HR" department delete ho gaya, toh jitne bhi employees HR department me kaam kar rahe the, wo bhi delete ho jayenge.