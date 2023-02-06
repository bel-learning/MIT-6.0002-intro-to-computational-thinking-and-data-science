###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Bilguudei
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def rec_search(current, egg_weights, memo, count):
    if(current == 0):
        return 0
    if(current in memo):
        return memo[current]

    min_weight = 1000000
    for weight in egg_weights:
        if(current - weight >= 0):
            min_weight = min(min_weight,rec_search(current-weight, egg_weights, memo, count) + 1)
    
    memo[current] = min_weight
    return memo[current]

def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    print(egg_weights)
    ans = rec_search(target_weight, egg_weights, memo, 0)
    return ans

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print(f"n = {n}")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))