
# A PROGRAM TO GENERATE SOME NOUNS AND ADJECTIVES FROM USER AND FORM A PARAGRAPH

count_adj = 0
num_adj = 1
listadj = []

person = input("Enter the name of this person: ")
print("Enter 5 adjectives.")

while count_adj < 5:
    print("Enter in adjective {} ".format(num_adj))
    adjective = input(" ")
    listadj.append(adjective)#ADDING THE ADJS INTO THE LIST
    num_adj = num_adj + 1
    count_adj = count_adj + 1

count_noun = 0
num_noun = 1
listnoun = []

print("Enter in a total of 4 nouns")
while count_noun < 4:
    print("Enter in noun {}".format(num_noun))
    noun = input(" ")
    listnoun.append(noun)#ADDING THE NOUNS INTO THE LIST
    num_noun = num_noun + 1
    count_noun = count_noun + 1


print("Dear Art Teacher")

print("Please excuse", person, "for being late for your", listadj[0], "art class.  It\'s my fault.I feel")
print(listadj[1], person, "was up until the ", listadj[2], "hours of the morning finishing his/her", listadj[3], "project")
print("Just as we were going out the", listadj[4], "door, I saw that his/her only pair of", listnoun[0], "had a", listnoun[1])
print("in them.  He/she needed to change! Then it took me an hour to find my", listnoun[2], "to drive")
print("him/her to school that morning since,", person, "missed the", listnoun[3])
