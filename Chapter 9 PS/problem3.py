def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

#now calling function to generate tables from 1 to 10
for i in range(2, 21):
    generateTable(i)