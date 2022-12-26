from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserForm
import ftplib
from ftplib import FTP
from docxtpl import DocxTemplate
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    userform = UserForm()
    if request.method == "POST":
        fio = request.POST.get("name")
        age = request.POST.get("age")
        adress = request.POST.get("adress")
        phone = request.POST.get("phone")
        fam = request.POST.get("fam")
        child = request.POST.get("child")
        edu_name1 = request.POST.get("edu_name1")
        edu_sta1 = request.POST.get("edu_sta1")
        edu_ed1 = request.POST.get("edu_ed1")
        spes = request.POST.get("spes")
        dop = request.POST.get("dop")
        comp = request.POST.get("comp")
        op_name1 = request.POST.get("op_name1")
        dolzh = request.POST.get("dolzh")
        op_s1 = request.POST.get("op_s1")
        op_e1 = request.POST.get("op_e1")
        fro = request.POST.get("fro")
        zp = request.POST.get("zp")
        new_dolzh = request.POST.get("new_dolzh")
        har = request.POST.get("har")
        amb = request.POST.get("amb")
        otvet = request.POST.get("otvet")
        date = request.POST.get("date")
        doc = DocxTemplate("анкета для собеседования.docx")
        context = { 'fio' : fio, "birth": age,"adress" : adress,"phone" : phone,
        "fam" : fam, "child" : child, "edu_name1" : edu_name1, "edu_sta1" : edu_sta1,
        "edu_ed1" : edu_ed1, "spes": spes,"dop" : dop, "comp" : comp, "op_name1" : op_name1, "op_s1" : op_s1, "op_e1" : op_e1, "dolzh" : dolzh,
        "fro" : fro, "zp": zp, "new_dolzh" : new_dolzh, "har" : har, "amb": amb, "otvet" : otvet, "date" : date }
        doc.render(context)
        doc.save("{}.docx".format(str(fio)))
        ftp=FTP()
        ftp.connect('192.168.4.5',21)
        ftp.login("hr","P@ssHR22@")
        ftp.encoding = "cp1251"
        file = "{}.docx".format(str(fio))   
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        userform = UserForm()
    return render(request, "index.html", {"form": userform})