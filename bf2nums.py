d = {">": "1", "<": "2", "+": "3", "-": "4", ".": "5", ",": "6"}
res = ""
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        for char in line:
            res += d[char] + " "

with open("output.txt", "w") as f:
    f.write(res[:-1])
print("Готово")

