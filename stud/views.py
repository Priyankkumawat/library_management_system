from django.shortcuts import redirect, render
from .models import book,issuebook
from datetime import date 
from django.db.models import F 

# python manage.py runserver

def index(request):  
    yn="No"
    y=issuebook.objects.filter(isreturn__icontains=yn)
    qu=request.POST.get('ret')
    for obj in y:
        if obj.book==qu:
            books=book.objects.get(number=qu)
            books.quantity=F('quantity')+1
            books.save() 
            obj.isreturn="Yes"
            obj.save()
    param={'bkn':y}        
    return render(request,'stud/index.html',param)

def issue(request):
    books=book.objects.all()
    if request.method=="POST":
        nam=request.POST['name']
        enrol=request.POST['enrol']
        mob=request.POST['mob']
        booknum=request.POST['booknum']
        is_date=date.today()
        ans=issuebook(name=nam,enrollment=enrol,mobile=mob,book=booknum,issue_date=is_date)
        for i in books:
            if i.number == booknum:
                if i.quantity >= 1 :
                    i.quantity=F('quantity')-1
                    i.save()
                    ans.save()
                else: 
                    print("not awailable")
            else:
                print("not match")
    return render(request,'stud/issue.html')

def search(request):
    query=request.GET['query']
    allbooks=book.objects.filter(book_name__icontains=query)
    params={'allbooks':allbooks}
    return render(request,'stud/search.html',params)

# def delete(request,id):
#     event=issuebook.objects.get(id=book)
#     event.delete()
#     return redirect('stud/index.html')
    