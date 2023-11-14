# 3.9
def sum_of_sequences(T):
    return [sum(x) for x in T]

sequences = [[],[4],(1,2),[3,4],(5,6,7)]
sums = sum_of_sequences(sequences)

print("Sumy sekwencji:", sums)

