import stackclass

# User specifies a name for the stack
stkname = input("Stack name: ")
stktype = input("Storage type: ")

skc = stackclass.stackbase(stackname=stkname, type=stktype)

recs = skc.create_stack()

done = False
val1 = "\nParticipant: "
val2 = "Value: "

while not done:
    name = input(val1)

    if name == "":
        done = True
        break

    else:
        score = input(val2)

        skc.push(name, score)

print(recs)
