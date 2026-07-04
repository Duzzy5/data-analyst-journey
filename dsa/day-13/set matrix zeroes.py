arr = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

def zp(arr):

    rows = []
    columns = []

    # Step 1: Find all original zeros
    for i in range(len(arr)):
        for j in range(len(arr[0])):

            if arr[i][j] == 0:

                rows.append(i)
                columns.append(j)

    # Step 2: Zero the rows
    for row in rows:

        for j in range(len(arr[0])):

            arr[row][j] = 0

    # Step 3: Zero the columns
    for col in columns:

        for i in range(len(arr)):

            arr[i][col] = 0

    return arr


print(zp(arr))
