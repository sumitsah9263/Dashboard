from django.shortcuts import redirect, render
from patient_retrieve import patient, visit_detail
from retrieve import readDetail

# Create your views here.


def pat(request):
    if request.user.is_authenticated:
        data = patient(str(request.user))

        context = {"data": data, "user": request.user}
        return render(request, 'patient.html', context)
    else:
        return redirect('/')


def visit(request, patient_id):
    if request.user.is_authenticated:
        data, pdata = visit_detail(patient_id)

        context = {"data": data, "pdata": pdata}
        return render(request, 'visit.html', context)
    else:
        return redirect('/')


def detail(request, visit_id):
    if request.user.is_authenticated:
        data = readDetail(visit_id)
        context = {'data': data}
        return render(request, 'detail.html', context)
    else:
        return redirect('/')
