
'''
In a list of tuples. The task is to extract all tuples which have all elements divisible by K.
Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6 
Output : [(6, 24, 12), (60, 12, 6)] 
Input : test_list = [(6, 24, 12), (60, 10, 5), (12, 18, 21)], K = 5 
Output : [(60, 10, 5)]

'''

def extract(t1: tuple, k:int) -> list:
    ls = []
    for t in t1:
        for ele in t:
            if ele%k != 0:
                break
        else:
            ls.append(t)
    return ls

t1 = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
k1 = 6

t2 = [(6, 24, 12), (60, 10, 5), (12, 18, 21)]
k2 = 5

print(f"output1: {extract(t1,k1)}")

print(f"output2: {extract(t2,k2)}")