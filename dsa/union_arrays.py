def union_of_arrays(a, b):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    for item in b:
        if item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    a = input("Enter the first numbers string: ").split()
    b = input("Enter the second numbers string: ").split()
    print(" ".join(union_of_arrays(a, b)))
