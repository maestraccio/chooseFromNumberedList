#!/usr/bin/python

# Version 2.10
# Date 20250608

# **chooseFromNumberedList** allows you to print and select from items in a given
# list by entering the number or moving the selector up and down with the plus
# and minus signs, or with brackets pointing left (backward) or right (forward),
# also multiple in one input. Confirm every input with the Enter key.
# The function requires one list of four, five or six elements:
# the NumberedList:    the given [list, with, the, items] to choose from
# the Sorting Method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
# the Starting Number: common are 0 or 1, but any positive number can be given
# the Default Option:  a number in the numbering list, between the lowest and
#                      the highest number in the list (inclusive)
# Optional1:           a customized indicator: Can contain a colour code
#                      (don't forget to close it with "\033[0m"!). Default
#                      string length is 3, but you can also change the length
#                      to make it stand out. If it is "O", the first three
#                      characters of the chosen key are used.
# Optional2:           A list with valid options that are not shown in the
#                      NumberedList. ATTENTION: It returns only the chosen
#                      option, twice!
# It returns the selected value and its key, except when an item from HiddenList
# is chosen.
def chooseFromNumberedList(Import):
    NumberedList =                  Import[0]
    AscendingOrDescendingOrRandom = Import[1]
    StartWithZeroOrOne =            Import[2]
    DefaultOption =                 Import[3]
    try:
        if type(Import[4]) == str:
            if Import[4].upper() == "O":
                this = "{:^3}".format(Key)[:4]
            else:
                this = Import[4]
            try:
                HiddenList = Import[5]
            except:
                HiddenList = []
        elif type(Import[4]) == list:
            this = "-> "
            HiddenList = Import[4]
        else:
            this = "-> "
            try:
                HiddenList = Import[5]
            except:
                HiddenList = []
    except:
        this = "-> "
        HiddenList = []
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
            break
        except(Exception) as e:
            #print(e)
            if ip in HiddenList:
                return ip,ip
            elif ip == "":
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
# The function requires one list of four, five or six elements:
# the NotNumberedList: the given [list, with, the, items] to choose from
# the Keys List:       the list with all possible keys to enter on input. Both
#                      lists MUST be equal in length
# the Case:            "U"pper, "l"ower or "C"ase sensitive
# the Default Choice:  The the default option key in the KeysList
# Optional1:           a customized indicator: Can contain a colour code
#                      (don't forget to close it with "\033[0m"!). Default
#                      string length is 3, but you can also change the length
#                      to make it stand out. If it is "O", the first three
#                      characters of the chosen key are used.
# Optional2:           A list with valid options that are not shown in the
#                      KeysList. ATTENTION: It returns only the chosen option,
#                      twice!
# It returns the selected value and its key, except when an item from HiddenList
# is chosen.
def chooseFromKeysList(Import):
    NotNumberedList = Import[0]
    KeysList =        Import[1]
    UpperOrLower =    Import[2]
    DefaultOption =   Import[3]
    try:
        if type(Import[4]) == str:
            if Import[4].upper() == "O":
                this = "{:^3}".format(Key)[:4]
            else:
                this = Import[4]
            try:
                HiddenList = Import[5]
            except:
                HiddenList = []
        elif type(Import[4]) == list:
            this = "-> "
            HiddenList = Import[4]
        else:
            this = "-> "
            try:
                HiddenList = Import[5]
            except:
                HiddenList = []
    except:
        this = "-> "
        HiddenList = []
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
        if ip in HiddenList:
            return ip,ip
        elif ip in KeysList:
            Option = ip
            break 
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
# Confirm every input with the Enter key.
# The function requires one list of two, three or four elements:
# the List:            the given [list, with, the, items] to choose from
# the Default Option:  an index number in the List
# Optional1:           a customized indicator: Can contain a colour code
#                      (don't forget to close it with "\033[0m"!). Default
#                      string length is 3, but you can also change the length
#                      to make it stand out. If it is "O", the first three
#                      characters of the chosen key are used.
# Optional2:           A list with valid options that are not shown in the
#                      List. ATTENTION: It returns only the chosen option, twice!
# It returns the selected value and its key, except when an item from HiddenList
# is chosen.
def chooseFromList(Import):
    List = Import[0]
    Int =  Import[1]
    try:
        if type(Import[2]) == str:
            if Import[2].upper() == "O":
                this = "{:^3}".format(Key)[:2]
            else:
                this = Import[2]
            try:
                HiddenList = Import[3]
            except:
                HiddenList = []
        elif type(Import[2]) == list:
            this = "-> "
            HiddenList = Import[2]
        else:
            this = "-> "
            try:
                HiddenList = Import[3]
            except:
                HiddenList = []
    except:
        this = "-> "
        HiddenList = []
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    thisnot = "   "
    connect = " : "
    def printList(Int):
        Index = Int
        for i in List:
            if List.index(i) == Int:
                print(this+str(i))
            else:
                print(thisnot+str(i))
        return Int
    printList(Int)
    yes = True
    while yes == True:
        ip = input()
        if ip in HiddenList:
            return ip,ip
        elif ip == "":
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

