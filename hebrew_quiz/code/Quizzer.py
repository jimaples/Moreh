import random
import collections
from copy import copy
# TODO: Only import what is needed

class ScaledCounter(collections.Counter):
    # Update collections.Counter to simplify scaling all values for feedback systems
    def __init__(self, threshold=0, iterable=[]):
        collections.Counter.__init__(self, iterable)
        self.threshold = threshold

    def __mul__(self, gain=1, replace=False):
        # figure out the minimum value that won't cross the threshold
        limit = self.threshold/gain
        
        if replace:
            for k in self.keys():
                if self[k] >= limit:
                    self[k] *= gain
                else:
                    del self[k]
        else:
            # create a new instance with scaled values
            new = dict([ (k, self[k]*gain) for k in self.keys() if self[k] >= limit ])
            return ScaledCounter(self.threshold, new)

    # TODO: Add __radd__ method to allow sum?
    
    def __repr__(self):
        return 'ScaledCounter('+str(self.threshold)+','+str(dict(self))+')'


class Question(collections.namedtuple('Question',['q','a','responses','weights'])):
    """Question(q, a, responses, weights)
    Create namedtuple class for memory efficiency
    .q = Question
    .a = Answer
    .responses = data structure for storing how the user has responded
    .weights   = data structure for storing weighting metrics
    """
    pass

    #To do: move the ScaledCounter() to initialize 
    #def __new__(self, q='question', a='answer', responses=ScaledCounter(), weights=ScaledCounter()):
    #    super(Question, self).__new__(self, q, a, responses, weights)


class QuestionSet():
    # Data structure for a related set of questions
    def __init__(self, qa_tuple_list=[], name='unknown',
                 prompt='Select the answer related to the following:'):
        self.quiz = tuple([ Question(i[0], i[1], ScaledCounter(), ScaledCounter()) for i in qa_tuple_list ])
        #self.quiz = tuple([ Question(i[0], i[1]) for i in qa_tuple_list ])
        self.name = name
        self.prompt = prompt

    def __getitem__(self, index=0):
        # Allow instances to be sliced to get at specific questions
        #selected = copy(self.quiz[index])
        selected = self.quiz[index]

        # Add set name and prompt to the question (to try to limit memory)
        if type(selected) == tuple:
            for i in selected:
                i.name = self.name
                i.prompt = self.prompt
        else: # single item
            selected.name = self.name
            selected.prompt = self.prompt
            
        return selected

    def __len__(self):
        # Return the number of questions in the set
        return len(self.quiz)

    def __repr__(self):
        return '{0:s} quiz ({1:d} questions)'.format(self.name, len(self.quiz))

    def cheat(self):
        # Show the mapping of questions to answers
        q,a = zip(*[ (i.q,i.a) for i in self.quiz ])
        # Get the length of the longest question for formatting
        max_q = max(len(i) for i in q)
        # Return a string of the results
        s=u'{0:>'+str(max_q)+'s} = {1:s}'
        return '\n'.join([ s.format(*i) for i in zip(q,a) ])


