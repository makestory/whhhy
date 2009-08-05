#coding=utf-8
from django.db import models

class Category(models.Model):
    title = models.CharField('名称',max_length=10)
    describe = models.TextField('描述',blank=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __unicode__(self):
        return self.title

class Daily(models.Model):
    "This Model is core unit of the blog "
    date = models.DateField('日期',primary_key=True)
    title = models.CharField('标题',max_length=50,blank=True)
    text = models.TextField('正文',blank=True)
    show = models.BooleanField('显示',default=True)
    count = models.IntegerField('留言数',default=0,editable=False)
    category = models.ForeignKey(Category,verbose_name='分类')

    class Meta:
        ordering = ['-date']
        verbose_name = '日志'
        verbose_name_plural = '日志'
        
    def __unicode__(self):
        return str(self.date)

    def url(self):
        "this method returns url of this daily,the return depend on your url design"
        return '/daily/%s' % str(self.date)
 
