def rgb_to_hex(rgb):
    hex_chars = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    if rgb < 0:
        rgb = 0
    if rgb > 255:
        rgb = 255
    rgb = round(rgb)
    hex = hex_chars[rgb//16] if rgb//16 > 9 else str(rgb//16)
    hex += hex_chars[(rgb%16)*1] if (rgb%16)*1 > 9 else str((rgb%16)*1)
    return hex

def rgb(r, g, b):
    hex = rgb_to_hex(r) + rgb_to_hex(g) + rgb_to_hex(b)
    # your code here :)
    return hex

# task description:
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values: