from itertools import permutations
# this does not solve the problem as written... I need to create the permutations
# and use a regular expression to look for repeating characters. Have been unsuccesful
# writing the regular expression


def permAlone(string):
    clean_perm = 0
    perms = permutations(string)
    for permutation in list(perms):
        no_repeats = True
        for i in range(len(permutation)-1):
            if permutation[i]== permutation[i+1]:
                no_repeats = False
            
        if(no_repeats):
            clean_perm = clean_perm + 1


    return clean_perm

print(permAlone('abcdefa'))