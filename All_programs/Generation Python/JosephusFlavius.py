number_of_person = int(input())
# number_of_person = 2^a + l     res = 2 * l + 1

m = number_of_person
counter = 0
while m >= 2:
    if m % 2 != 0:
        m = m-1
    m = m/2
    counter += 1

l = number_of_person - 2**counter


number_of_place = 2 * l + 1
print(number_of_place)
