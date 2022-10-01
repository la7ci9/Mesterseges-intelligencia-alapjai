from search import *

class NQueen(Problem):

    def __init__(self, N):
        #super().__init__([0] * N + [1])
        super().__init__([0,0,0,0,1])
        self.N = N

    def actions(self, state):
        acts = []
        for m in range(1,self.N + 1):
            prerequisites = True
            for j in range(1,state[-1]):
                if m == state[j - 1] or abs(state[j - 1] - m) == abs(state[-1] - j):
                    prerequisites = False
            if prerequisites:
                acts.append(m)
        return acts

    def result(self, state, action):
        new_state = list(state)
        new_state[new_state[-1] - 1] = action
        new_state[-1] += 1
        return new_state

    def goal_test(self, state):
        if state[-1] == self.N + 1:
            return True
        return False

    def value(self, state):
        n_conflict = 0
        for i in range(state[-1] - 1):
            for j in range(i + 1, state[-1]):
                if state[j] != 0 and (state[i] == state[j] or abs(state[j] - state[i]) == abs(i - j)):
                    n_conflict += 1
        return n_conflict



n_queen = NQueen(4)
for i in range(30):
    print(Hill_Climbing(n_queen))