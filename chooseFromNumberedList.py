#!/usr/bin/python

# Version 0.3
# Date 20250523
#
# chooseFromNumberedList allows you to print and select from items in a given
# list by entering the number or moving the selector up and down with the plus
# and mius signs, or with brackets pointing left (backward) or right (forward),
# also multiple in one input. Confirm every input with the Enter key.
#
# The function requires exactly four arguments:
# the NumberedList:    the given [list, with, the, items] to choose from
# the Sorting Method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
# the Starting Number: common are 0 or 1, but any positive number can be given
# the Default Option:  a number in the numbering list, between the lowest and
#                      the highest number in the list (inclusive)
# It returns the selected item in the list and its index number in that list.
def chooseFromNumberedList(NumberedList,AscendingOrDescendingOrRandom,StartWithZeroOrOne,DefaultOption):
    import random
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    this = "-> "
    thisnot = "   "
    connect = " : "
    Int = DefaultOption
    IntList = []
    if AscendingOrDescendingOrRandom.upper() == "D":
        for item in NumberedList:
            IntList.append(len(NumberedList)-NumberedList.index(item)+StartWithZeroOrOne-1)
    elif AscendingOrDescendingOrRandom.upper() == "R":
        TempList = []
        for item in NumberedList:
            TempList.append(NumberedList.index(item)+StartWithZeroOrOne)
        while len(TempList) > 0:
            Num = random.choice(TempList)
            IntList.append(Num)
            TempList.remove(Num)
    else:
        for item in NumberedList:
            IntList.append(NumberedList.index(item)+StartWithZeroOrOne)
    def printNumberedList(Int):
        StrList = []
        for i in IntList:
            StrList.append(str(i))
        maxlen = len(max(StrList,key = len))
        Index = (Int-StartWithZeroOrOne) % len(IntList)
        if AscendingOrDescendingOrRandom.upper() == "D":
            PrInt = len(IntList)-1-IntList.index(Index+StartWithZeroOrOne)
        else:
            PrInt = IntList.index(Index+StartWithZeroOrOne)
        for i in IntList:
            if i-StartWithZeroOrOne == PrInt:
                print(this+("{:>%d}" % maxlen).format(i)+connect+str(NumberedList[IntList.index(i)]))
            else:
                print(thisnot+("{:>%d}" % maxlen).format(i)+connect+str(NumberedList[IntList.index(i)]))
        return Int
    printNumberedList(Int)
    yes = True
    while yes == True:
        ip = input()
        try:
            Index = (int(ip) - StartWithZeroOrOne) % len(NumberedList)
            Int = Index + StartWithZeroOrOne
        except(Exception) as e:
            #print(e)
            if ip == "":
                break
            for k in ip:
                if k in nexti:
                    Index = (Int - StartWithZeroOrOne + 1) % len(NumberedList)
                    Int = Index + StartWithZeroOrOne
                elif k in previ:
                    Index = (Int - StartWithZeroOrOne - 1) % len(NumberedList)
                    Int = Index + StartWithZeroOrOne
                else:
                    pass
        printNumberedList(Int)
    # 0 = item in list, 1 = index of that item in list
    return NumberedList[IntList.index(Int)],Int-StartWithZeroOrOne
# chooseFromKeysList allows you to print and select from items in a given list
# by entering the key or moving the selector up and down with the plus and mius
# signs, or with brackets pointing left (backward) or right (forward), also
# multiple in one input. Confirm every input with the Enter key.
#
# The function requires exactly four arguments:
# the NotNumberedList: the given [list, with, the, items] to choose from
# the Keys List:       the list with all possible keys to enter on input. Both
#                      lists MUST be equal in length
# the Case:            "U"pper, "l"ower or "C"ase sensitive
# the Default Choice:  The the default option key in the KeysList
# It returns the selected item in the list and the corresponding key.
def chooseFromKeysList(NotNumberedList,KeysList,UpperOrLower,DefaultOption):
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    this = "-> "
    thisnot = "   "
    connect = " : "
    if UpperOrLower.upper() == "U":
        Option = DefaultOption.upper()
    elif UpperOrLower.lower() == "l":
        Option = DefaultOption.lower()
    else:
        Option = DefaultOption
    if len(NotNumberedList) != len(KeysList):
        print("len(NumberedList) != len(KeysList)")
        return
    def printNotNumberedList(Option):
        maxlen = len(max(KeysList,key = len))
        PrOption = KeysList[KeysList.index(Option)]
        for i in KeysList:
            if i == PrOption:
                print(this+("{:>%d}" % maxlen).format(i)+connect+str(NotNumberedList[KeysList.index(i)]))
            else:
                print(thisnot+("{:>%d}" % maxlen).format(i)+connect+str(NotNumberedList[KeysList.index(i)]))
        return Option
    printNotNumberedList(Option)
    yes = True
    while yes == True:
        if UpperOrLower.upper() == "U":
            ip = input().upper()
        elif UpperOrLower.lower() == "l":
            ip = input().lower()
        else:
            ip = input()
        if ip in KeysList:
            Option = ip
        else:
            if ip == "":
                break
            for k in ip:
                if k in nexti:
                    try:
                        Option = KeysList[KeysList.index(Option)+1]
                    except:
                        Option = KeysList[0]
                elif k in previ:
                    Option = KeysList[KeysList.index(Option)-1]
                else:
                    pass
        printNotNumberedList(Option)
    # 0 = item in list, 1 = chosen option
    return NotNumberedList[KeysList.index(Option)],Option
