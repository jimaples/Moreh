# Create your views here.
from datetime import datetime as dt

from code.Moreh import *
# Imports these objects
# h = HebrewReference()
# qz = Quiz(test=0)
      
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

class Choice(collections.namedtuple('Choice',['idx','a'])):
    pass
    
def makeChoices(options):
    return [ Choice(i, s) for i,s in enumerate(options) ]

class Category(collections.namedtuple('Category',['name','done','idx','progress'])):
    pass
    
def makeCategories():
    categories = []
    for i, s in enumerate(qz.sets):
        set_progress, num_left = qz.progress(s[1])
        categories += [ Category(s[1].name, (set_progress == 100), i, qz.progress(s[1])) ]
    #return [ Category(*tuple([s[1].name]+list(qz.progress(s[1])))) for s in qz.sets ]
    return categories

# TODO: create global response dictionary, update it from the view methods, 
# and use global dictionary in the render_to_response call (use decorator?)
quiz_params = {
    'html':'index.html',
    'now': dt.now(),

    'question': None,
    'choices': makeChoices(['A','B','C','D']),

    'feedback': False,
    'correct': False,
    'previous': None,
    'progress': None,

    'show_cat': True,
    'categories': makeCategories(),

    'show_help': True,
    'q_set': qz.q_set,
    }

def getQuestion():
    q = qz.question()
    if qz.q_set != quiz_params['q_set']:
        quiz_params.update({'feedback': False, 'show_help':True})
    quiz_params.update({'question': q, 'q_set': qz.q_set,
        'choices': makeChoices(q.options)})    

# Get question to start things out
getQuestion()

def render(params={}, request=None):
    params['now'] = dt.now()
    return render_to_response(params['html'], params, context_instance=RequestContext(request))
    
def index(request):
    getQuestion()
    quiz_params.update({'feedback': False})
    return render(quiz_params, request)
	
def answer(request, guess):
    old_q, correct, progress = qz.answer(int(guess))
    quiz_params.update({'feedback': True, 'correct': correct, 'previous': old_q,
        'progress': '{0:2d}%'.format(int(progress)),
        'categories': makeCategories()})
    
    getQuestion()    
    return render(quiz_params, request)

###########################################################

def showCategories(request, showCat):
    quiz_params.update({'show_cat': bool(int(showCat))})
    return render(quiz_params, request)

###########################################################

def showHelp(request, help):
    qz.penalty()
    quiz_params.update({'feedback': False, 'show_help': bool(int(help)), 
        'q_set': qz.q_set, 'categories': makeCategories()})
    return render(quiz_params, request)

###########################################################

def setCategory(request, cat):
    qz.setCategory(int(cat))    

    # get a new question from the selected set
    getQuestion()    

    return showHelp(request, '1')
    
