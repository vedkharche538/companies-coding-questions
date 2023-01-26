"""
Problem Statement:
You are given a set S of N points. Point A dominates point B if Ax>=Bx and Ay>=By.
find the total number of non-empty subsets of S that do not contain two points A and B such that A dominates B. Since the answer may be large return it modulo 10^9+7.

Input Format:
The first line contains an integer,N, denoting the number of elements in X.
Each line i of the N subsequent lines (where 0 <= i < N) contains an integer describing X[i].
Each line i of the N subsequent lines (where 0 <= i < N) contains an integer describing Y[i].

Constraints:
1<=N<=10^5
1<= X[i] <= 10^5
1<= Y[i] <= 10^5

Sample Input
Case1:
2
4
4
3
1

Output: 2
Explanation: N=2 X=[4,4] Y=[3,1] Here points are  {4,3} and {4,1}. We can make two subsets ({4,3}) and ({4,1}). We cannot make the subset ({4,3}, {4,1}) as {4,3} dominates {4,1}.

Case2:
4
1
2
3
4
1
2
3
4

Output: 4
Explanation: N=4 X=[1,2,3,4] Y=[1,2,3,4] Here points are {1,1}, {2,2}, {3,3}, {4,4}.
The only valid sets are the ones with exactly one point. Cause if we take a set of 2 points one will always dominate the other.

Case3:
5
1
3
5
3
2
2
4
3
2
1

Output: 7
Explanation: N=5 X=[1,3,5,3,2] Y=[2,4,3,2,1] Here points are {1,2}, {3,4}, {5,3}, {3,2}, {2,1}.
Now we can form subsets
({1,2}), ({3,4}),
({5,3}), ({3,2}),
({2,1}), ({3,4},{5,3}) and ({1,2},{2,1})
"""


import itertools

# case:1
x = [4, 4]
y = [3, 1]
"""
Approach: 
Here, S = {(4,3), (4,1)}; S1={(4,1)} i.e. S1 is a subset of S.
and S2={(4,3)} i.e. S2 is also subset of S.
Till this point count=2
other subsets would be: {(4,3), (4,1)}, {(4,1), (4,3)} considered all combinations.
Consider Example: {(4,1), (4,3)}
A = (4,1)
B = (4,3)

Here Ax>=Bx and Ay<=By A is not dominating B.

with combinations of same: we have {(4,3), (4,1)} variation where,
A = (4,3)
B = (4,1)
As per the given condition here A is dominating B so we do not want this points to be counted.
so earlier subset which was having same points with different variation also can not be consider.

Hence, our final answer is 2.

"""

# case:2
# x = [1, 2, 3, 4]
# y = [1, 2, 3, 4]
"""
Approach:
Here as per given values S = {(1,1), (2,2), (3,3), (4,4)}
S1 = {(1,1)} i.e. S1 is a subset of S
S2 = {(2,2)} i.e. S2 is also subset of S
S3 = {(3,3)} i.e. S3 is also subset of S
S4 = {(4,4)} i.e. S4 is also subset of S
Current Count is 4;

if we create a all combinations with two points then,
S12 = {(1,1), (2,2)} S22={(2,2), (1,1)}
As per created combination if we consider S22: Ax>=Bx and Ay>=By, condition is verified.
i.e. A is dominating B.
so we do not want to consider these points, as per the condition mentioned in problem statement.
so with points we can not create a subset hence we are not incrementing the counter.
similarly,
for remaining combination one point will always dominate other so we can not create a subset out of it.

Hence, our final answer is 4.


"""

# case:3
# x = [1, 3, 5, 3, 2]
# y = [2, 4, 3, 2, 1]


# creating a points
points = tuple(zip(x, y))
# initializing a counter
counter = 0

# Currently default N value will be our single points sets those will be same irrespective of combinations.
counter = len(points)
# Creating a combinations by specifying a r value 2.
combinations = itertools.combinations(points, 2)
for comb in list(combinations):
    elements = list(itertools.permutations(comb))
    # Here elements contain [((4, 3), (4, 1)), ((4, 1), (4, 3))]
    # We have separated it out for smooth comparision
    x = elements[0]
    y = elements[1]
    # condition which will validate the mention condition if any one of the point is dominating then we are not considering those points as a subset.
    if (x[0][0] < x[1][0] or x[0][1] < x[1][1]) and (
        y[0][0] < y[1][0] or y[0][1] < y[1][1]
    ):
        counter += 1
print(f"Total Subsets: {counter}")
