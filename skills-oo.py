#1. Students
class Students(object):
    """Initialize Student attributes"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

#2. Questions

class Questions(object):
    """class for storing question and answer data"""
    
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        
#Midterm
# Q1 = Question('What is the capital of Alberta?', 'Edmonton')
# Q2 = Question('Who is the author of Python?', 'Guido Van Rossum')
#Final
# Q3 = Question("Who is Ubermelon's competition?", 'Squysh')
# Q4 = Question("What is Balloonicorn's favorite color?", Sparkles')

#3. Exam

class Exam(object):
    """Exams look up to Questions for their data"""
    
    def __init__(self, exam_type):
        #Your __init__ function should take a name for the exam as a parameter
        self.exam_type = exam_type
        #How do I initialize an attribute?initialize the questions attribute 
        #as an empty list in the body__init__ function
        self.questions = []


#Part 3 METHODS
add a method to the Exam class which take a question and a correct_answer
    def add_question(question, correct_answer):
        makes a Question from these?


        exam = Exam('midterm')
        exam.add_question(
            'What is the method for adding an element to a set?'
            '.add()')

2 - Add a method to the Question class that prints the question to the console 
and prompts the user for an answer.

It should return True or False depending on whether the correct answer matches the user's answer.

for example
question = Question('What is the method for adding an element to a set?'
            '.add()')
question.ask_and_evaluate()
What is the method for adding an element to a set? > .add()
True


3- Add a method to the Exam class which administers all of the exam's '
questions and returns the user's score at the end.'
S building on ou code from problem 2, here's how the Exam class shoud work:'