def rearrange_alternating(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    result = []
    i, j = 0, 0

    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    result.extend(pos[i:])
    result.extend(neg[j:])
    return result


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(rearrange_alternating(arr))
