def solution(number):
    if number <= 0:
        return 0
    sum = 0
    fives = (number - 1) // 5
    threes = (number - 1) // 3
    for i in range(fives):
        sum += (i + 1) * 5
    for i in range(threes):
        sum += (i + 1) * 3
    for i in range(fives // 3):  # determine how many shared multiples occur
        sum -= (
                           i + 1) * 15  # each shared multiple is a multiple of 15 so substract the occuring multiples of 15 from sum
    return sum

# Task description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
#
# Note: If the number is a multiple of both 3 and 5, only count it once.