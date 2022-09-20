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