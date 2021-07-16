from django.db import models

class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100, null=True, blank=True)
    age = models.IntegerField('年齢')
    job = models.CharField('仕事', max_length=100, null=True, blank=True)
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='image', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='image', verbose_name='サブ画像')
    
    def __str__(self) -> str:
        return self.name
    

class Work(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    skill = models.CharField('スキル', max_length=100)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateTimeField('作成日時')
    description = models.TextField('説明')
    
    def __str__(self):
        return self.title 
    
    
class Experience(models.Model):
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)
    
    def __str__(self):
        return self.occupation
    
    
class Skill(models.Model):
    name = models.CharField('スキル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')
    
    def __str__(self):
        return self.name