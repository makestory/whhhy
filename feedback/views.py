#coding=utf-8
from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
from feedback.models import Message,Customer
from feedback.forms import MessageForm
from daily.models import Daily
from base import BaseView

def ajax(request):
    if request.method == 'POST':
        url  = request.META['HTTP_REFERER']
        date = url[-11:-1]
        form = MessageForm(request.POST)
        try:
            daily = Daily.objects.get(date=date)
        except:
            daily = None
        if form.is_valid():
            content = form.cleaned_data['content']
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            ip      = request.META['REMOTE_ADDR']
            at      = daily
            m       = Message(customer=Customer.objects.get(name = name),content = content,ip = ip,at = at)
            m.save()
            number=Message.objects.filter(at=daily).count()
            return render_to_response('ajax.xml', {'form':form,'message':m,'number':number,'ok':True})
        else:
            return render_to_response('ajax.xml', {'form':form,'ok':False})
    else:
        return render_to_response('ajax.xml', {'ok':False})

def delete(request):
    pk = int(request.POST['pk'])
    Message.objects.get(pk=pk).delete()
    script ="<script> $('#pk%s').slideUp()</script>" % pk
    return HttpResponse(script)
    


class FeedbackViews(BaseView):
    @classmethod
    def feedback(self,request):
        template='feedback.html'
        para=BaseView().para
        para['repeat']=False
        para['messages'] = Message.objects.filter(show=True)[:30]
        if request.method == 'POST':
            form = MessageForm(request.POST)
            para['form']= form
            if form.is_valid():
                content = form.cleaned_data['content']
                name    = form.cleaned_data['name']
                email   = form.cleaned_data['email']
                ip      = request.META['REMOTE_ADDR']
                at      = None
                m       = Message(customer=Customer.objects.get(name=name),content=content,ip=ip,at=at)
                try:
                    if content==para['messages'][0].content:
                        para['repeat']=True
                        return render_to_response(template, para)
                    else:
                        m.save()
                        para['ok']=True
                        return render_to_response(template, para)
                except:
                    para['ok']=True
                    m.save()
                    return render_to_response(template, para)
            else:
                wrong = request.POST
                wrong.name = form['name']
                wrong.email = form['email']
                wrong.content = form['content']
                para['worng'] = wrong
                return render_to_response(template, para)
        else:
            para['form'] = MessageForm()
            return render_to_response(template, para)
