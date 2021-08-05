name = input("Enter your name:\n")
print(f"Welcome {name}")
myList = ["Hate", "Wisdom", "Boy", "Girlfriend", "Woman", "Husband", "Wisdom", "Wife", "Wellington", "Seven",
"Us", "Pretend", "Monkey", "Hospital", "Mansion", "Speaker", "Believe", "Success"]

do =  len(myList)
for i in range(do):
    length = len(myList[i])
    print("The length of the word", myList[i] + " is", length)