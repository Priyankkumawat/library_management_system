from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class book(models.Model):
    number = models.CharField(max_length=10,primary_key=True,default="1.1.1")
    table_num=models.PositiveSmallIntegerField(default=1)
    sub_num=models.PositiveSmallIntegerField(default=1)
    book_num=models.PositiveSmallIntegerField(default=1)
    book_name=models.CharField(max_length=50,default="")
    author_name=models.CharField(max_length=50)
    quantity=models.PositiveSmallIntegerField(default=1)
    edition=models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.book_name

class issuebook(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=12)
    enrollment=models.CharField(max_length=12)
    book=models.CharField(max_length=10,primary_key=True)
    issue_date=models.DateField(auto_now=False,auto_now_add=False, default = date.today())
    isreturn=models.CharField(max_length=4, default="No")

    def __str__(self):
        return self.name

    @property
    def Number_of_days(self):
        today=date.today()
        days=today-self.issue_date
        d=str(days).split(" ",1)[0]
        return d
        
