#Corinne Kieras, 10/9
#Code that takes in a hex value, turns it into an array of ints and performs calculations on
#them to compute the hamming code.
def hamming(theval):
    #converts the hex to a binary
    valone = bin(int('1'+ theval, 16))[3:]
    value = []
    #appends the values of valone into a list
    for i in valone:
        value.append(i)
    #converts the values in list value to ints
    val = list(map(int,value))
    #inserts 0's in val as placeholders for the parity bits
    val.insert(0,0)
    val.insert(1,0)
    val.insert(3,0)
    val.insert(7,0)
    val.insert(15,0)
    #Invariant: sum1 holds the total amount of 1's for every other bit in val
    sum1 = 0
    for i in range(0, len(val), 2):
       sum1+=val[i]
    if sum1%2==1: #if the sum1 is odd insert a 1 for the parity bit
        val.remove(0)
        val.insert(0,1)
    else:
        val.remove(0) #otherwise insert a 0 for the parity bit
        val.insert(0,0)
    #Appends the values for the 2nd parity bit into a new list.
    sum2 = 0
    valbytwo = []
    valbytwo.append(val[2])
    valbytwo.append(val[5])
    valbytwo.append(val[6])
    valbytwo.append(val[9])
    valbytwo.append(val[10])
    valbytwo.append(val[13])
    valbytwo.append(val[14])
    valbytwo.append(val[17])
    valbytwo.append(val[18])
    #Invariant: sum2 holds the total of 1's in valtwo in order to compute the parity bit.
    for thing in range(len(valbytwo)):
        sum2+=valbytwo[thing]
    if sum2%2==1:
        del(val[1]) #if the sum of 1's in the list is odd insert a 1 into the original list
        val.insert(1,1)
    else:
        del(val[1])
        val.insert(1,0)#else, insert a 0
    # Appends the values for the 3nd parity bit into a new list.
    sum3 = 0
    valbyfour = []
    valbyfour.append(val[4])
    valbyfour.append(val[5])
    valbyfour.append(val[6])
    valbyfour.append(val[11])
    valbyfour.append(val[12])
    valbyfour.append(val[13])
    valbyfour.append(val[14])
    valbyfour.append(val[19])
    valbyfour.append(val[20])
    # Invariant: sum3 holds the total amount of 1's for every other bit in val
    for x in range(len(valbyfour)):
        sum3+=valbyfour[x]
    if sum3%2==1:
        del(val[3])#if the sum of 1's in the list is odd insert a 1 into the original list
        val.insert(3,1)
    else:
        del(val[3])
        val.insert(3,0)#else, insert a 0
    # Appends the values for the 4nd parity bit into a new list.
    sum4 = 0
    valbyeight = []
    valbyeight.append(val[8])
    valbyeight.append(val[9])
    valbyeight.append(val[10])
    valbyeight.append(val[11])
    valbyeight.append(val[12])
    valbyeight.append(val[13])
    valbyeight.append(val[14])
    # Invariant: sum4 holds the total amount of 1's for every other bit in val
    for x in range(len(valbyeight)):
        sum4 += valbyeight[x]
    if sum4 % 2 == 1:
        del(val[7]) #if the sum of 1's in the list is odd insert a 1 into the original list
        val.insert(7, 1)
    else:
        del(val[7])
        val.insert(7, 0)#else, insert a 0
    # Appends the values for the 4nd parity bit into a new list.
    sum5 = 0
    valbysixteen = []
    valbysixteen.append(val[16])
    valbysixteen.append(val[17])
    valbysixteen.append(val[18])
    valbysixteen.append(val[19])
    valbysixteen.append(val[20])
    # Invariant: sum5 holds the total amount of 1's for every other bit in val
    for k in range(len(valbysixteen)):
        sum5 += valbysixteen[k]
    if sum5 % 2 == 1:
        del(val[15])#if the sum of 1's in the list is odd insert a 1 into the original list
        val.insert(15, 1)
    else:
        del(val[15])#else, insert a 0
        val.insert(15, 0)
    #joins all the ints in val together
    #joinedval = "".join(map(str, val))
    val = "".join(map(str, val))
    val = '%8X' % int(val, 2)
    print(val)

