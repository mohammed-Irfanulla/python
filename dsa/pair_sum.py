def find_pairs(arr, target):
    pairs = []
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs


if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    arr = [int(input("Enter the number: ")) for _ in range(n)]
    target = int(input("Enter the target sum: "))
    for a, b in find_pairs(arr, target):
        print(a, b)
