#The program's version is 0.2.3
print("/->Input Testing 0.2.3<-")
print("|")
#Let the user type something
txt = input("\_/->Say something: ")
#If the user said the value "smiling cat", do this:
if txt == "smiling cat":
    print(" | :)")
    #After continue to "else:"
#If the user said the value "cat", do this:
if txt == "cat":
    print(" | cute cat")
    #After continue to "else:"
#If the user said the value "test", do this:
if txt == "test":
    print(" | wtf are you testing?")
    #After continue to "else:"
#If the user said the value "sus", do this:
if txt == "sus":
    print(" | no u")
    #After continue to "else:"
#If the user said nothing, do this:
if txt == "":
    print(" | ")
    #After continue to "else:"
#If the user said the value "obsolete", do this:
if txt == "obsolete":
    print(" | ERROR: OBSOLETE TEXT. RETRYING. (error code: 0x08501373)")
    #After continue to "else:"
#If the user said the value "sussy", do this:
if txt == "sussy":
    print(" | no u")
    print(" | ")
    print("/---->", txt) #txt - what the user have typed in.
    print("|  /--\ ") #Comment
    print("| /-----> this is what you have typed in") #idk what to type here
    print("\/ ")
    #After do nothing, because after you said this value the program skips "else:"
#If nothing matches these values, do the else:
else:
    #Print the text the user have typed in
    print(" | ")
    print("/---->", txt) #txt - what the user have typed in.
    print("|  /--\ ") #Comment
    print("| /-----> this is what you have typed in") #idk what to type here
    print("\/ ")