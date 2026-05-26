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



# -----------------------------------------------------
# 2 Öva på loopar och listor

print("\nUppgift 2:1a")
print("1a Skriv färdigt kodexemplet")
print("------------------------------------------------")
# Programmet beräknar summan av talen 1 till 10 i en loop där talen adderas.

answer = 0
for i in range(11):
    answer += i
print(f"Summan av talen 1 till 10 är : {answer}")


print("\nUppgift 2:1b")
print("1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)")
print("------------------------------------------------")
# Programmet beräknar summan av talen 1 till 100 i en for-loop där talen adderas.

sum_of_numbers_1_to_100 = 0

for i in range(1, 101):
    sum_of_numbers_1_to_100 += i
print(f"Summan av talen 1 till 100 = {sum_of_numbers_1_to_100}")


print("\nUppgift 2:1c")
print("1c Skriv om 1b så att den använder en while-loop.")

print("------------------------------------------------")
# Programmet beräknar summan av talen 1 till 100 i en while-loop där talen adderas.

sum_of_numbers_1_to_100 = 0
increment_value = 1

while increment_value <= 100:
    sum_of_numbers_1_to_100 += increment_value
    increment_value += 1
print(f"Summan av talen 1 till 100 = {sum_of_numbers_1_to_100}")


print("\n2:2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]")
# Programmet itererar en lista med tal och adderar objekten.

list_of_numbers = [1, -2, 3, -2, 4, -3]
sum_of_numbers = 0

for item in list_of_numbers:
    sum_of_numbers += item
print(f"Summan av talen i listan = {sum_of_numbers}")


# 3 Träna på att skapa och manipulera listor.
#   Alla uppgifter ska lösas med funktionerna som står i presentationen.

print("\n3:3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar.")
list_of_movies = ["Terminator", "Avatar", "Alien", "Prometheus"]
print(list_of_movies)


print("\n3:3b Lägg till 'Fellowship of the ring' sist i listan.")
list_of_movies.append("Fellowship of the ring")
print(list_of_movies)


print("\n3:3c Lägg till 'The two towers' på första platsen i listan. (index noll)")
list_of_movies.insert(0, "The two towers")
print(list_of_movies)


print("\n3:3d Ta reda på vilken position (index) 'Fellowship of the ring' har nu.")
index_fellowship_of_the_ring = list_of_movies.index('Fellowship of the ring')
print(f"Fellowship of the ring har nu ändrat till index : {index_fellowship_of_the_ring}")


print("\n3:3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?")
list_of_movies.remove("Avatar")
index_fellowship_of_the_ring = list_of_movies.index('Fellowship of the ring')
print(f"Fellowship of the ring har nu ändrat till index : {index_fellowship_of_the_ring}")


print("\n3:3f Ta reda på hur lång listan är. (len)")
number_of_films_in_list = len(list_of_movies)
print(f"Listan med filmer innehåller : {number_of_films_in_list} objekt.")


print("\n3:3g Vänd listan baklänges.")
list_of_movies.reverse()
print(list_of_movies)


print("\n3:3h Sortera listan stigande i bokstavsordning")
print("------------------------------------------------")
list_of_movies.sort()
print(list_of_movies)




#3 Kvittouträknaren

# -----------------------------------------------
# Collect subtotals until user abort with "quit"
# -----------------------------------------------
print("\nVälkommen till Kvittokompis! Avsluta genom att skriva: quit")

list_of_subtotals = []

while True:
    subtotal = input("Skriv in ett belopp: ")

    if subtotal.lower() == "quit":
        break

    try:
        list_of_subtotals.append (float(subtotal))
    except ValueError:
        print("\nFel input, det inmatade värdet är inget belopp.")
        print("Försök igen.")


# -----------------------------------------------
# Sum subtotals entered by user
# -----------------------------------------------
total_sum = sum(list_of_subtotals)


# -----------------------------------------------
# Ask user for amount of persons to share the bill
# -----------------------------------------------
persons_to_split = 0

while True:

    try:
        persons_to_split = int(input("Hur många är ni? "))

        if persons_to_split < 1:
            print("\nMinst en person måste betala.")
            print("Försök igen.")
            continue
        break

    except ValueError:
        print("\nFel input, mata in antalet personer som ska dela notan.")
        print("Försök igen.")
        continue

# -----------------------------------------------
# Ask user for tip in percent. Blank input sets default 10 %.
# -----------------------------------------------

while True:
    tip_in_percent = input("Ange dricks i % (blank = 10 %): ")

    if tip_in_percent == "":
        tip_in_percent = 10.0 # Default if no user selection
        break

    try:
        tip_in_percent = float(tip_in_percent)
        break

    except ValueError:
        print("\nFel input, mata in dricks i procent.")
        print("Försök igen.")

# -----------------------------------------------
# Calculate total tip and total sum including tip
# -----------------------------------------------
total_tip = total_sum * (tip_in_percent /100)
sum_to_pay = total_sum + total_tip

# -----------------------------------------------
# Calculate amount to pay for each person
# -----------------------------------------------
amount_per_person = sum_to_pay / persons_to_split

# -----------------------------------------------
# Print results
# -----------------------------------------------
print("--------------------------------------------")
print("-- KVITTO")
print("--------------------------------------------")

print(f"-- Summa att betala: \t {round(total_sum, 2)} kr")
print(f"-- Dricks {tip_in_percent} %  \t\t {round(total_tip, 2)} kr")
print(f"-- Per person  : \t\t {round(amount_per_person, 2)} kr")
print("--------------------------------------------")
print(f"-- Totalt att betala : \t {round(sum_to_pay, 2)} kr")
print("--------------------------------------------")
print("Välkommen åter!")