# **chooseFromDictionary** allows you to print and select from items in a given
# dictionary by entering (a fragment of) the key or moving the selector up and
# down with the plus and minus signs, or with brackets pointing left (backward)
# or right (forward), also multiple in one input. Confirm every input with the
# Enter key.
# The function requires one list of three, four or five elements:
# the Dictionary:     the given dictionary with the keys and values to choose
#                     from.
# the Showing option: The line with the indicator is always printed, plus:
#                     0: don't show a line if its value is ""
#                     1: print all lines, buf if its value is "", print only the
#                     key
#                     2: print all lines, including the connector and the empty
#                     value
#                     3: print only the lines with an empty value
#                     the Default Option: an existing key in the dictionary
# Optional1:          a customized indicator: Can contain a colour code (don't
#                     forget to close it with "\033[0m"!). Default string length
#                     is 3, but you can also change the length to make it stand
#                     out. If it is "O", the first three characters of the chosen
#                     key are used.
# Optional2:          A list with valid options that are not shown in the
#                     Dictionary. ATTENTION: It returns only the chosen option,
#                     twice!
# It returns the selected value and its key, except when an item from HiddenList
# is chosen.
def chooseFromDictionary(Import):
    Dictionary =    Import[0]
    ShowEmpty =     Import[1]
    DefaultOption = Import[2]
    try:
        if type(Import[3]) == str:
            if Import[3].upper() == "O":
                this = "{:^3}".format(Key)[:3]
            else:
                this = Import[3]
            try:
                HiddenList = Import[4]
            except:
                HiddenList = []
        elif type(Import[3]) == list:
            this = "-> "
            HiddenList = Import[3]
        else:
            this = "-> "
            try:
                HiddenList = Import[4]
            except:
                HiddenList = []
    except:
        this = "-> "
        HiddenList = []
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    thisnot = "   "
    connect = " : "
    Key = DefaultOption
    IList = []
    JList = []
    for i,j in Dictionary.items():
        IList.append(i)
        JList.append(j)
    def printDictionary(Key):
        KeysList = []
        for i in IList:
            KeysList.append(str(i))
        maxlen = len(max(KeysList,key = len))
        for i in IList:
            if ShowEmpty == 0:
                if i == Key:
                    print(this+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                elif str(JList[IList.index(i)]) == "":
                    pass
                else:
                    print(thisnot+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
            elif ShowEmpty == 1:
                if i == Key:
                    print(this+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                elif str(JList[IList.index(i)]) == "":
                    print(thisnot+("{:>%d}" % maxlen).format(i))
                else:
                    print(thisnot+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
            elif ShowEmpty == 2:
                if i == Key:
                    print(this+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                else:
                    print(thisnot+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
            else:
                if i == Key:
                    print(this+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                elif str(JList[IList.index(i)]) == "":
                    print(thisnot+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                else:
                    pass
        return Key
    printDictionary(Key)
    yes = True
    while yes == True:
        NewKey = input()
        if NewKey == "":
            break
        elif NewKey in HiddenList:
            return NewKey,NewKey
        for j in IList:
            if NewKey in j:
                Key = j
                yes = False
                break
        for k in NewKey:
            if k in nexti:
                Key = IList[(IList.index(Key) + 1) % len(Dictionary)]
            elif k in previ:
                Key = IList[(IList.index(Key) - 1) % len(Dictionary)]
        printDictionary(Key)
    # 0 = item in Dictionary, 1 = Key of that item in Dictionary
    return Dictionary[Key],Key

#ExampleList = [
#        "Als",
#        2,
#        "Catania",
#        None,
#        "Etna",
#        "Fakkelt"
#        ]
#ExampleKeysList = [
#        "A",
#        "B",
#        "C",
#        "D",
#        "E",
#        "F"
#        ] 
#ExampleDictionary = {
#        "A": "Als",
#        "B": None,
#        "C": "",
#        "D": True,
#        "E": "Etna",
#        "F": "Fakkelt"
#        }
#ExampleHiddenList = [
#        ":q",
#        ":u",
#        ":w"
#        ]
#what, where = chooseFromNumberedList([ExampleList, "D", 0, 2])
#print(what, where)
#what, where = chooseFromKeysList([ExampleList, ExampleKeysList, "U", "c"])
#print(what, where)
#what, where = chooseFromList([ExampleList, 0, "---"])
#print(what, where)
#what, where = chooseFromDictionary([ExampleDictionary, 1, "B", "\033[32m"+">- "+"\033[0m",ExampleHiddenList])
#print(what, where)
