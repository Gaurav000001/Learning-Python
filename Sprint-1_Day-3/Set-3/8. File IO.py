# 1. **File I/O**: Write a Python program that reads a file, counts the number of words,
# and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0


def write_word_count(file_path, count):
    try:
        with open(file_path, 'w') as file:
            file.write(str(f"Number of words: {count}"))
            print(f"Word count ({count}) written to file '{file_path}' successfully.")
    except IOError:
        print(f"Error: Could not write to file '{file_path}'.")


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    word_count = count_words(input_file)
    write_word_count(output_file, word_count)
