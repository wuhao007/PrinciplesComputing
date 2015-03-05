"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    line_len = len(line)
    merge_line = line[:]
    line_flag = [False] * line_len

    for ptr_i in range(1, line_len):
        if merge_line != 0:
            ptr_k = ptr_i
            for ptr_j in range(ptr_i - 1, -1, -1):
                if merge_line[ptr_j] == 0:
                    ptr_k = ptr_j
                else:
                    break
            merge_line[ptr_k], merge_line[ptr_i] = merge_line[ptr_i], merge_line[ptr_k]
            if ptr_k > 0 and merge_line[ptr_k] == merge_line[ptr_k - 1] and line_flag[ptr_k - 1] == False:
                merge_line[ptr_k - 1], merge_line[ptr_k] = 2 * merge_line[ptr_k - 1], 0 
                line_flag[ptr_k - 1] = True
    return merge_line

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2])
print merge([8, 16, 16, 8])
