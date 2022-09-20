#I admit this one is a little... chunky (haha) compared to other solutions,
# but I put more focus on making the code understandable und readable instead of
# compressing it as dense as possible, which does not mean that I could not still be improved upon.

def calculate_fib(n):                                                   # first defining a simple method for calculating result of the fibonacci sequence with a given n
    sum = 0
    prev_num = 0
    current_num = 1
    for i in range(n - 1):
        sum = prev_num + current_num
        prev_num = current_num
        current_num = sum
    return sum


def around_fib(n):
    total = calculate_fib(n)
    num_string = str(total)                                                # converting the result of calculate_fib to a string to make it iterable.
    maxcnt = 0                                                             # variable for storing the most occurences of any digits in num_string
    digit = 9                                                              # initializing digit variable. Could be initialized with any digit, but since the following loop starts with 9 I decided for that.
    for n in reversed(
            range(10)):                                                    # looping down from 9 to inclusive 0. Personal taste made me use this syntax instead for the start,end,step syntax.
        if num_string.count(
                str(n)) >= maxcnt:                                         # if occurences of actual digit is higher or equal than current maxcnt, maxcnt gets updated, but more importantly digit gets updated as well. By counting down in the loop it is assured that with equal occurences of different digits, the digit variable always stores the smaller one.
            maxcnt = num_string.count(str(n))
            digit = n

    chunks = []                                                            # creating an empty list to store the chunks in
    num_of_chunks = (len(num_string) // 25)                                # calculating how many chunks of 25 digits exist in num_string

    for i in range(num_of_chunks):                                         # appending whole chunks of 25 digits to chunks[]
        chunks.append(num_string[i * 25:(i + 1) * 25])
    if not len(num_string) % 25 == 0:                                      # if there is a remaining chunk smaller than 25 characters
        chunks.append(num_string[num_of_chunks * 25:])

    return "Last chunk " + chunks[-1] + "; Max is " + str(maxcnt) + " for digit " + str(digit)

# task description:
# Another Fibonacci... yes but with other kinds of result. The function is named aroundFib or around_fib, depending of the language. Its parameter is n (positive integer).
#
# First you have to calculate f the value of fibonacci(n) with fibonacci(0) --> 0 and fibonacci(1) --> 1 (see: https://en.wikipedia.org/wiki/Fibonacci_number)
#
#         Find the count of each digit ch in f (ch: digit from 0 to 9), call this value cnt and find the maximum value of cnt; call this maximum value maxcnt. If there are ties, the digit ch to consider is the first one - in natural digit order - giving maxcnt.
#         Cut the value f into chunks of length at most 25. The last chunk may be 25 long or less.
#
# Example: for `n=100` you have only one chunk `354224848179261915075`
# Example: for `n=180` f is `18547707689471986212190138521399707760` and you have two chunks
# `1854770768947198621219013` and `8521399707760`. First length here is 25 and second one is 13.
#
#     At last return a string in the following format: "Last chunk ...; Max is ... for digit ..."
#
# where Max is maxcnt and digit the first ch (in 0..9) leading to maxcnt.
#
# Example: for `n=100` -> "Last chunk 354224848179261915075; Max is 3 for digit 1"
# Example: for `n=180` -> "Last chunk 8521399707760; Max is 7 for digit 7"
# Example: for `n=18000` -> "Last chunk 140258776000; Max is 409 for digit 1"
