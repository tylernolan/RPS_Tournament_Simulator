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
	def evalPairing(self):
		result = self.p1.evaluate(self.p2)
		if result == "Win":
			self.p1.wins += 1
		elif result == "Loss":
			self.p2.wins += 1
		elif result == "Draw":
			random.shuffle(self.players)
			self.players[0].wins += 1
			
class TournamentSimulator():
	def __init__(self, rocks = 45, papers =45, scissors=10, rounds=10):
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
			
		self.displayResults()
		
	def pairRound(self):
		round = []
		random.shuffle(self.players)
		self.players = sorted(self.players, key= lambda x : x.wins)
		for i in range(0,len(self.players),2):
			round.append(Pairing(self.players[i], self.players[i+1]))
		self.evalRound(round)
		
	def evalRound(self, round):
		for pairing in round:
			pairing.evalPairing()
			
	def generateAverage(self, type):
		total = sum(p.wins for p in self.players if p.name.name == type)
		potential = sum(10 for p in self.players if p.name.name == type)
		average = total / float(potential)
		return average
	def displayResults(self):
		self.players = sorted(self.players, key= lambda x : x.wins)
		for player in self.players:
			print str(player.name.name) + " "+str(player.wins)
		scissorAverage = self.generateAverage("Scissors")
		print scissorAverage
		rockAverage = self.generateAverage("Rock")
		print rockAverage
		paperAverage = self.generateAverage("Paper")
		print paperAverage
TournamentSimulator()