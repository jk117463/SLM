import random

#Defining dices
normal_dice = sorted(list(range(1, 7)))
sums_of_normal_dices = sorted(list(d1 + d2 for d1 in normal_dice for d2 in normal_dice))
already_checked_combinations = list()
max_value_on_a_dice = 10
found = False

#max iterations
max_iterations = 10 ** 10

for i in range(0, max_iterations):
    new_dice1 = [1]
    new_dice2 = [1]
    while len(new_dice1) < 6 and len(new_dice2) < 6:
        new_dice1.append(random.randint(2, max_value_on_a_dice))
        new_dice2.append(random.randint(2, max_value_on_a_dice))

    new_dice1.sort()
    new_dice2.sort()

    #perform standard validations
    if new_dice1 == normal_dice or new_dice2 == normal_dice or max(new_dice1) + max(new_dice2) > 12:
        continue

    if [new_dice1, new_dice2] in already_checked_combinations or [new_dice2, new_dice1] in already_checked_combinations:
        continue

    sums_of_new_dices = sorted(list(d1 + d2 for d1 in new_dice1 for d2 in new_dice2))

    #if sorted list of sum (cobimations) of dices are same they we've a match
    if sums_of_normal_dices == sums_of_new_dices:
        print("\n Sicherman dices found! \n Dice - 1 : " + new_dice1.__str__() + "\n Dice - 2 : " + new_dice2.__str__())
        found = True
        break

    already_checked_combinations.append([new_dice1, new_dice2])

if found == False:
   print("Sicherman dices not found!")