tr = raw_input("Please enter a 4-digit hexadecimal value: ")
if len(tr) != 4:
    print("You did not enter four digits! Aborting.")
    exit()

hamming(tr)

#hamming code extra code
def hammingextras(val):
    value = []
    errorfinder = []
    for i in val:
        value.append(i)
    #converts the values in list value to ints
    val = list(map(int,value))
    # Invariant: sum1 holds the total amount of 1's for every other bit in val
    sum1 = 0
    for i in range(0, len(val), 2):
        sum1 += val[i]
    if sum1 % 2 == 1:  # if the sum1 is odd insert a 1 for the parity bit
        errorfinder.append(1)
    #else:
     #   val.remove(0)  # otherwise insert a 0 for the parity bit
      #  val.insert(0, 0)
    # Appends the values for the 2nd parity bit into a new list.
    sum2 = 0
    valbytwo = []
    valbytwo.append(val[1])
    valbytwo.append(val[2])
    valbytwo.append(val[5])
    valbytwo.append(val[6])
    valbytwo.append(val[9])
    valbytwo.append(val[10])
    valbytwo.append(val[13])
    valbytwo.append(val[14])
    valbytwo.append(val[17])
    valbytwo.append(val[18])
    # Invariant: sum2 holds the total of 1's in valtwo in order to compute the parity bit.
    for thing in range(len(valbytwo)):
        sum2 += valbytwo[thing]
    if sum2%2 == 1:
        errorfinder.append(2)
    #else:
     #   del (val[1])
      #  val.insert(1, 0)  # else, insert a 0
    # Appends the values for the 3nd parity bit into a new list.
    sum3 = 0
    valbyfour = []
    valbyfour.append(val[3])
    valbyfour.append(val[4])
    valbyfour.append(val[5])
    valbyfour.append(val[6])
    valbyfour.append(val[11])
    valbyfour.append(val[12])
    valbyfour.append(val[13])
    valbyfour.append(val[14])
    valbyfour.append(val[19])
    valbyfour.append(val[20])
    # Invariant: sum3 holds the total amount of 1's for every other bit in val
    for x in range(len(valbyfour)):
        sum3 += valbyfour[x]
    if sum3 % 2 == 1:
        errorfinder.append(4)
    #else:
     #   del (val[3])
      #  val.insert(3, 0)  # else, insert a 0
    # Appends the values for the 4nd parity bit into a new list.
    sum4 = 0
    valbyeight = []
    valbyeight.append(val[7])
    valbyeight.append(val[8])
    valbyeight.append(val[9])
    valbyeight.append(val[10])
    valbyeight.append(val[11])
    valbyeight.append(val[12])
    valbyeight.append(val[13])
    valbyeight.append(val[14])
    # Invariant: sum4 holds the total amount of 1's for every other bit in val
    for x in range(len(valbyeight)):
        sum4 += valbyeight[x]
    if sum4 % 2 == 1:
        errorfinder.append(8)
   # else:
    #    del (val[7])
     #   val.insert(7, 0)  # else, insert a 0
    # Appends the values for the 4nd parity bit into a new list.
    sum5 = 0
    valbysixteen = []
    valbysixteen.append(val[15])
    valbysixteen.append(val[16])
    valbysixteen.append(val[17])
    valbysixteen.append(val[18])
    valbysixteen.append(val[19])
    valbysixteen.append(val[20])
    # Invariant: sum5 holds the total amount of 1's for every other bit in val
    for k in range(len(valbysixteen)):
        sum5 += valbysixteen[k]
    if sum5 % 2 == 1:
        errorfinder.append(16)
    sm = sum(errorfinder)
    if sm !=0:
        if val[sm-1]==0:
            del(val[sm-1])
            val.insert((sm-1),1)
        else:
            del(val[sm-1])
            val.insert((sm-1),0)
        val = int("".join(map(str, val)))
        print"This is the correct Hamming code: ", val
        print"You had an error at bit: ",sm
    else:
        print("Your Hamming Code is correct.")


hammcode = raw_input("Please enter a 21-digit Hamming Code you would like to check: ")
if len(hammcode) != 21:
    print("You did not enter 21 digits! Aborting.")
    exit()
#print "Here is the corrected Hamming Code: ",hammingextras(hammcode)
hammingextras(hammcode)
