from django.shortcuts import render
import pyrebase
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
config = {
    'apiKey': "AIzaSyDacvxdaPmR8qgOqHWXSFKYqJQP1aaDae0",
    'authDomain': "kritiapp-2f73b.firebaseapp.com",
    'databaseURL': "https://kritiapp-2f73b.firebaseio.com",
    'projectId': "kritiapp-2f73b",
    'storageBucket': "kritiapp-2f73b.appspot.com",
    'messagingSenderId': "924829656507",
    'appId': "1:924829656507:web:753c82b560e4a375d1d09e",
  'measurementId': "G-13JKYMC09Z"
  }

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def home(request):
    return render(request, "home.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request,"home.html",{"messg":message})

    # print(user['idToken'])

    if email in ['cse@iitg.ac.in','eee@iitg.ac.in','codingclub@iitg.ac.in','finance@iitg.ac.in']:
        uid = user['localId']
        name = database.child("ClubDept").child(uid).child("name").get()
        all_courses = database.child(name.val()).child("courses").get()
        # print ("//////////////............",all_courses.val())
        courses = []
        count = 0
        try:
            for course in all_courses.each():
                courses.append(str(count) + " "+course.key())
                count += 1
        except :
            pass
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        return render(request, "upload.html",{"name":name.val(),"courses":courses})
    else:    
        uid = user['localId']
        name = database.child("Users").child(uid).child("name").get()
        # print ("....................",name.val())
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        return render(request, "index.html",{"name":name.val()})

def upload(request):
    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    uid = a['localId']
    name = database.child("Users").child(uid).child("name").get()
    return render(request, "upload_common.html",{"name":name.val()})



def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def postsignup(request):

    name=request.POST.get('name')
    roll=request.POST.get('rollno')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data={"name":name,"roll":roll}
        database.child("Users").child(uid).set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})
    return render(request,"home.html")



def create(request):

    return render(request,'upload_home.html')

def upload_save(request):
    dept = request.POST.get('dept')
    OverView =request.POST.get('overview')
    url = request.POST.get('url')
    title = request.POST.get('vtitle')
    data_json = {
        'bookOverview': OverView,
        'url': url
    }
    database.child(dept).child('Reading').child(title).set(data_json)
    return render(request,'Welcome.html')

def post_create(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Kolkata')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))
    # dept = request.POST.get('dept')
    
    vtitle = request.POST.get('vtitle')
    OverView =request.POST.get('progress')
    url = request.POST.get('url')
    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    dept = database.child("ClubDept").child(a).child("name").get()
    if request.POST.get('work'):
        Title = request.POST.get('work')
    else:
        all_courses = database.child(dept.val()).child("courses").get()
        courses = []
        try:
            for course in all_courses.each():
                courses.append(course.key())
        except :
            pass
        # print (";;;;;;;;;;;;;;;;;;;;",courses)
        count = request.POST.get('title')
        Title = courses[int(count)] 
    print("info"+str(a))
    url_json = {
        'url':url
    }
    OverView_json = { 'OverView':OverView }
    database.child(dept.val()).child('courses').child(Title).child("OverView").set(OverView_json)
    database.child(dept.val()).child('courses').child(Title).child("urls").child(vtitle).set(url_json)
    name = database.child('Users').child(a).child('name').get()
    return render(request,'Welcome.html', {'e':name.val()})

def departments(request):
     return render(request,'departments.html')


def club(request):
     return render(request,'clubs.html')

def civil(request):
    return render(request, 'deps.html' , {'name': 'Civil Engineering','uc': 'civcourse'})

def mech(request):
    return render(request, 'deps.html' , {'name': 'Mechanical Engineering','uc': 'mccourse'})

def ece(request):
    return render(request, 'deps.html' , {'name': 'Electronics Engineering','uc': 'eccourse'})

def eee(request):
    return render(request, 'deps.html' , {'name': 'Electrical Engineering','uc': 'eecourse'})

def mnc(request):
    return render(request, 'deps.html' , {'name': 'Mathematics And Computing','uc': 'mnccourse'})

def bio(request):
    return render(request, 'deps.html' , {'name': 'Bio-Tech Engineering','uc': 'biocourse'})

def cse(request):
    
    return render(request, 'deps.html' , {'name': 'Computer Science Engineering','uc': 'csecourse'})

def chem(request):
    return render(request, 'deps.html' , {'name': 'Chemical Engineering','uc': 'chemcourse'})

def civilcourse(request):
    all_courses = database.child('CIVIL').child("courses").get()
    
    return render(request, 'courses.html' , {'name': 'CIVIL','full':all_courses.val()})

def mechcourse(request):
    all_courses = database.child('MECH').child("courses").get()
    
    return render(request, 'courses.html' , {'name': 'MECHANICAL','full':all_courses.val()})

def ececourse(request):
    all_courses = database.child('ECE').child("courses").get()
    
    return render(request, 'courses.html' , {'name': 'ELECTRONICS','full':all_courses.val()})

def eeecourse(request):
    all_courses = database.child('EEE').child("courses").get()
    
    return render(request, 'courses.html' , {'name': 'ELECTRICAL','full':all_courses.val()})

def mnccourse(request):
    all_courses = database.child('MNC').child("courses").get()
   
    return render(request, 'courses.html' , {'name': 'Maths','full':all_courses.val()})

def biocourse(request):
    all_courses = database.child('BIO').child("courses").get()
   
    return render(request, 'courses.html' , {'name': 'Bio-Tech','full':all_courses.val()})

def csecourse(request):
    all_courses = database.child('CSE').child("courses").get()
   
    return render(request, 'courses.html' , {'name': 'CSE', 'full':all_courses.val()})

def chemcourse(request):
    all_courses = database.child('CHEM').child("courses").get()
    
    return render(request, 'courses.html' , {'name': 'Chemical','full':all_courses.val()})


