#coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from daily.models import Daily
from feedback.models import Message,Customer
from feedback.forms import MessageForm
from base import BaseView

class DailyViews(BaseView):
    
    
    @classmethod
    def latest(cls,request):
        "This method redirect the page to latest daily"
        try:
            date = str(Daily.objects.filter(show=True).all()[0].date)
            return HttpResponseRedirect('/daily/%s' % date)
        except:
            raise Http404

    @classmethod
    def monthly(cls,request,date):
        "show a daily list of a month"
        template = 'monthly.html'
        para = BaseView().para
        year = int(date[0:4])
        month = int(date[5:7])
        para['dailys'] = Daily.objects.filter(date__year=year,date__month=month,show=True)
        return render_to_response(template,para)

    @classmethod
    def daily(cls,request,date):
        "daily detail and form system"
        template ='daily.html'
        para = BaseView().para
        para['repeat'] = False
        para['daily'] = Daily.objects.filter(show=True).get(date=date)
        para['messages'] = para['daily'].message_set.filter(show=True).order_by('date')
        if request.method == 'POST':
            form = MessageForm(request.POST)
            para['form'] = form
            if form.is_valid():
                content = form.cleaned_data['content']
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                ip = request.META['REMOTE_ADDR']
                at = para['daily']
                m = Message(customer=Customer.objects.get(name=name),content=content,ip=ip,at=at)
                try:
                    if content==Message.objects.filter(at=para['daily'])[0].content:
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
