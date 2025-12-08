class Solution(object):
    def judgeCircle(self, moves):
        #moves=moves.lower()
        if moves.count('U')==moves.count('D')and moves.count('L')==moves.count('R'):
            return True
        else:
            return False

        
