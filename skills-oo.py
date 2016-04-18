Part 2: Classes and Init Methods

Directions: Make Python classes that could store the each of the 
following three pieces of data. 

Use the dictionaries below as examples to guide you in 
creating class definitions for the following objects. 

Define an __init__ method to allow callers of this class to provide 
initial values for each attribute.

Student

class Students(object):
    """Initialize Student attributes"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        
 Write a class that can store data like this:

{'first_name': 'Jasmine',
 'last_name': 'Debugger',
 'address': '0101 Computer Street'}

{'first_name': 'Jaqui',
 'last_name': 'Console',
 'address': '888 Binary Ave'}

Question
Questions are a question & a correct answer; 
here are two example questions. 

Write a class that could store data like this:


class Question(object):
pass

{'question': 'What is the capital of Alberta?',
 'correct_answer': 'Edmonton'}

{'question': 'Who is the author of Python?',
 'correct_answer': 'Guido Van Rossum'}

Exam
Notice that an Exam should have an attribute called questions. 
Simply initialize the questions attribute as an empty list in 
the body __init__ function. 

We’ll deal with adding questions to the exam later on in this assignment. 

Your __init__ function should take a name for the exam as a parameter.

A Note on Attributes
Though we’ve mainly seen attributes that are strings or integers, 
remember: attributes can also be lists, and many other data types. 

In the case of our questions attribute, we’ll have a list of Question objects.

For example, here are two exams. Make a class that could store data like this:

class Exams(object):
    pass

{'name':'Midterm',
 'questions': [

    {'question':'What is the capital of Alberta?',
     'correct_answer': 'Edmonton'},

    {'question': 'Who is the author of Python?',
     'correct_answer': 'Guido Van Rossum' }

  ]
}

{'name':'Final',
 'questions': [

    {'question':"Who is Ubermelon's competition?",
     'correct_answer': 'Sqysh'},

    {'question': "What is Balloonicorn's favorite color?",
     'correct_answer': 'Sparkles'}

  ]
}
