'''
An implementation of the knapsack problem using Dynamic Programming.

This resolves the overlapping subproblems and substructures that was observed in the greedy approach.
However, it adds to the space complexity, by storing the evaluated weights for all cases in the lookup
dictionary. Basically trading space for time.

Much like the greedy approach,the Algorithm returns the max possible value one can obtain by putting 
items defined by an itemList which is a 2-D array consisting of value and weight of items, in a knapsack 
with a given weight capacity.
'''
def knapSack(W, itemList, n): 
	# W is the Weight capacity of the knapsack, itemList is a 2-D list of items with value and weights
	# and n is a count for items to be considered from the list, this decrements to 0 to terminate recursion.
	
    #using a dictionary to avoid using a generator to build the weight table, and have simpler indexing
    k = dict()

    # Build the dictionary from 0 to to the max weight of the knapsack, and updating as necessary, 
    # max value possibilities are evaluated against all possible item counts and knapsack weights
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0:
                # set value to 0 if no items exist, or no weight capacity left.
                # acts like the exit case from the greedy approach.
                k[i,w] = 0

            elif itemList[i-1][1] <= w: 
                # if the current item and be fit into the knapsack, rercurse for the conditions if its included or not.
                k[i,w] = max(itemList[i-1][0] + k[i-1,w-itemList[i-1][1]],  k[i-1,w])

            else: 
                # copy over the previous weight if the current item cant be added to the knapsack, as possible value
                # remains the same.
                k[i,w] = k[i-1,w]
    
    # return the desired  answer, from the dictionary
    return k[n,W]

#Test code
if __name__ == "__main__": 
    # Define List of items as a 2-D array 
    itemList = [
        [30, 10],
        [55, 20],
        [70, 25],
        [90, 35],
        [110, 50],
        [140, 70],
        [200, 100],
    ]
    #print the maximum possible value	
    print (knapSack(350, itemList, len(itemList)))