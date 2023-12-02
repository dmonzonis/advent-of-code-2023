def find_first_digit(s):
    """Find the first digit in a string."""
    for c in s:
        if c.isdigit():
            return int(c)
    return 0


def get_first_last_digits(s):
    """Get the first and last digits in a string and concatenates them together."""
    first_digit = find_first_digit(s)
    last_digit = find_first_digit(s[::-1])
    return first_digit * 10 + last_digit


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# Part 1
sum_digits = sum(get_first_last_digits(line) for line in lines)
print(sum_digits)
