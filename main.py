from LongestSuffix import longest_suffix

if __name__ == '__main__':
    input_str = input()
    two_str = input_str.split()
    if len(two_str) != 2:
        raise Exception
    regular_machine_str = two_str[0]
    pattern = two_str[1]
    print(longest_suffix(regular_machine_str, pattern))


