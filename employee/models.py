from django.db import models

# Create your models here.
class Status(models.Model):
    name= models.CharField(max_length=20,verbose_name= "Status", unique=True)
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural ="Status"
        verbose_name ="Status"
        db_table = "status"

class  Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=5,verbose_name="Employee_id", unique= True)
    last_name = models.CharField(max_length=255,verbose_name="Last_Name")
    first_name = models.CharField(max_length=255,verbose_name="First_Name")
    email= models.EmailField(max_length=255,verbose_name= "email",unique=True, null=True,blank=True)
    department= models.CharField(max_length=255,verbose_name="department", null=True, blank=True)
    job_role= models.CharField(max_length=255,verbose_name="Job_role",null=True, blank=True)
    gender = models.CharField (max_length=10,verbose_name="Gender", null=True, blank=True)
    phone_number = models.CharField(max_length=11,verbose_name="Phone_Number", null=True, blank=True)
    alternate_number = models.CharField(max_length=11,verbose_name="Alt_Number", null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="date_joined" , null=True, blank=True)
    date_of_birth = models.DateTimeField(verbose_name="Date_Of_Birth" , null=True, blank=True)
    is_active =models.BooleanField(verbose_name="active_status", null=True, blank=True)
    leave_status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural ="Employee"
        verbose_name ="Employee"
        db_table = "employee"
    
 