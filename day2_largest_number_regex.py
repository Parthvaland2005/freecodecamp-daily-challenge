import re

def largest_number(s):
    nums = re.split(r"[,!?:;]", s)
    return max(float(num) for num in nums)

if __name__ == "__main__":
    print(largest_number("1,5;10.5:-20"))