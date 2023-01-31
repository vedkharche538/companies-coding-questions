"""
N friends play a game. In each turn of the game, you create a random permutation P with length N, and every player I will take the element Pi and sum it up to his total score.

You are given an array S of length N where S[i] is total score of the ith friend after K turns. Find the value of K.
Input Format:
The first line contains an integer, N denoting the number of players. Each line I of the N subsequent lines (where 0<=i<N) contains an integer describing S[i].

Test Cases:
Sample Input	Sample Output	Explanation
3
4
4
4	2	N=3 S= [4,4,4] K=2 since 1st turn=> P=1 2 3 
2nd turn=>P=3 2 1 So the sum of each player is: 1+3,2+2,3+1 => 4 4 4. Note that P can be changed in the game, but the number of turns is constant.
3
7
5
6	3	N=3 S= [7,5,6] K=3 since 1st turn=> P=3 1 2 
2nd turn=>P=1 2 3 3rd turn=>P=3 2 1. So the sum of each player is: 3+1+3, 1+2+2, 2+3+1 =>7 5 6.
5
5
10
15
20
25	5	Same explanation as above

"""
def find_turns(S:list, N:int):
    total_sum=0
    for num in S:
      total_sum += num
    total_div=0
    while N>0:
      total_div+=N
      N-=1
    return total_sum//total_div
  
if __main__ == "__name__":
  output = find_turns([4,4,4], 3)
  print(f"Total number of turns taken: {output}")
