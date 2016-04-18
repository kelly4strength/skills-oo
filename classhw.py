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

	def add_question:
		
