class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        cnt=0
        players.sort()
        trainers.sort()
        i=j=0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                cnt+=1
                i+=1
            j+=1
        return cnt