from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic.list import ListView
from .models import user_data,event_info
from .forms import userform,eventform
from django import forms
from django.db.models import Count
from .tables import cat_table
from django_tables2 import RequestConfig



def user_reg(request):
    userform.base_fields['Event']=forms.ModelChoiceField(queryset=event_info.objects.all())
    
    if request.method=="POST":
        getform=userform(request.POST)
        if getform.is_valid():
            '''
            if 'preview' in request.POST:
                post_row=getform.save(commit=False)
                pre_name=getform.cleaned_data['name']
                pre_mobile=getform.cleaned_data['mobile']
                pre_email=getform.cleaned_data['email']
                pre_evtype=getform.cleaned_data['reg_type']
                pre_event=getform.cleaned_data['Event']
                pre_count=getform.cleaned_data['ticket_count']
                pre_img=getform.cleaned_data['idcard_img']
                return render(request,'preview.html',{ 'form2':getform,'name':pre_name,'mobile':pre_mobile,'email':pre_email,'evt_type':pre_evtype,'count':pre_count,'evt':pre_event,'img':pre_img})
             '''   
            if 'preview' not in request.POST:
                try:
                    getform.save()
                except Exception as Error:
                    form=userform()
                    return render(request,'registration.html',{'form':form,'Error':Error})
                row=user_data.objects.latest('id')
                form=userform()
                return render(request,'registration.html',{'form':form,'stat':'Success','reg_num':row.regnum})
        Error=getform.errors
        form=userform()
        return render(request,'registration.html',{'form':form,'Error':Error})
        
            
    
    form=userform()
    return render(request,'registration.html',{'form':form})
def exitpage(request):
    logout(request)
    return render (request,'logout.html')

@login_required(login_url='login_page')
@permission_required('Event.add_event_info' ,login_url='Error_page')
def managerview(request):
    
    qryset=user_data.objects.values('reg_type').annotate(count=Count('reg_type'))
    master=[]
    master.append(['Task', 'link', 'Hours per Day'])
    for i in qryset:
        cat=i.get('reg_type')
        cnt=i.get('count')
        link='/cat/'+cat+'/'
        lis=[]
        lis.append(cat)
        lis.append(link)
        lis.append(cnt)
        master.append(lis)
    return render(request,'base.html',{'dict':master})
def table(request,pk):
    qset=user_data.objects.filter(reg_type=pk)
    table=cat_table(qset)
    RequestConfig(request).configure(table)
    return render(request,'detail.html',{'table':table})
def addevent(request):
    if request.method=="POST":
        form=eventform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'evtform.html',{'form':form ,'stat':'Success'})
        Error=form.errors
        form=eventform()
        return render(request,'evtform.html',{'form':form,'Error':Error})
    
    form=eventform()    
    return render(request,'evtform.html',{'form':form})
def exitpage(request):
    logout(request)
    return render (request,'logout.html')