from django.shortcuts import redirect, render
from .models import Studbook,IssueBook
from datetime import date 

# python manage.py runserver

def index(request):  
    yn="No"
    y=IssueBook.objects.filter(isreturn__icontains=yn)
    qu=request.POST.get('ret')
    for obj in y:
        if obj.book==qu:
            books=Studbook.objects.get(number=qu)
            books.quantity="1"
            books.save() 
            obj.isreturn="Yes"
            obj.save() 
    param={'bkn':y}        
    return render(request,'stud/index.html',param)

def issue(request):
    notavail="0"
    match="1"
    books=Studbook.objects.all()
    if request.method=="POST":
        nam=request.POST['name']
        enrol=request.POST['enrol']
        mob=request.POST['mob']
        booknum=request.POST['booknum']
        is_date=date.today()
        ans=IssueBook(name=nam,enrollment=enrol,mobile=mob,book=booknum,issue_date=is_date)
        for i in books:        
            if i.number == booknum:
                if i.quantity == "1" :
                    i.quantity = "0"
                    i.save()
                    ans.save()
                else: 
                    notavail="1"
            else:
                match="0"
    dict={'notavail':notavail,'match':match}      
    return render(request,'stud/issue.html',dict)

def search(request):
    query=request.GET['query']
    allbooks=Studbook.objects.filter(book_name__icontains=query)
    params={'allbooks':allbooks}
    return render(request,'stud/search.html',params)