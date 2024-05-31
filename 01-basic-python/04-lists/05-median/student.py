# Write your code here
def median(ns):
    ns.sort()
    index = len(ns)//2
    if len(ns) % 2 == 0:
        return (ns[index-1] + ns[index]) / 2
    else:
        return ns[index]