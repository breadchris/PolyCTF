import sys, random

ROCK = 100
PAPER = 101
SCISSORS = 102
toss_choices = {"r": ROCK, "p": PAPER, "s": SCISSORS}
toss_choices_swapped = {n: t for t, n in toss_choices.items()}

WIN = 1
LOSE = 2
TIE = 3
BAD_INPUT = 4

class AI():

    def __init__(self):
        self.history = []
        self.rng = random.SystemRandom()

    def run_round(self, player_toss):
        if toss_choices.has_key(player_toss):
            player_toss = toss_choices[player_toss]
            if len(self.history) < 10: # Computer picks randomly until it has enough data to start making decisions
                computer_toss = self.rng.choice(toss_choices.values())
            else:
                computer_toss = self.smart_choose_user_next_input()
            self.history.append(player_toss) # Add player_toss to history after computer decides
            result = self.check_round(player_toss, computer_toss)
            return result
        else:
            return False

    def check_round(self, player_toss, computer_toss):
        if __name__ == "__main__":
            sys.stdout.write("The computer tossed " + toss_choices_swapped[computer_toss] + "! ")
        if player_toss == computer_toss:
            return TIE
        elif player_toss == ROCK:
            if computer_toss == SCISSORS:
                return WIN
            elif computer_toss == PAPER:
                return LOSE
        elif player_toss == PAPER:
            if computer_toss == ROCK:
                return WIN
            elif computer_toss == SCISSORS:
                return LOSE
        elif player_toss == SCISSORS:
            if computer_toss == PAPER:
                return WIN
            elif computer_toss == ROCK:
                return LOSE
        else:
            return BAD_INPUT
        return result

    def choose_best(self, scores):
        if scores[ROCK] == 0 and scores[PAPER] == 0 and scores[SCISSORS] == 0:
            return False
        choices = []
        max_score = max(scores.values())
        for choice in scores.keys():
            if scores[choice] == max_score:
                choices.append(choice)
                #break # This means that only one choice would be in the list <-- use it to exploit the ai's scoring system
        player_next_toss = self.rng.choice(choices)
        if player_next_toss == ROCK:
            return PAPER
        elif player_next_toss == PAPER:
            return SCISSORS
        elif player_next_toss == SCISSORS:
            return ROCK

    def smart_choose_user_next_input(self):
        scores = {ROCK: 0, PAPER: 0, SCISSORS: 0}
        history_length = len(self.history)

        length = 4
        i = len(self.history) - length
        while i >= length-1:
            if (self.history[i] == self.history[history_length-1]):
                if (self.history[i-1] == self.history[history_length-2]):
                    if (self.history[i-2] == self.history[history_length-3]):
                        if (self.history[i-3] == self.history[history_length-4]):
                            scores[self.history[i+1]] += 1
            i -= 1
        best = self.choose_best(scores)
        if best:
            return best

        scores = {ROCK: 0, PAPER: 0, SCISSORS: 0}
        length = 3
        i = len(self.history) - length
        while i >= length-1:
            if (self.history[i] == self.history[history_length-1]):
                if (self.history[i-1] == self.history[history_length-2]):
                    if (self.history[i-2] == self.history[history_length-3]):
                        scores[self.history[i+1]] += 1
            i -= 1
        best = self.choose_best(scores)
        if best:
            return best

        scores = {ROCK: 0, PAPER: 0, SCISSORS: 0}
        length = 2
        i = len(self.history) - length
        while i >= length-1:
            if (self.history[i] == self.history[history_length-1]):
                if (self.history[i-1] == self.history[history_length-2]):
                        scores[self.history[i+1]] += 1
            i -= 1
        best = self.choose_best(scores)
        if best:
            return best
        
        return toss_choices.values()[0] # If history doesn't match, use ROCK

if __name__ == "__main__":
    ai = AI()
    stats = {"win": 0, "lose": 0, "tie": 0}
    turns = 1
    while True:
        player_toss = raw_input(str(stats) + " - Round " + str(turns) + " - Choose (r)ock, (p)aper, or (s)cissors > ").strip()
        result = ai.run_round(player_toss)
        if result == False:
            print "Bad Input!"
            continue
        elif result == WIN:
            stats["win"] += 1
            print "Win!"
        elif result == LOSE:
            stats["lose"] += 1
            print "Lose!"
        elif result == TIE:
            stats["tie"] += 1
            print "Tie!"
        turns += 1
