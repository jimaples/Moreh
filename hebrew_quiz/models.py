"""
    hebrew_quiz.models
    ===================

https://developers.google.com/appengine/docs/python/datastore/overview
Limit                                                       Amount
Maximum entity size                                         1 megabyte
Maximum transaction size                                     10 megabytes
Maximum number of index entries for an entity                 20000
Maximum number of bytes in composite indexes for an entity     2 megabytes
"""
from django.db import models
#from google.appengine.ext import db

def update_model(model, d={}):
    # add model parameters based on a dictionary
    # updating models is an inline change
    for k, v in values.iteritems():
        setattr(model, k, v)        

class Question(models.Model):
    #q, a_opt, a_shift = Quiz.question()
    #s_question = db.StringProperty(required=True)
    #sl_answers = db.StringListProperty(required=True)
    #i_rotate   = db.IntegerProperty(required=True)
    s_question = models.CharField(max_length=100)
    sl_answers = models.CharField(max_length=100)
    i_rotate   = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return self.s_question
    
