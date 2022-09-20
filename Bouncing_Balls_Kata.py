def bouncing_ball(h, bounce, window):
    # your code
    if (h <= 0 or (bounce >= 1 or bounce <= 0) or window >= h):
        return -1
    i = 1  # first fall down
    h *= bounce  # height reached after first bounce
    while (h > window):
        i += 2  # for every following bounce mother sees ball rising an falling
        h *= bounce
    return i
