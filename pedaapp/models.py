from django.db import models

class Curriculum(models.Model):
  name = models.CharField(max_length=200)

class Chapter(models.Model):
  name = models.CharField(max_length=200)
  curric = models.ForeignKey(Curriculum)

class Module(models.Model):
  name = models.CharField(max_length=200)
  chapter = models.ForeignKey(Chapter)

class Item(models.Model):
  name = models.CharField(max_length=200)
  modules = models.ManyToManyField(Module)

class Clazz(models.Model):
  name = models.CharField(max_length=200)
  curric = models.ForeignKey(Curriculum)

class Student(models.Model):
  name = models.CharField(max_length=200)
  clazzes = models.ManyToManyField(Clazz)

class AssessmentField(models.CharField):
  CORRECT = 'c'
  INCORRECT = 'i'
  UNCOMPILABLE = 'u'
  VALUES = (
    (CORRECT, 'correct'),
    (INCORRECT, 'incorrect'),
    (UNCOMPILABLE, 'uncompilable')
  )

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 1
    kwargs['choices'] = self.VALUES
    super(AssessmentField, self).__init__(*args, **kwargs)

class Attempt(models.Model):
  start = models.DateTimeField()
  stop = models.DateTimeField()
  student = models.ForeignKey(Student)
  clazz = models.ForeignKey(Clazz)
  item = models.ForeignKey(Item)
  data = models.TextField()
  assessment = AssessmentField()

class KC(models.Model):
  name = models.CharField(max_length=200)
  items = models.ManyToManyField(Item)

