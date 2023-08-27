def stars(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("* ", end="")
        print()

# Driver Code
num_rows = 5
stars(num_rows)
