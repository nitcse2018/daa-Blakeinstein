'''
An implementation of the knapsack problem using the branch and bound algorithm.

Holy.. this was a tough one, and I had to study some cpp code for this, you can find traces of it,
Escpecially with the node structure. I have no concrete Idea about the benefits of using Branch and 
Bound algorithm, but I can say that it resolves the space complexity of the Dynamic Programming approach
Hah! Solving problems with complex code, I doubt anyone can understand this mess anymore but I will try
my best.

Much like the previous approaches, the Algorithm returns the max possible value one can obtain by putting 
items defined by an itemList which is a 2-D array consisting of value and weight of items, in a knapsack 
with a given weight capacity. (Heh redudandant comments, the next level)
'''
from dataclasses import dataclass #Thank god for python libraries, who writes classes for structs anyways?
from copy import deepcopy as copy #append(v) is just a pointer reference to v, i needed to allocate new memory.

#Defining the node struct, representing a tree node, since there was no necessity for storing the entire tree
# as this is not dynamic programming, a way to representing the working node, for better understanding was 
# required.
@dataclass
class node:
    #The level defines current tree depth, cannot exceed total no. of items,
    #value profit margin of the current item.
    #net weight of the current item
    #bounding function for the branch and bound algorithm
    level: int = 0
    value: int = 0
    weight: float = 0
    bound: int = 0

def findBound(node, W, itemList, n):
    
    #return 0 as bound, if current node item weight exceeds required weight
    if node.weight >= W:
        return 0
  
    # initialize bound on value by current value and set weight to current weight
    valueBound, totalWeight = node.value, node.weight
  
    # Start including items after the current node item
    j = 0 # to have the final value of j available in current scope
    for j in range(node.level+1, n):
        #To check if the item being included doesnt exceed weight of knapsack
        if totalWeight + itemList[j][1] > W: 
            break
        #if it can be included, add it and proceed to next item in sequence
        totalWeight += itemList[j][1]
        valueBound += itemList[j][0]
    
    #by now supposed bound is known but if all items werent included, then consider the last skipped item
    # lpartially, to obtain upper bound on value, I really appreciate geeksforgeeks for including this
    if j < n:
        valueBound += (W - totalWeight) * itemList[j][0] /  itemList[j][1]
    # At last return the bound.
    return valueBound

def knapSack(W, itemList, n):  
    # W is the Weight capacity of the knapsack, itemList is a 2-D list of items with value and weights
	# and n is a count for items to be considered from the list, no recursion was used in this algorithm
    # but n was considered anyways for consistency.
    
    # sorting items based on value per weight, in descending order.
    itemList = sorted(itemList, key=lambda x: x[1]/x[0])
    
    # q is the node traversal queue, python has the same data type for stack and queue, list, in a sense.
    q = [node(-1)] #consider dummy node to start.
    
    temp = node() # temporary variable to keep the current node to be appended to the traversal queue

    #Initialize maxValue, to declare its scope
    maxValue = 0
    
    #dequeue the traversal queue, and evaluate the bound on the popped node, until queue is empty
    # This also updates the max expected possible value of the knapsack.
    while q:
        u = q.pop(0) #Dequeue the node from the traversal queue.

        # Iwell we cant proceed to the next node if there isnt any
        if u.level == n-1:
            continue
  
        #set temp to point to next node.
        temp.level = u.level + 1
  
        # we consider, the possibility of adding the next item first
        
        # consider the sum of the current node's and next item's weight and value
        temp.weight = u.weight + itemList[temp.level][1]
        temp.value = u.value + itemList[temp.level][0]
  
        #if current weight is under knapsack capacity and value profit already exceeds the current maxValue
        # update maxValue 
        if temp.weight <= W and temp.value > maxValue:
            maxValue = temp.value

        # Get upper value profit bound to see if traversal of current node will lead to a solution or not
        temp.bound = findBound(temp, W, itemList, n)

        #if the bound comes out to be above current max value profit, there is a chance that it might 
        #  lead to a better solutiom, and as such add it to the traversal queue.
        if temp.bound > maxValue:
            q.append(copy(temp)) #passing temp would only store a reference, to temp and updating 
            #temp would also update the object in the queue, basically a shallow copy would exist
  
        # We now consider, the possibility of not considering the next item, and perform the same
        # procedure.
        
        #the level is incrememented but the weight and value remain same, as the item wasnt included
        temp.weight = u.weight
        temp.value = u.value
        #we find the bound for a possibility of a better answer in this case,
        temp.bound = findBound(temp, W, itemList, n)
        #check if it is possible and add to traversal queue
        if temp.bound > maxValue:          
            q.append(copy(temp))
    #by the end of the loop the maximum possible profit will be known, thus return it
    return maxValue

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