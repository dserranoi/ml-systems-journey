def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    return sum(numbers) / len(numbers)

def filter_positive(numbers: list[float]) -> list[float]:
    """Return only positive numbers from the list."""
    return [n for n in numbers if n > 0]

if __name__ == "__main__":
    data: list[float] = [3.5, -1.2, 7.0, -0.5, 4.2]
    positives = filter_positive(data)
    average = calculate_average(positives)
    print(f"Positives: {positives}")
    print(f"Average: {average:.2f}")