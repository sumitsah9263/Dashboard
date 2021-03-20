from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

import itertools
from subprocess import *
import psutil
import subprocess
import sys
import time
import random
import csv
import json
from datetime import date
import os
import signal
import pickle
# ecg=subprocess.Popen('python Cardio/run.py')

x = 1
ecg = 1
pcg = 1
prev_value = 1
y = 0
open_terminal = True
prev_value_pcg = 1
x_pcg = 500

sumit = 0
extra = False


def profile(request):
    return render(request, 'doc_profile.html')


def doc_reg(request):
    detail = []
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        # detail.append(fname)
        # detail.append(lname)
        # messages.info(request,fname)
        password = request.POST['password1']

        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('../')
    else:
        return render(request, 'login&registration/doc_registration.html')


def home(request):
    global ecg
    detail = []
    p_count = patient_count()
    if request.method == 'POST':
        full_name = request.POST['name']
        age = request.POST['age']
        phone = request.POST['phone']
        gender = request.POST['gender']
        detail.append(full_name)
        detail.append(age)
        detail.append(phone)
        detail.append(gender)
        data = {
            "Name": full_name, "Age": age, "Phone": phone, "Gender": gender
        }
        with open("info.json", "w") as write_file:
            json.dump(data, write_file)
        messages.info(request, full_name)
        print('user created')
        # ecg=subprocess.Popen('python spi.py')
        # theproc.communicate()
        return redirect('/reading')
    else:
        messages.info(request, 100-p_count)
        return render(request, 'patient_new.html')


def patient_count():
    files = folders = 0
    dirs = []

    filename = "count_data.pkl"

    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            dirs_dict = pickle.load(file)
    else:
        dirs_dict = {}

    path = "larkai/patient_Data"  # path for patient_data folder

    for _, dirnames, _ in os.walk(path):
        folders += len(dirnames)
        dirs += dirnames

    for i in dirs:
        if i in dirs_dict:
            dirs_dict[i] += 1
        else:
            dirs_dict[i] = 1

    with open(filename, 'wb') as file:
        pickle.dump(dirs_dict, file)
        file.close()

    return(folders)


def fetch_pcg():
    nline = []

    global prev_value_pcg

    # print('Inside fetch 2')
    # with open('pcg_sibam.csv','r') as pcg:
    # ecg_reader=csv.reader(pcg)
    # s=prev_value_pcg
    # for num in range(prev_value_pcg,x_pcg):
    #san=next(itertools.islice(csv.reader(pcg), s, None))
    # new={'y':san}
    # nline.append(new)
    # s=0
    #prev_value_pcg = x_pcg
    #x_pcg=(prev_value_pcg + 500)
##        print("Start : "+str(prev_value)+" End : "+str(x_pcg))
# print(nline)
    # yield nline
    with open('/home/larkai/Downloads/larkai/pcg_data.csv', 'r') as pcg:
        pcg_reader = csv.reader(pcg)
        # time.sleep(5)

# print("1")
        file = open('/home/larkai/Downloads/larkai/pcg_data.csv')
        reader = csv.reader(file)
        lines = len(list(reader))
        x = lines-50
# print("2")
        s = prev_value_pcg
        for num in range(prev_value_pcg, x):
            # print("3")
            san = next(itertools.islice(csv.reader(pcg), s, None))
            new = {'y': san}
            nline.append(new)
            s = 0


##            print("N Line is ::::::::",nline)
##            print("Starting Value is {} and ending value is {} ".format(prev_value_pcg,x))
        prev_value_pcg = x
        yield nline


def fetch_value(request):
    try:
        data = {}
        sensor_data = []
        nline = []
        global x, prev_value
        with open('ecg_data.csv', 'r') as ecg:
            ecg_reader = csv.reader(ecg)
            # time.sleep(5)

            file = open('ecg_data.csv')
            reader = csv.reader(file)
            lines = len(list(reader))
            x = lines-10

            s = prev_value
            for num in range(prev_value, x):

                san = next(itertools.islice(csv.reader(ecg), s, None))
                new = {'y': san}
                nline.append(new)
                s = 0
            prev_value = x
# print(nline)
            return JsonResponse(nline, safe=False)

    except Exception as e:
        print(e)
        f = open('demofile.txt', 'a')
        f.write(str(e))
        f.close()
        pass


def fetch_value2(request):

    try:
        f1 = open("demofile.txt", "a")
        f1.write("Getting into fetch vale :------->")
        f1.close()
        data = {}
        sensor_data = []
        global open_terminal, ecg, pcg
        global y
        if(open_terminal == True):
            print(
                "Spi 1 ended=====>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# time.sleep(5)
#             os.killpg(os.getpgid(ecg.pid),signal.SIGTERM)
#             ecg.kill()
            open_terminal = False
# print("test")
            process = psutil.Process(ecg.pid)
            for proc in process.children(recursive=True):
                proc.kill()

            process.kill()
            pcg = subprocess.Popen(
                'python3 spi2.py', shell=True, preexec_fn=os.setsid)

        # yield nline
        for ls in fetch_pcg():
            ##            print("ecg is :",ls)
            return JsonResponse(ls, safe=False)
    except Exception as e:
        f1 = open("/home/larkai/Downloads/larkai/demofile.txt", "a")
        f1.write(str(e))
        f1.close()

        # f1.close()
        return render(request, 'final.html', {'exception': e})


def reading(request):
    global extra, ecg
    if(extra == False):
        # ecg=subprocess.Popen('python3 larkai/spi.py',shell=True,preexec_fn=os.setsid)
        time.sleep(1)
        print("Spi 1 started")
        extra = True
    return render(request, 'reading.html')


def loader_reading(request):
    print("Inside loader reading====>>>>>>>>>>>>>>")

    return render(request, 'loader_reading.html')


def loading(request):
    global pcg
    process = psutil.Process(pcg.pid)
    for proc in process.children(recursive=True):
        proc.kill()

    process.kill()
    subprocess.Popen(
        'python3 /home/larkai/Downloads/larkai/Cardio/run.py', shell=True)
    return render(request, 'loader.html')


def final(request):
    global ecg, x, y, extra, open_terminal
    x = 0
    y = 0
    extra = False
    open_terminal = True
    # ecg.terminate()
    print("Spi 2 ended")
    subprocess.Popen('python3 Cardio/pdf_gen.py', shell=True)
    time.sleep(5)
    # messages.info(request,fname)
    # time.sleep(40)
    with open('info.json', 'r') as openfile:
        json_object = json.load(openfile)

        img_name = json_object['Name']+str(date.today())+'/result.png'
        pdf_name = json_object['Name']+str(date.today())+'/report.pdf'
        print(img_name)
    messages.info(request, pdf_name)

    # posts={"img":img_name,"pdf":pdf_name}
    return render(request, 'final.html', {'Image': img_name, 'Name': json_object['Name']})
    # return render(request,'final.html')
