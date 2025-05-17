#!/usr/bin/python

# Version 0.2
# Date 20250517
#
# This module allows you to print and select from items in a given list by
# entering the number or moving the selector up and down with the plus and mius
# signs, or with brackets pointing left (backward) or right (forward), also
# multiple in one input. Confirm every input with the Enter key.
#
# The function requires exactly four arguments:
# the list:            the given [list, with, the, items] to choose from
# the sorting method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
# the starting number: common are 0 or 1, but any positive number can be given
# the default choice:  a number in the numbering list, between the lowest and
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
            Int = int(ip)
        except(Exception) as e:
            #print(e)
            if ip == "":
                break
            for k in ip:
                if k in nexti:
                    try:
                        Int = Int+1
                    except:
                        Int = Int
                elif k in previ:
                    Int = Int-1
                else:
                    pass
        printNumberedList(Int)
    # 0 = item in list, 1 = index of that item in list
    return NumberedList[IntList.index(Int)],Int-StartWithZeroOrOne
