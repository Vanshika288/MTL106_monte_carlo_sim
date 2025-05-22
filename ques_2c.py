import numpy as np
import random


class Alice:
    def __init__(self):
        self.past_play_styles = [1, 1]
        self.results = [1, 0]
        self.opp_play_styles = [1, 1]
        self.points = 1
        self.opp_points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.

        Returns:
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 0:
            #     prev match was a bob win
            return 1
        elif self.results[-1] == 0.5:
            return 0
        else:
            # self.past_play_styles = np.append(self.past_play_styles,0)
            nb = self.opp_points
            na = self.points
            attack_prb = nb / (na + nb)
            if attack_prb > 6 / 11:
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


class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1, 1]
        self.results = [0, 1]
        self.opp_play_styles = [1, 1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:
            return 0

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
    pick_result = random.choices([(1, 0), (0.5, 0.5), (0, 1)], weights=payoff_matrix[A_moves][B_moves])[0]
    alice.observe_result(A_moves, B_moves, pick_result[0])
    alice.opp_points += pick_result[1]
    bob.observe_result(B_moves, A_moves, pick_result[1])




# Run Monte Carlo simulation with a specified number of rounds
def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    cnt = 0
    alice = Alice()
    bob = Bob()
    alice_win =1
    prev_pt = 1
    no_of_rounds = 2
    na = alice.points
    nb = bob.points
    sum_round = 0
    no_of_matches  = 0
    payoff_matrix = [[[nb/(na+nb),0,na/(na+nb)],[7/10,0,3/10],[5/11,0,6/11]],[[3/10,0,7/10],[1/3,1/3,1/3],[3/10,1/2,1/5]],[[6/11,0,5/11],[1/5,1/2,3/10],[1/10,4/5,1/10]]]
    while cnt<(10**5):
        if alice_win==T:
            sum_round += no_of_rounds
            no_of_matches += 1
            no_of_rounds = 2
            alice = Alice()
            bob = Bob()
            prev_pt = 1
            alice_win = 1
        na=alice.points
        nb=bob.points
        payoff_matrix[0][0]=[nb/(na+nb),0,na/(na+nb)]
        simulate_round(alice,bob,payoff_matrix)
        no_of_rounds +=1
        if alice.points==prev_pt+1:
            alice_win +=1
        prev_pt = alice.points
        
        cnt += 1

    return sum_round/no_of_matches



# Run Monte Carlo simulation with a specified number of rounds