class Quiz():
    # Determine questions for one or more QuestionSet instances
    def __init__(self, test=0):
        self.sets = []
        self.difficulty = 0

        # For integration, limit the number of questions in each set
        self.test = test

        # Question references
        self.q_active = Question('Q', 'A', ScaledCounter(), ScaledCounter())        
        self.q_set = []

        # negative feedback loop parameters
        # new = (old + .increment (if correct)) * .scale
        self.delete = 0.03
        self.scale = 0.6
        self.increment = 0.85
        self.mastered  = 1.1

    def append(self, questions=[], answers=[], name='Unknown',
               prompt='Select the answer related to the following:'):
        # For now, give each set a unique difficulty so sets don't get mixed together
        difficulty = len(self.sets)
        self.sets += [ (difficulty, QuestionSet(zip(questions, answers), name, prompt)) ]
        # set the threshold for deleting old answers
        self.sets[-1][1].threshold = self.delete
        # set the active set
        if len(self.q_set) == 0:
            self.q_set = self.sets[-1][1]

    def question(self):
        if self.sets:
            # Build question pool (all_q) and count how many sets of questions are being used
            self.q_set = []
            if self.test:
                num_sets = len([ self.q_set.extend(i[1][:self.test]) for i in self.sets if i[0] == self.difficulty ])
            else:
                num_sets = len([ self.q_set.extend(i[1]) for i in self.sets if i[0] == self.difficulty ])
            
            # Remove questions that have been asked recently
            recent = [ self.q_active ]
            # Remove questions the user has mastered
            pool = [ i for i in self.q_set if (i.weights[i.a] < self.mastered) and (i not in recent) ]

            # Assign probability weights to each option, pick randomly based on cumulative sum
            # For now, just pick randomly
            if pool: # Pick questions
                q_opt = random.sample(pool, 1)
            else:                
                q_opt = random.sample(self.q_set, 1)

            def validQuestion(q):
                if q in q_opt:
                    return False;
                elif q.a in [ i.a for i in q_opt ]:
                    return False
                return True

            # Assign probability weights to each option, pick randomly based on cumulative sum
            # For now, just pick randomly
            for j in range(3):
                # select answers out of remaining questions
                a_pool = [ i for i in pool if validQuestion(i) ]
                
                if len(a_pool) == 0: # no unique answers left!
                    a_pool = [ i for i in self.q_set if validQuestion(i) ]

                if a_pool: # don't sample an empty set
                    q_opt += random.sample(a_pool, 1)
                
            # Placeholder to check type of answer
            # strings -> multiple choice
            # bool    -> True/False

            # Set the active question
            #self.q_active = copy(q_opt[0])
            self.q_active = q_opt[0]

            # Output question and answer options
            self.q_active.correct = random.randint(1, len(q_opt))-1
            self.q_active.options = collections.deque([ j.a for j in q_opt ])
            self.q_active.options.rotate(self.q_active.correct-1)
            self.q_active.options = tuple(self.q_active.options)
            return self.q_active
        
        else: # No question sets loaded!
            q_mc = Question('Question', 'Answer 0', ScaledCounter(), ScaledCounter())
            q_mc.correct = 1
            q_mc.options = tuple(['Answer '+str(i) for i in range(4)])
            return q_mc

    def penalty(self):
        # decrease weighting on all answers when user "cheats"
        self.q_active.weights.__mul__(self.scale, True)        

    def answer(self, guess=0, verbose=False):
        # update question set with answer results
        a_correct = self.q_active.a

        if 'options' in self.q_active.__dict__.keys():
            a_user = self.q_active.options[guess]
            correct = (a_user == a_correct)

            self.q_active.responses[a_user] += 1
            
            self.q_active.weights[a_user] += self.increment
            self.q_active.weights.__mul__(self.scale, True)
        else: # Something got out of sync
            correct = False

        # Check set progress
        set_progress, num_mastered = self.progress()

        if verbose: # TODO move to seperate function                
            print u'"{4:s}" -> "{1:s}" at {2:d}% {3:d}/{0:d}'.format(
                sum(self.q_active.responses.itervalues()),
                a_user,
                min(100,int(self.q_active.weights[a_correct]*100.0/self.mastered)),
                self.q_active.responses[a_correct],
                self.q_active.q)

            # Figure out overall progress
            print 'Question set at {0:d}% ({1:d} questions remaining)'.format(
                set_progress, num_mastered)

        if set_progress == 100:
            # Update the difficulty
            new = [ i[0] for i in self.sets if i[0] > self.difficulty ]
            if new: # If there are any higher difficulty levels...
                self.difficulty = min(new)

                # TODO show "cheat screen" to review material before starting next set
                #set_progress = 0

        return self.q_active, correct, set_progress

    def progress(self, q_set=None):
        '''Report progress of active or specified QuestionSet'''
        if q_set == None:
            # Report progress of active set
            q_set = self.q_set
        #print "q_set : ",len(q_set),
        if self.test > 0:
            q_set = q_set[:self.test]
            #print '->',len(q_set)
                
        pool = [ min(self.mastered,i.weights[i.a]) for i in q_set ]
        set_progress = int(100.0*sum(pool)/len(pool)/self.mastered+0.01)
        num_left = len([ i for i in pool if i < self.mastered ])

        return set_progress, num_left

    def setCategory(self, setIdx):
        self.difficulty = self.sets[setIdx][0]

    def cheat(self):
        # Show the mapping of questions to answers
        q,a = zip(*[ (i.q,i.a) for i in self.q_set ])
        # Get the length of the longest question for formatting
        max_q = max(len(i) for i in q)
        # Return a string of the results
        s=u'{0:>'+str(max_q)+'s} = {1:s}'
        return '\n'.join([ s.format(*i) for i in zip(q,a) ])

    
if __name__ == '__main__':
    from Hebrew import *

    cnt = ScaledCounter(0.2, 'gallahad')

    h = HebrewReference()
    q = QuestionSet(zip(h.alephbet, h.a_name),'Hebrew Letter Names')
   
    qz = Quiz(test=5)
    qz.append(h.alephbet, h.a_name, 'Hebrew Letter Names',
              'Select the name for this character:')

    qz.append(h.alephbet, h.a_english,'Hebrew Letter Transliteration',
              'Select the English transliteration for this character:')

    from Moreh import test


