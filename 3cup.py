from search import *

class Cup3(Problem):

    def __init__(self):
        super().__init__((5,0,0),[(4,1,0),(4,0,1)])

    def actions(self, state):
        s1, s2, s3 = state
        acts = []

        if s1 > 0 and s2 <3:
            acts.append('operator_1-2')
        if s1 > 0 and s3 <2:
            acts.append('operator_1-3')
        if s2 > 0 and s1 <5:
            acts.append('operator_2-1')
        if s2 > 0 and s3 <2:
            acts.append('operator_2-3')
        if s3 > 0 and s1 <5:
            acts.append('operator_3-1')
        if s3 > 0 and s2 <3:
            acts.append('operator_3-2')

        return acts

    def result(self, state, action):
        s1, s2, s3 = state

        if action == 'operator_1-2':
            m = min(s1,3 -s2)
            return (s1 - m, s2 + m, s3)
        if action == 'operator_1-3':
            m = min(s1, 2 - s3)
            return (s1 - m, s2, s3 + m)
        if action == 'operator_2-3':
            m = min(s2, 2 - s3)
            return (s1, s2 - m, s3 + m)
        if action == 'operator_2-1':
            m = min(s2, 5 - s1)
            return (s1 + m, s2 - m, s3)
        if action == 'operator_3-1':
            m = min(s3, 5 - s1)
            return (s1 + m, s2, s3 - m)
        if action == 'operator_3-2':
            m = min(s3, 3 - s2)
            return (s1, s2 + m, s3 - m)


def main():
    c = Cup3()
    print(c.initial)
    print(c.goal)
    print(c.actions(c.initial))
    print(c.result(c.initial, 'operator_1-3'))

#Entry point
main()