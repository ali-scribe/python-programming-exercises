f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("The word 'twinkle' is present in the poem.")
else:
    print("The word 'twinkle' is not present in the poem.")

f.close()