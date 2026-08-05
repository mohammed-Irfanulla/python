def first_non_repeating_character(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None


if __name__ == "__main__":
    s = input("Enter the string: ")
    result = first_non_repeating_character(s)
    if result is None:
        print("No non-repeating character found")
    else:
        print(result)
