from django.db import models
from datetime import date

# Create your models here.

# class Studbook(models.Model):
#     number = models.CharField(max_length=10,primary_key=True,default="1.1.1")
#     table_num=models.PositiveSmallIntegerField(default=1)
#     sub_num=models.PositiveSmallIntegerField(default=1)
#     book_num=models.PositiveSmallIntegerField(default=1)
#     book_name=models.CharField(max_length=50,default="")
#     author_name=models.CharField(max_length=50)
#     publication=models.CharField(max_length=15)
#     quantity=models.PositiveSmallIntegerField(default=1)
#     edition=models.PositiveSmallIntegerField(default=1)

class Studbook(models.Model):
    number = models.CharField(db_column='Number', max_length=9, primary_key=True)  
    table_number = models.CharField(db_column='Table number', max_length=12)  
    subject_num = models.CharField(db_column='Subject num', max_length=12)  
    book_number = models.CharField(db_column='book number', max_length=11)  
    book_name = models.CharField(db_column='Book name', max_length=59)
    author = models.CharField(db_column='Author', max_length=34, blank=True) 
    publication = models.CharField(db_column='Publication', max_length=41,blank=True)  
    edition = models.CharField(db_column='Edition', max_length=13, default="First",blank=True)  
    quantity = models.CharField(db_column='Quantity',default="1",max_length=2)
 
    def __str__(self):
        return self.book_name

    class Meta:
        managed = False
        db_table = 'studbook'


# class Issuebook(models.Model):
#     name=models.CharField(max_length=20)
#     mobile=models.CharField(max_length=12)
#     enrollment=models.CharField(max_length=12)
#     book=models.CharField(max_length=10,primary_key=True)
#     issue_date=models.DateField(auto_now=False,auto_now_add=False, default = date.today())
#     isreturn=models.CharField(max_length=4, )

class IssueBook(models.Model):
    name = models.CharField(db_column='Name', max_length=30)  
    mobile = models.CharField(db_column='Mobile', max_length=12)  
    enrollment = models.CharField(db_column='Enrollment', max_length=12)  
    book = models.CharField(db_column='Book', max_length=10, primary_key=True)  
    issue_date=models.DateField(db_column='Issue Date',auto_now=False,auto_now_add=False,default=date.today())
    isreturn = models.CharField(db_column='Isreturn', max_length=8, default="No") 

    def __str__(self):
        return self.name
    
    @property
    def Number_of_days(self):
        today=date.today()
        days=today-self.issue_date
        d=str(days).split(" ",1)[0]
        return d

    class Meta:
        managed = False
        db_table = 'issue_book'