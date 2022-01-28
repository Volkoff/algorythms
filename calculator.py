import math
import random


class Calculator:

    bruteForceResults = []
    def boat_brute_force(self,a):
        source = a
        self.PermuteBrute(source, 0, len(source) - 1)
        min = math.inf
        for result in self.bruteForceResults:
            difference = abs(result[0] - result[len(result)-1])
            if difference<min:
                min = difference
                minresult = result
        #print("Full minimum: "+ str(min))


    def PermuteBrute(self, source, l, r):
        if l == r:
            self.bruteForceResults.append(source.copy())
        else:
            for i in range(l, r + 1):
                source[l], source[i] = source[i], source[l]
                self.PermuteBrute(source, l + 1, r)
                source[l], source[i] = source[i], source[l]



#==============================================================MONTE-CARLO===========================
    permutationList = []

    def get_min_diff(self,perm: list) -> list:
        results = [(None, float('inf'))]
        for p in perm:
            odd = 0
            if len(p) % 2 == 0:
                middle = int(len(p) / 2)
            else:
                middle = len(p) // 2
                odd = 1
            sum_l = p[:middle]
            sum_r = p[middle + odd:]
            diff = abs(sum(sum_l) - sum(sum_r))
            if diff < results[0][1]:
                results.clear()
                results.append((p, diff))
            elif diff == results[0][1]:
                results.append((p, diff))
        return results


    def monte_carlo(self,args):
        combinations = random.randint(2, len(args) - 1)
        perm = list()
        input_data = list(args)
        while combinations > 0:
            shuffled_list = list(input_data)
            random.shuffle(input_data)
            if shuffled_list not in perm:
                perm.append(tuple(shuffled_list))
                combinations -= 1
        results = self.get_min_diff(perm)
        return results


#===========================================HEURISTIC==========================================




