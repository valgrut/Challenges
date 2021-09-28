# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

def conv(char):
    return (ord(char) - 96)

def csum(str):
    x = 0
    for ic in range(0, len(str)):
            # x += conv(str[ic])
            x += (ord(str[ic]) - 96)
    return x

# Test
print("abc", csum("abc"))
print("acb", csum("acb"))
print("b", csum("b"))
print("",csum(""))
print("excellent", csum("excellent"))
print("microspectrophotometries", csum("microspectrophotometries"))
