import numpy as np

# filtering = refers to the process of selecting elements
              # from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages <= 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
# print((adults))
# print((adults))
# print((evens))
# print((odds))

adults = np.where(ages >= 18, ages,0)
# adults = np.where(ages >= 18, ages,-1)
print(adults)