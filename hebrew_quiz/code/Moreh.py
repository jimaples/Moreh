# TODO: Only import what is needed

######################################################################
# Hebrew Language Reference
# The following encodings support Hebrew
# cp424    , EBCDIC-CP-HE, IBM424
# cp856
# cp862    , 862, IBM862
# cp1255   , windows-1255
# iso8859_8, iso-8859-8, hebrew
# utf8, utf16 utf32
######################################################################

from Hebrew import *
from Quizzer import *

h = HebrewReference()
print 'HebrewReference includes', h.__dict__.keys()

cnt = ScaledCounter(0.2, 'gallahad')
q = QuestionSet(zip(h.alephbet, h.a_name),'Hebrew Letter Names')
    
qz = Quiz(test=0)

qz.append(h.alephbet, h.a_name, 'Hebrew Letter Names',
          'Select the name for this character:')

qz.append(h.alephbet, h.a_english,'Hebrew Letter Transliteration',
          'Select the English transliteration for this character:')

alternate = [ (i[0],'First '+i[2]) for i in zip(h.a_first, h.alephbet, h.a_name) if i[0] != i[1] ]
alternate += [ (i[0],'Final '+i[2]) for i in zip(h.a_final, h.alephbet, h.a_name) if i[0] != i[1] ]
alternate, names = zip(*alternate)
qz.append(alternate, names, 'Hebrew Alternate Letter Names',
          'Select the name for this character:')

qz.append([ u'{1:13s}:{0:>4s}'.format(*i) for i in zip(h.vowels, h.v_names) ],
          [ '{0:s} as in {1:s}'.format(*i) for i in zip(h.v_english, h.v_word) ],
          'Hebrew Vowel Pronunciation', 'How do you pronounce this vowel?')

# Vowels

# Lesson 5 Excercises

######################################################################
# Display Functions
######################################################################

def dispNextQuestion(q):
    """dispNextQuestion(q)
    Command-line interface to display a question and check the answer
    q.name    : Question category
    q.prompt  : Question prompt
    q.q       : Question
    q.options : Shuffled answer options
    q.correct : Index of correct answer

    Output the question index
    """
    print '\n'*100
    print q.name+'\n'+'-'*60+'\n'+q.prompt+'\n  '+q.q

    for i, a in enumerate(q.options):
        print str(i+1)+')',a
        
    guess = raw_input('\nEnter the number for the answer: ')
    return str(int(guess)-1)

def dispFeedback(q, correct, progress):
    if correct:
        print '  Correct!'
    else:
        print '  The correct answer is', q.correct

##dispNextQuestion(*qz.question())

def test():
    while True:
        guess = dispNextQuestion(qz.question())
        if guess.isdigit:
            dispFeedback(*qz.answer(int(guess), verbose=True))
        i = raw_input('Press Enter to continue...')
        
