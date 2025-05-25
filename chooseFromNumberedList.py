#!/usr/bin/python

# Version 1.01
# Date 20250525

# **chooseFromNumberedList** allows you to print and select from items in a given
# list by entering the number or moving the selector up and down with the plus
# and minus signs, or with brackets pointing left (backward) or right (forward),
# also multiple in one input. Confirm every input with the Enter key.
# The function requires one list of four or five elements:
# the NumberedList:    the given [list, with, the, items] to choose from
# the Sorting Method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
# the Starting Number: common are 0 or 1, but any positive number can be given
# the Default Option:  a number in the numbering list, between the lowest and
#                      the highest number in the list (inclusive)
# Optional:            a customized indicator: Can contain a colour code (don't
#                      forget to close it with "\033[0m"!). Default string length
#                      is 3, but you can also change the length to make it stand
#                      out.
# It returns the selected item in the list and its index number in that list.
def chooseFromNumberedList(Import):
    NumberedList =                  Import[0]
    AscendingOrDescendingOrRandom = Import[1]
    StartWithZeroOrOne =            Import[2]
    DefaultOption =                 Import[3]
    try:
        this = Import[4]
    except:
        this = "-> "
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    thisnot = "   "
    connect = " : "
    Int = DefaultOption
    IntList = []
    if AscendingOrDescendingOrRandom.upper() == "D":
        for item in NumberedList:
            IntList.append(len(NumberedList)-NumberedList.index(item)+StartWithZeroOrOne-1)
    elif AscendingOrDescendingOrRandom.upper() == "R":
        import random
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

# **chooseFromKeysList** allows you to print and select from items in a given list
# by entering the key or moving the selector up and down with the plus and minus
# signs, or with brackets pointing left (backward) or right (forward), also
# multiple in one input. Confirm every input with the Enter key.
# The function requires one list of four or five elements:
# the NotNumberedList: the given [list, with, the, items] to choose from
# the Keys List:       the list with all possible keys to enter on input. Both
#                      lists MUST be equal in length
# the Case:            "U"pper, "l"ower or "C"ase sensitive
# the Default Choice:  The the default option key in the KeysList
# Optional:            a customized indicator: Can contain a colour code (don't
#                      forget to close it with "\033[0m"!). Default string length
#                      is 3, but you can also change the length to make it stand
#                      out.
# It returns the selected item in the list and the corresponding key.
def chooseFromKeysList(Import):
    NotNumberedList = Import[0]
    KeysList =        Import[1]
    UpperOrLower =    Import[2]
    DefaultOption =   Import[3]
    try:
        this = Import[4]
    except:
        this = "-> "
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
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

# **chooseFromList** allows you to print and select from items in a given list by
# moving the selector up and down with the plus and minus signs, or with brackets
# pointing left (backward) or right (forward), also multiple in one input.
# Confirm every input with the Enter key.  The function requires one list of two
# or three elements:
# the List:            the given [list, with, the, items] to choose from
# the Default Option:  an index number in the List
# Optional:            a customized indicator: Can contain a colour code (don't
#                      forget to close it with "\033[0m"!). Default string length
#                      is 3, but you can also change the length to make it stand
#                      out.
# It returns the selected item in the list and its index number in that list.
def chooseFromList(Import):
    List = Import[0]
    Int =  Import[1]
    try:
        this = Import[2]
    except:
        this = "-> "
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    thisnot = "   "
    connect = " : "
    def printList(Int):
        Index = Int
        for i in List:
            if List.index(i) == Int:
                print(this+i)
            else:
                print(thisnot+i)
        return Int
    printList(Int)
    yes = True
    while yes == True:
        ip = input()
        if ip == "":
            break
        for k in ip:
            if k in nexti:
                Index = (Int + 1) % len(List)
                Int = Index
            elif k in previ:
                Index = (Int - 1) % len(List)
                Int = Index
            else:
                pass
        printList(Int)
    # 0 = item in list, 1 = index of that item in list
    return List[Int],Int
