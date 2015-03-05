"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    lineLen = len(line)
    mergeLine = line[:]
    lineFlag = [False] * lineLen

    for i in range(1, lineLen):
        if mergeLine != 0:
            k = i
            for j in range(i - 1, -1, -1):
                if mergeLine[j] == 0:
                    k = j
                else:
                    break
            mergeLine[k], mergeLine[i] = mergeLine[i], mergeLine[k]
            if k > 0 and mergeLine[k] == mergeLine[k - 1] and lineFlag[k - 1] == False:
                mergeLine[k - 1], mergeLine[k] = 2 * mergeLine[k - 1], 0 
                lineFlag[k - 1] = True
    return mergeLine

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2])
print merge([8, 16, 16, 8])
