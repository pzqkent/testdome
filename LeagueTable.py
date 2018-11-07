
'''
The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 

The player's rank in the league is calculated using the following logic:

The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
If two players are tied on score, then the player who has played the fewest games is ranked higher.
If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.
Implement the player_rank function that returns the player at the given rank.

For example

		table = LeagueTable(['Mike', 'Chris', 'Arnold'])
		table.record_result('Mike', 2)
		table.record_result('Mike', 3)
		table.record_result('Arnold', 5)
		table.record_result('Chris', 5)
		print(table.player_rank(1))

All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".

'''

from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
    	a = list(map(dict,self.standings.values()))
    	# print(sorted(a,key = lambda x: (-x['score'],x['games_played'])))
    	# print(sorted(a,key = lambda x:x['games_played']))
    	# print(self.standings.keys())
    	# print(self.standings.values())
    	key1 = self.standings.keys()
    	value1 = self.standings.values()
    	dic1 = self.standings
    	# c = list(key1).index('Mike')
    	# print(c)
    	b = sorted(key1, key = lambda x: (-dic1[x]['score'],dic1[x]['games_played'],list(key1).index(x)) )
    	# print('b',b)
    	return b[rank - 1]


    	# sorted(self.standings,key=lambda x:x[0])


      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))