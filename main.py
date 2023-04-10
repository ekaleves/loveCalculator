# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

nameCount1 = 0
nameCount2 = 0
score = "score"

nameCount1 += int(name1.count("t"))
nameCount1 += int(name1.count("r"))
nameCount1 += int(name1.count("u"))
nameCount1 += int(name1.count("e"))
nameCount1 += int(name2.count("t"))
nameCount1 += int(name2.count("r"))
nameCount1 += int(name2.count("u"))
nameCount1 += int(name2.count("e"))


nameCount2 += int(name1.count("l"))
nameCount2 += int(name1.count("o"))
nameCount2 += int(name1.count("v"))
nameCount2 += int(name1.count("e"))
nameCount2 += int(name2.count("l"))
nameCount2 += int(name2.count("o"))
nameCount2 += int(name2.count("v"))
nameCount2 += int(name2.count("e"))

score = str(nameCount1) + str(nameCount2)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your Score is {score}")


