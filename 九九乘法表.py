row = 1
while row < 10:
    col = 1
    while col <= row:
        print(f"{col} * {row} = {col * row}",end="\t")
        col += 1
    print()
    row += 1 
