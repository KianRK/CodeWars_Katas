#At first I did not like this Kata, because instructions and expexted return
#respectively output have not been clear in my opinion.
# But it taught me the string.center() method I did not know before.
#below I used the center() method and commented out my previous solution for comparison.
#Im aware its not best practice in terms of readability, but for a change I laid focus
#compressing the code in this one.

def tower_builder(n_floors):
    pyramid = [("*" + n*2*"*").center(2*n_floors-1)]
    #pyramid = [(n_floors-(n+1))*" " + "*" + n*2*"*" + (n_floors-(n+1))*" " for n in range(n_floors)]
    return pyramid

# task description:
# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
#
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]
