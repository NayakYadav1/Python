def count_file_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = 0
            word_count = 0
            char_count = 0

            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                char_count += len(line)

        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "Day20/data.txt"  # Replace with your file path
count_file_stats(filename)
