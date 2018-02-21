# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Email Regular Expression
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
            
        try:
            name = postData['name']
            desc = postData['desc']

            if len(name) <= 0:
                errors["name"] = "Name cannot be blank!"
            elif len(name) >= 1 and len(name) < 5:
                errors["name"] = "Name must be longer than 5 letters!"

            if len(desc) <= 0:
                errors["desc"] = "Description cannot be blank!"
            elif len(desc) >= 1 and len(desc) < 15:
                errors["desc"] = "Description must be longer than 15 letters!"

        except:
            pass
            
        return errors

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()

    def __str__(self):
        return "\n\tID: {}\n\tName: {}\n\tDescription: {}\n".format(str(self.id), str(self.name), str(self.desc))

    __repr__ = __str__

class Comment(models.Model):
    content = models.TextField()
    commentor = models.ForeignKey(Course, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "\n\tID: {}\n\tComment: {}\n".format(str(self.id), str(self.comment))

    __repr__ = __str__
