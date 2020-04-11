'''
An implementation of the knapsack problem using the greedy algortihm.

As one might observe, max value with an item is sometimes evaluated multiple times.
The overlapping subproblems and substructures will be resolved in the Dynamic Programming Objective.

The Algorithm returns the max possible value one can obtain by putting items defined by an itemList
which is a 2-D array consisting of value and weight((I had given dictionary a thought but realized
I was too lazy), in a knapsack with a given weight capacity.
'''
def knapSack(W, itemList, n): 
	# W is the Weight capacity of the knapsack, itemList is a 2-D list of items with value and weights
	# and n is a count for items to be considered from the list, this decrements to 0 to terminate recursion.
	# Best case, to exit recursion.
	if n == 0 or W == 0 : 
		return 0

	#If the nth item cannot be fit in the knapsack as it may exceed weight, skip it
	if (itemList[n-1][1] > W): 
		return knapSack(W, itemList, n-1) 

	#since the nth item can be fit, check weight by inclucding it, and by not including it, and return maximum
	# of both the cases. Both cases recurse to check if the item before it can be included or not to yield max
	# value from the knapsack capacity, 
	else: 
		return max(itemList[n-1][0] + knapSack(W-itemList[n-1][1], itemList, n-1), 
				knapSack(W, itemList, n-1)) 

if __name__ == "__main__": 
	itemList = [
		[30, 10],
		[55, 20],
		[70, 25],
		[90, 35],
		[110, 50],
		[140, 70],
		[200, 100],
		]
	print (knapSack(350, itemList, len(itemList))
