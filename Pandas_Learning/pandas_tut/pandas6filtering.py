import pandas as pd

df = pd.read_csv("data.csv",index_col="Name")

# filtering = keeping the rows that match the condition

# tall_pokemon = (df[df["Height"]>8])
# # print(tall_pokemon)
# # print(df[df["Weight"]>100])
# heavy_pokemon = (df[df["Weight"]>100])
# print(heavy_pokemon)

# light_pokemon = (df[df["Weight"]<100])
# legendary_pokeman = (df[df["Legendary"]==1])
# legendary_pokeman = (df[df["Legendary"]==True])
# water_pokemon = (df[(df["Type1"]=="Water")|(df["Type2"]=="Water")])
# water_pokemon = (df[(df["Type1"]=="Water")|(df["Type2"]=="Water")])
# print(water_pokemon)
# print(legendary_pokeman)
# print(light_pokemon.to_string())

# ff_pokemon = df[(df["Type1"]=="Fire")]
# ff_pokemon = df[(df["Type1"]=="Fire") &
#                 (df["Type2"]=="Flying")]
# print(ff_pokemon)



# while True:
#   print("Choose your option")
#   print("1 for Name")
#   print("2 for Height")
#   print("3 for weight")
#   print("4 for type 2")
#   print("0 for exit")
#   option = int(input("Choose your condition : "))
#   match option:
#     case 1:
#       print(df[df["Name"]])
#     case 2:
#       filter_num = int(input("Enter your filtering number : "))
#       print(df[df["Height"]>filter_num])
#     case 3:
#       filter_num = int(input("Enter your filtering number : "))
#       print(df[df["Weight"]>filter_num])
#     case "Type 2":
#       filter_num = int(input("Enter your filtering number : "))
#       print(df[df["Type 2"]>filter_num])
#     case 0:
#       break