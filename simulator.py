from rpsTypes import *
import random
class Player():
	def __init__(self, rps):
		self.name = rps
		self.wins = 0
	def evaluate(self, opp):
		result = self.name.evaluate(opp)
		return result
			
	
class Pairing():
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2
		self.players = [self.p1, self.p2]
		self.winner = None
		
	def evalPairing(self):
		result = self.p1.evaluate(self.p2.name)
		if result == "Win":
			self.p1.wins += 1
			self.winner = self.p1
		elif result == "Loss":
			self.p2.wins += 1
			self.winner = self.p2
		elif result == "Draw":
			random.shuffle(self.players)
			self.players[0].wins += 1
			self.winner = self.players[0]
		else:
			raise BaseException("invalid result: result: {}, p2.name: {}, p1.name: {}".format(result, p2.name, p1.name))
	def __str__(self):
		return "{}  {} vs {}  {} Winner: {}".format(self.p1.name.name, self.p1.wins, self.p2.name.name, self.p2.wins, self.winner.name.name)

		
class TournamentSimulator():
	def __init__(self, rocks, papers, scissors, rounds):
		self.players = []
		self.rounds = rounds
		self.rocks = rocks
		self.papers = papers
		self.scissors = scissors
		for i in range(rocks):
			self.players.append(Player(Rock()))
		for i in range(papers):
			self.players.append(Player(Paper()))
		for i in range(scissors):
			self.players.append(Player(Scissors()))
			
		for i in range(rounds):
			self.pairRound()
			
		
	def pairRound(self):
		round = []
		random.shuffle(self.players)
		self.players = sorted(self.players, key= lambda x : x.wins)
		for i in range(0,len(self.players),2):
			round.append(Pairing(self.players[i], self.players[i+1]))
		self.evalRound(round)
		
	def evalRound(self, round, printPairings = False):
		for pairing in round:
			pairing.evalPairing()
			if printPairings:
				print pairing
			
	def generateAverage(self, type):
		total = sum(p.wins for p in self.players if p.name.name == type)
		potential = sum(self.rounds for p in self.players if p.name.name == type)
		try:
			average = total / float(potential)
		except:
			average = 0
		return average
		
	def getResults(self):
		rockAverage = self.generateAverage("Rock")
		paperAverage = self.generateAverage("Paper")
		scissorAverage = self.generateAverage("Scissors")
		return [rockAverage, paperAverage, scissorAverage]
		
	def displayResults(self, printFinalStandings = False):
		self.players = sorted(self.players, key= lambda x : x.wins)
		if printFinalStandings:
			for player in self.players:
				print str(player.name.name) + " "+str(player.wins)
		rockAverage, paperAverage, scissorAverage = self.getResults()
		print "Rock Average: " + str(rockAverage)
		print "Paper Average: " + str(paperAverage)
		print "Scissor Average: "+ str(scissorAverage)
		
		
		
class MultipleTournamentSimulator():
	def __init__(self, rocks = 450, papers =450, scissors=100, rounds=10, iterations = 25):
		self.rockWinRate = []
		self.paperWinRate = []
		self.scissorWinRate = []
		self.iterations = iterations
		for i in range(iterations):
			ts = TournamentSimulator(rocks, papers, scissors, rounds)
			results = ts.getResults()
			self.rockWinRate.append(results[0])
			self.paperWinRate.append(results[1])
			self.scissorWinRate.append(results[2])
			
	def displayResults(self):
		print "Averages Over {} tournaments: ".format(self.iterations)
		rockAverage = sum(self.rockWinRate) / self.iterations
		paperAverage = sum(self.paperWinRate) / self.iterations
		scissorAverage = sum(self.scissorWinRate) / self.iterations
		print "Rock Win Rate: " + str(rockAverage)
		print "Paper Win Rate: " + str(paperAverage)
		print "Scissor Win Rate: " + str(scissorAverage)
ts = MultipleTournamentSimulator()
ts.displayResults()