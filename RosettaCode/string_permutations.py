from itertools import permutations


def permAlone(string):
    clean_perm = 0
    perms = permutations(string)
    for permutation in list(perms):
        no_repeats = True
        # print(permutation)
        for i in range(len(permutation)-1):
            # print('in loop')
            # print('i=', i)
            if permutation[i]== permutation[i+1]:
                no_repeats = False
            
        if(no_repeats):
            clean_perm = clean_perm + 1


    return clean_perm

print(permAlone('abcdefa'))