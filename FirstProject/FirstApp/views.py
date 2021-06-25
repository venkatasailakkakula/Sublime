from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.
def home(request):
	return HttpResponse("Hi Good Evening to All...")


def htmltag(y):
	return HttpResponse("<h2>Hi Welcome to APSSDC Program</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:pink'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:green;padding:23px'>Hi User <span style='color:blue'>{}</span> and your age is: <span style='color:red'{}</span></h3>".format(un,ag))


def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is: {</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def page(request):
	return render(request,'html/ug1.html')

def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(request):
	if request.method=="POST":
		#print(request.POST)
		uname=request.POST['uname']
		rollno=request.POST['rollno']
		email=request.POST.get('email')
		#print(uname,rollno,email)
		data={'username':uname,'rno':rollno,'emailId':email}
		return render(request,'html/display.html',data)

	return render(request,'html/myform.html')

def form(request):
	if request.method=="POST":
		#print(request.POST)
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST.get('email')
		phno=request.POST.get('phno')
		gender=request.POST['gender']
		address=request.POST['address']
		languages=request.POST.getlist('languages')

		#print(uname,rollno,email)
		data={'firstname':fname,'lastname':lname,'emailId':email,'phonenumber':phno,'gender':gender,'address':address,'languages':languages}
		return render(request,'html/show.html',data)
	return render(request,'html/form.html')

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def btrgei(request):
	return render(request,'html/btregst.html')

def reg(request):
	return render(request,'html/reg.html')

def register1(request):
	# name = "siva"
	# email = "siva@gmail.com"
	reg = Register(name = "rasool",email = "rasool@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully...")

def register2(request):
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name,email = email)
		reg.save()
		return HttpResponse("Record inserted successfully")
	return render(request,'html/register2.html')

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	# return HttpResponse("Your name is {} and your email id is: {}".format(w.name,w.email))

def supt(request,q):
	t=Register.objects.get(id=q)
	if request.method=='POST':
		na=request.POST['n']
		em=request.POST['e']
		t.name=na
		t.email=em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b=Register.objects.get(id=p)
	if request.method=="POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndel.html',{'z':b})