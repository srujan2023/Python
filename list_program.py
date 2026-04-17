# List Sample Program in Python

def main():
    numbers = [10, 20, 30, 40]
    print("numbers:", numbers, "| first:", numbers[0], "| last:", numbers[-1], "| slice:", numbers[:3])

    numbers.append(50)
    numbers[1:1] = [15]          # insert 15 at index 1 (short form)
    numbers.extend([60, 70])
    print("after add:", numbers)

    numbers.remove(30)
    popped = numbers.pop()
    print("popped:", popped, "| after remove:", numbers)

    x = 40
    print("search 40 index:", numbers.index(x) if x in numbers else -1)
    print("length:", len(numbers))

    print("sorted copy:", sorted(numbers))
    numbers.sort(reverse=True)
    print("sorted desc:", numbers)

    print("loop:", *numbers)
    numbers.clear()
    print("after clear:", numbers)


if __name__ == "__main__":
    main()
