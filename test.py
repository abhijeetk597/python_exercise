def count_frequency(input_dict):
    frequency_dict = {}  # Dictionary to store element frequencies

    for key, value in input_dict.items():
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    return frequency_dict

# Example usage
input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
frequency_result = count_frequency(input_dict)

print("Frequency of each element:")
for key, value in frequency_result.items():
    print(f"'{key}': {value}")

