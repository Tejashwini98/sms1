from django.shortcuts import render, redirect
from .models import Application,Scheme
from .forms import ApplicationForm, SchemeForm
from django.contrib import messages

def application_view(request):
    if request.user.is_authenticated:
        application = Application.objects.filter(user=request.user)
        if application:
            # application = Application.objects.get(user=request.user)
            # id = application.id
            id = request.user.id
            messages.success(request, "you have already applied for the schoolarship")
            return redirect(f"/core/applications-status/{id}")
        if request.method == "POST":
            form = ApplicationForm(request.POST,request.FILES)
            if form.is_valid():
                dilip = form.save(commit=False)
                dilip.user = request.user
                dilip.save()
                id = request.user.id
                messages.success(request, "you have applied for the schoolarship")
                return redirect(f"/core/applications-status/{id}")
        
        form = ApplicationForm()
        return render(request, "core/schoolarship.html", {'form':form})
    return redirect("/account/login/")

def approval_view(request):
    if request.method == "POST":
        form = ApprovalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(".")
    form =ApprovalForm()
    return render(request ,'core/approval.html',{'form':form})

def amount_view(request):
    if request.method == "POST":
        form = AmountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(".")
    form = AmountForm()
    return render(request, 'core/amount.html', {'form':form})

def no_of_application(request):
    if request.user.is_staff:
        application = Application.objects.all()
        return render(request, 'core/all_application.html',{'application':application})
    else:
        messages.warning(request, "you are not authorised")
        return redirect("/")
def applicant_detail(request, pk):
    application = Application.objects.get(id=pk)
    return render(request, 'core/applicant_detail.html',{'application':application})

def approved_application_view(request):
    application = Application.objects.filter(status="approve")
    return render(request, 'core/approved_application.html',{'application':application})
    
def rejected_application_view(request):
    application = Application.objects.filter(status="reject")
    return render(request, 'core/rejected_application.html',{'application':application})

def pending_application_view(request):
    application = Application.objects.filter(status="pending")
    return render(request, 'core/pending_application.html',{'application':application})
  
def application_status_view(request, pk):
    try:
        application = Application.objects.get(user=request.user)
        return render(request, 'core/application_status.html',{'application':application})
    except:
        return render(request, 'core/application_status.html')

def reject_view(request, pk):
    application = Application.objects.get(id=pk)
    application.status = "reject"
    application.save()
    return redirect("/core/applications/")

def approve_view(request, pk):
    application = Application.objects.get(id=pk)
    application.status = "approve"
    application.save()
    return redirect("/core/applications/")

def processing_view(request, pk):
    application = Application.objects.get(id=pk)
    application.status = "processing"
    application.save()
    return redirect("/core/applications/")


def create_scheme_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form = SchemeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        form = SchemeForm()
        return render(request, 'core/create_scheme.html',{'form':form})
    return redirect("/")

def scheme_list_view(request):
    scheme = Scheme.objects.filter(publish=True)
    return render(request, 'core/scheme_list.html',{'scheme':scheme})