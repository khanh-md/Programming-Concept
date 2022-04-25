# Driver: Khanh Dong (U14837275)
# Navigator: Tess Zitouni(U95647951)
	
# Description: This is the class definition for a question, which include 4 answers, a correct one, and mutator method corresponding
	
# Question class

class Question:
	def __init__(self,question,a1,a2,a3,a4,correct_ans):
		self.triviaquestion = question
		self.ans1 = a1
		self.ans2 = a2
		self.ans3 = a3
		self.ans4 = a4
		self.correct = correct_ans
	def get_correct(self):
		return self.correct
	def __str__(self):
		return "{}\n1. {}\n2. {}\n3. {}\n4. {}".format(self.triviaquestion, self.ans1, self.ans2, self.ans3, self.ans4)
		

	


