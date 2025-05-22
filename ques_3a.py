import numpy as np
import random
class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [1,0]
        self.opp_play_styles = [1,1]
        self.points = 1
        self.opp_pts = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        bob_pts = self.opp_pts

        if bob_pts/(bob_pts+self.points)> 15/44:
            return 0
        else:
            return 2
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1,1]
        self.results = [0,1]
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    A_moves = alice.play_move()
    B_moves = bob.play_move()
    # print(A_moves, B_moves)
    pick_result = random.choices([(1, 0), (0.5, 0.5), (0, 1)], weights=payoff_matrix[A_moves][B_moves])[0]
    alice.observe_result(A_moves, B_moves, pick_result[0])
    alice.opp_pts += pick_result[1]
    bob.observe_result(B_moves, A_moves, pick_result[1])
    pass
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.

    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    payoff_matrix = []
    for i in range(0,2):
        temp=[]
        for j in range(0,2):
            temp.append([-1,-1,-1])
        payoff_matrix.append(temp)
    na = alice.points
    nb = bob.points
    payoff_matrix = [[[nb/(na+nb),0,na/(na+nb)],[7/10,0,3/10],[5/11,0,6/11]],[[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],[[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    alice_pts_per_round = [1, 1]

    for _ in range(num_rounds):
        simulate_round(alice, bob,payoff_matrix)
        na = alice.points
        nb = bob.points
        payoff_matrix[0][0]=[nb/(na+nb),0,na/(na+nb)]
        alice_pts_per_round.append(alice.points)
    print(alice.points)
    return alice_pts_per_round



# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    list_of_pts = monte_carlo(num_rounds=10**5)
    # plotting(list_of_pts)