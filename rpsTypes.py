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
		else:
			return "Draw"
class Scissors(RPS_Type):	
	def __init__(self):
		self.name = "Scissors"
	def evaluate(self, opp):
		if opp.name == "Paper":
			return "Win"
		elif opp.name == "Rock":
			return "Loss"
		else:
			return "Draw"
			
class Rock(RPS_Type):
	def __init__(self):
		self.name = "Rock"
	def evaluate(self, opp):
		if opp.name == "Scissors":
			return "Win"
		elif opp.name == "Paper":
			return "Loss"
		else:
			return "Draw"