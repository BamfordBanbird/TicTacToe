import random

class CPU:

    def moveSelection(self, gridList):
        while True:

            cpuSelect = random.choice(range(1,9))
            for i in range(3):
                for j in gridList[i]:
                    if j == cpuSelect:
                        print('Computer Player chose '+str(cpuSelect))
                        return cpuSelect
