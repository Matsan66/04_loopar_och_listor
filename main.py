####################
# Veckouppgift 3
####################

# 1 Diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE,
# exakt som den står, och kör den.

# 1. Vad skrivs ut?
# Svar = Lodrät : 5 7 9 11 13 15
print("\nUppgift 1:1")
print("---------------")
limit = 15
index = 5

while index <= limit:
    print(index)
    index += 2


# ------------------------------------------
# 2. Vad skrivs ut?
# Svar = Lodrät : 0 1 2 3 4  6 7 8 9
print("\nUppgift 1:2")
print("---------------")
for i in range(10):
    if i == 5:
        print(" ")
    else:
        print(i)
    # i += 1 Onödig rad. i inkrementeras i loopen


# ------------------------------------------
# 3. Vad blir summan? Skriv ner din bästa gissning innan du kör koden.
# Svar = 15
print("\nUppgift 1:3")
print("---------------")
counter = 0
for i in range(6):
    counter += i
print(counter)


# ------------------------------------------
# 4. Vad skrivs ut?
# Svar =
# x tilldelas värdena 1, -1, 8, 4, 29, 23, 72, 64, 145
# slutvärde = 145
print("\nUppgift 1:4")
print("---------------")
x = 0
y = 1

while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y += 1
print(f"Värdet på x = {x}")


# ------------------------------------------
# 5. Vad skrivs ut?
# Svar = _tim
print("\nUppgift 1:5")
print("---------------")

print("Originalkod")
message = "its_time_to_get_coding"
print(message[3:7])

# Kan du göra om koden så att den skriver ut "time" i stället?
print("\nÄndrad kod")
message = "its_time_to_get_coding"
print(message[4:8])


# ------------------------------------------
# 6. Vad skrivs ut?
# Svar =
print("\nUppgift 1:6")
print("---------------")
"""
#........
.#.......
..#......
...#.....
....#....
.....#...
......#..
"""

print("Originalkod")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

# Kan du flytta linjen ett steg åt höger?
print("\nÄndrad kod")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1:
            s += "#"
        else:
            s += "."
    print(s)
