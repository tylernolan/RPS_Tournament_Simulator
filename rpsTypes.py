class RPS_Type():
	def __init__(self):
		pass
	def evaluate(self, opp):
		pass
		
class Paper(RPS_Type):	
	def __init__(self):
		self.name = "Paper"
	def evaluate(self, opp):
		if opp.name == "Scissors":
			return "Loss"
		elif opp.name == "Rock":
			return "Win"
		elif opp.name == "Paper":
			return "Draw"
		else:
			raise BaseException("Invalid Result: self.name: {} opp.name: {}".format(self.name, opp.name))
class Scissors(RPS_Type):	
	def __init__(self):
		self.name = "Scissors"
	def evaluate(self, opp):
		if opp.name == "Paper":
			return "Win"
		elif opp.name == "Rock":
			return "Loss"
		elif opp.name == "Scissors":
			return "Draw"
		else:
			raise BaseException("Invalid Result: self.name: {} opp.name: {}".format(self.name, opp.name))
			
class Rock(RPS_Type):
	def __init__(self):
		self.name = "Rock"
	def evaluate(self, opp):
		if opp.name == "Scissors":
			return "Win"
		elif opp.name == "Paper":
			return "Loss"
		elif opp.name == "Rock":
			return "Draw"
		else:
			raise BaseException("Invalid Result: self.name: {} opp.name: {}".format(self.name, opp.name))