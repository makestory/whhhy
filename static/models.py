#coding=utf-8
from django.db import models

class Wallpaper(models.Model):
    image = models.ImageField('图片',upload_to='wallpaper')
    number = models.IntegerField('编号')
    
    def __unicode__(self):
        return str(self.image
                   )
    class Meta:
        ordering = ['number']
        verbose_name = '墙纸'
        verbose_name_plural = '墙纸'

class File(models.Model):
    
    data = models.FileField('文件',upload_to='static')
    describe = models.CharField('描述',max_length=20)
    
    def __unicode__(self):
        return str(self.describe
                   )
    def url(self):
        return "data/static/%s" % self.data.url
        
    class Meta:
        verbose_name = '静态文件'
        verbose_name_plural = '静态文件'
