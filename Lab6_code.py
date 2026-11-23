
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    filename = "date.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            numbers_line = file.readline()
            algorithm_line = file.readline()

        if not numbers_line or not algorithm_line:
            print("Error: The file must contain two input lines.")
            return

        numbers_text = numbers_line.split()

        if not numbers_text:
            print("Error: No numbers found in the file.")
            return

        try:
            numbers = [int(number) for number in numbers_text]
        except ValueError:
            print("Error: The file contains invalid numbers.")
            return

        algorithm = algorithm_line.strip().lower()

        if algorithm == "insertion":
            result = insertion_sort(numbers.copy())
            algorithm_name = "Insertion"

        elif algorithm == "merge":
            result = merge_sort(numbers.copy())
            algorithm_name = "Merge"

        else:
            print("Error: Unknown sorting algorithm.")
            print("Available algorithms: Insertion, Merge")
            return

        original_data = numbers_line
        if not original_data.endswith(("\n", "\r")):
            original_data += "\n"

        original_data += algorithm_line
        if not original_data.endswith(("\n", "\r")):
            original_data += "\n"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(original_data)
            file.write(f"{algorithm_name}: {' '.join(map(str, result))}\n")

        print("Sorting completed successfully!")
        print(f"Algorithm: {algorithm_name}")
        print(f"Sorted numbers: {result}")

    except FileNotFoundError:
        print("Error: date.txt file was not found.")

    except OSError:
        print("Error: Unable to read or write the file.")


if __name__ == "__main__":
    main()
