# Write your code here
def is_increasing(ns):
    return all(ns[i] <= ns[i+1] for i in range(len(ns)-1))
