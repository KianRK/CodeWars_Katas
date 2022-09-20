def delete_nth(order,max_e):
    order.reverse()         #reversing the list, so that I can simply remove the first element without needing to find the correct index first
    for element in order:
        occur = order.count(element)
        if (occur > max_e):
            for i in range(occur - max_e): #expression in parantheses gives the number of elements that need to be removed
                order.remove(element)
    order.reverse()
    return order

# task description:
# Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].