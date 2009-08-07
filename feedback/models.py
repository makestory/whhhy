#coding=utf-8
from django.db import models
from daily.models import Daily

class Customer(models.Model):
    name = models.CharField('名字',max_length=14,)
    email = models.EmailField()
    date = models.DateField('注册日期',auto_now_add=True)
    class Meta:
        verbose_name = '留言者'
        verbose_name_plural = '留言者'
    def __unicode__(self):
        return self.name
    
  

class Message(models.Model):
    customer = models.ForeignKey(Customer,verbose_name ='留言人')
    content = models.TextField('内容')
    date = models.DateTimeField('日期',auto_now_add=True)
    ip = models.CharField('IP地址',max_length=20)
    reply=models.TextField('回复',blank=True)
    show = models.BooleanField('显示',default=True)
    at = models.ForeignKey(Daily,blank=True,null=True,verbose_name ='关联')
    
    def save(self):
        models.Model.save(self)
        if self.at:
            self.at.count=Message.objects.filter(at=self.at).count()
            self.at.save()
    def delete(self):
        models.Model.delete(self)
        if self.at:
            self.at.count=Message.objects.filter(at=self.at).count()
            self.at.save()
    class Meta:
        ordering=['-date']
        verbose_name = '留言'
        verbose_name_plural = '留言'
    def __unicode__(self):
        return "%s:%s..." % (self.customer.name,self.content[0:30])
