from search import Problem

class hanoi(Problem):

        def __init__(self):
            super().__init__("111","333")

        def actions(self, state):
            acts = []
            f1 = state.find('1') + 1
            f2 = state.find('2') + 1
            f3 = state.find('3') + 1

            if f1 == 0:
                f1 = float('inf')
            if f2 == 0:
                f2 = float('inf')
            if f3 == 0:
                f3 = float('inf')

            if f1 < f2:
                acts.append((1,2))
            if f1 < f3:
                acts.append((1,3))
            if f2 < f1:
                acts.append((2,1))
            if f3 < f2:
                acts.append((3,2))
            if f3 < f1:
                acts.append((3, 1))

            return acts

        def result(self, state, action):
            i,j = action
            return state[:i-1] + str(j) + state[i:]


def main():
    h = hanoi()
    print(h.initial)
    print(h.goal)
    print(h.actions(h.initial))
    print(h.result(h.initial, (1,3)))

#Entry point
main()