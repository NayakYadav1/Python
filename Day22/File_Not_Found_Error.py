try:
    with open("Day20/data.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("File not found. Please check the file path and try again.")
finally:
    print("Execution completed.")