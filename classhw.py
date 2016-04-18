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

# Q1 = Question('What is the capital of Alberta?', 'Edmonton')
# Q2 = Question('Who is the author of Python?', 'Guido Van Rossum')

#3. Exam

class Exam(Questions):
	"""Exams look up to Questions for their data"""
	
	def __init__(self, exam_type):
		self.exam_type = exam_type


# {'name':'Midterm',
#  'questions': [

#     {'question':'What is the capital of Alberta?',
#      'correct_answer': 'Edmonton'},

#     {'question': 'Who is the author of Python?',
#      'correct_answer': 'Guido Van Rossum' }

#   ]
# }

# {'name':'Final',
#  'questions': [

#     {'question':"Who is Ubermelon's competition?",
#      'correct_answer': 'Sqysh'},

#     {'question': "What is Balloonicorn's favorite color?",
#      'correct_answer': 'Sparkles'}

#   ]
# }

