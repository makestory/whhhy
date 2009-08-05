#coding=utf-8
from django import forms
from models import Message,Customer

class MessageForm(forms.Form):
    content = forms.CharField(required=False)
    name = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(required=False)
    def clean_content(self):
        content = self.cleaned_data['content'].strip()
        if not content:
            raise forms.ValidationError("留言内容不能为空")
        return content
    
    def clean_name(self):
        name = self.cleaned_data.get('name').strip()
        if name=='':
                name='一个不愿透露姓名的家伙'
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        try:
            name = self.cleaned_data.get('name').strip()
            if name =='一个不愿透露姓名的家伙':
                email='unknow@whhhy.com'
            if email=='':
                raise forms.ValidationError("如果您要留名的话请输入邮箱地址")
        except:
            raise forms.ValidationError("如果您要留名的话请输入邮箱地址")
            return email
        try:
            exist=Customer.objects.filter(name=name)[0]
        except:
            c=Customer(name=name,email=email)
            c.save()
            return email
        if exist.email != email:
            raise forms.ValidationError("邮箱与此用户名不匹配")
            return email
        return email
        
            
  