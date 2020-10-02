from django.db import models

class emp(models.Model):
    ename=models.CharField("emp_name",max_length=50)
    eage = models.IntegerField("emp_age")
    eemail = models.EmailField("emp_email", max_length=50)
    esal = models.FloatField("emp_fees")
    edesg = models.CharField("emp_dept", max_length=50)
    active = models.CharField("active", max_length=50,default='Y')
    #studAddress = models.OneToOneField(Address,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table ='Emp_Info'
