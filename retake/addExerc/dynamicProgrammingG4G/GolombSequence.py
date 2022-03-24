"""
In mathematics, the Golomb sequence is a non-decreasing integer sequence where n-th term is equal to number of times n appears in the sequence.
The first few values are 
1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, ……
Explanation of few terms: 
Third term is 2, note that three appears 2 times. 
Second term is 2, note that two appears 2 times. 
Fourth term is 3, note that four appears 3 times.
Given a positive integer n. The task is to find the first n terms of Golomb sequence. 
"""



def golomb( n ):
    DP = [0] * ( n + 1 )
    DP[1] = 1
    for i in range(2, n + 1):
        DP[i] = 1 + DP[i - DP[i - 1]]
    return DP

print(golomb( 4 ))