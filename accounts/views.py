from django.shortcuts import render

from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from accounts.models import  Registercustomer,CustomerBankaccount,Registercustomertranscations


# Create your views here.
def home(request):
    return  render(request,'accounts/home.html')
def about_us(request):
    return  render(request,'accounts/about_us.html')
def contact(request):
    return  render(request,'accounts/contact.html')



class RegisterCustomer(TemplateView):
    template_name = 'accounts/RegisterCustomer.html'
    def get(self,request):
        customers = Registercustomer.objects.filter(first_name='Florence')
        args = {'customers': customers}
        return render(request,self.template_name, args)
class CustomerBankAccount(TemplateView):
    template_name = 'accounts/CustomerBankAccount.html'

    def get(self, request):
        accounts = CustomerBankaccount.objects.filter(full_name='Florence Namukwaya')
        args = {'accounts': accounts}
        return  render(request,self.template_name,args)
@login_required
def view_profile(request):
    args={'user':request.user}
    return  render(request,"accounts/profile.html",args)

class RegisterCustomerTranscations(TemplateView):
        template_name = 'accounts/RegisterCustomerTranscations.html'
        def get(self, request):
            transactions = Registercustomertranscations.objects.filter(Full_name='Florence Namukwaya')

            args = {'transactions':transactions}
            return render(request, self.template_name, args)



def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/accounts')
    else:
        form =RegistrationForm()
        args = {'form':form}
        return render (request,"accounts/register.html",args)
def logout(request):
    logout(request)
    return redirect('/accounts')
