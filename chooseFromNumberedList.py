#!/usr/bin/python

# Version 0.1
# Date 20250516

import random

# This module allows you to print and select from items in a given list by
# entering the number or moving the selector up and down with the plus and mius
# signs, or with brackets pointing left (back) or right (forward). Confirm every
# entry with the Enter key.
#
# The function requires exactly four arguments:
# the list:            the given [list, with, the, items] to choose from
# the sorting method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
# the starting number: common are 0 or 1, but any positive number can be given
# the default choice:  a number in the numbering list, between the lowest and
#                      the highest number in the list (inclusive)

nexti = [")","}","]",">","+"]
previ = ["(","{","[","<","-"]
this = "-> "
thisnot = "   "
connect = " : "
def chooseFromNumberedList(NumberedList,AscendingOrDescendingOrRandom,StartWithZeroOrOne,DefaultOption):
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
    
    # print arrow+number+connector+listitem
    # The arrow goes where the targeted number is (DefaultOption)
    def printNumberedList(Int):
        ValidRange = range(StartWithZeroOrOne,StartWithZeroOrOne+len(NumberedList)-1)
        Index = (Int-StartWithZeroOrOne) % len(IntList)
        if AscendingOrDescendingOrRandom.upper() == "D":
            PrInt = len(IntList)-1-IntList.index(Index+StartWithZeroOrOne)
        else:
            PrInt = IntList.index(Index+StartWithZeroOrOne)
        for i in IntList:
            if i-StartWithZeroOrOne == PrInt:
                print(this+"{:>2}".format(i)+connect+str(NumberedList[IntList.index(i)]))
            else:
                print(thisnot+"{:>2}".format(i)+connect+str(NumberedList[IntList.index(i)]))
        return Int
    printNumberedList(Int)
    yes = True
    while yes == True:
        ip = input()
        try:
            #Int = NumberedList[int(ip) % len(NumberedList)-StartWithZeroOrOne]
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
    # 0 = item in list, 1 = chosen number (not index!)
    return NumberedList[IntList.index(Int)],Int
