#!/usr/bin/python

# Version 2.20
# Date 20250608

# **chooseFromNumberedList** allows you to print and select from items in a given
# list by entering the number or moving the selector up and down with the plus
# and minus signs, or with brackets pointing left (backward) or right (forward),
# also multiple of those in one input.
# The function requires one list of (min) four to (max) seven elements:
# the NumberedList:    the given [list, with, the, items] to choose from
# the Sorting Method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
# the Starting Number: common are 0 or 1, but any positive number can be given
# the Default Option:  a number in the numbering list, between the lowest and
#                      the highest number in the list (inclusive)
# Optional1 (string):  a customized indicator: Can contain a colour code
#                      (don't forget to close it with "\033[0m"!). Default
#                      string length is 3, but you can also change the length
#                      to make it stand out. If it is "O", the first three
#                      characters of the chosen key are used.
# Optional2 (list):    A list with valid options that are not shown in the
#                      NumberedList - recommended for repeating exit options.
#                      ATTENTION: It returns only the chosen option, twice!
# Optional3 (integer): 0: move the indicator to the chosen position and wait for
#                         the next input, accept only on "Enter" (except for
#                         options in the optional "HiddenList", which are always
#                         immediately accepted).
#                      1: immediately accept the input if the input is a valid
#                         option (default if omitted)
# It returns the selected item in the list and its index number in that list.
def chooseFromNumberedList(Import):
    NumberedList =                  Import[0] # provide as list
    AscendingOrDescendingOrRandom = Import[1] # provide as str
    StartWithZeroOrOne =            Import[2] # provide as int
    DefaultOption =                 Import[3] # provide as int
    DefaultIndicator =              "-> "     # provide as str,  Import[4]
    DefaultHiddenList =             []        # provide as list, Import[4] or Import[5]
    DefaultAccept =                 True      # provide as int,  Import[4] or Import[5] or Import[6]
    # Import[4]
    try:
        if type(Import[4]) == str:
                Indicator = Import[4]
    except:
        Indicator =  DefaultIndicator
    try:
        if type(Import[4]) == list:
            HiddenList = Import[4]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    try:
        if type(Import[4]) == int:
            if Import[4] == 0:
                Accept == False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    # Import[5]
    try:
        if type(Import[5]) == list:
            HiddenList = Import[5]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    try:
        if type(Import[5]) == int:
            if Import[5] == 0:
                Accept == False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    # Import[6]
    try:
        if type(Import[6]) == int:
            if Import[6] == 0:
                Accept = False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    nexti     = [")","}","]",">","+"]
    previ     = ["(","{","[","<","-"]
    Outicator = "   "
    connect   = " : "
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
    def printNumberedList(Int,Indicator):
        if Indicator.upper() == "O":
            Indicator = "{:^3}".format(Int)[:3]
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
                print(Indicator+("{:>%d}" % maxlen).format(i)+connect+str(NumberedList[IntList.index(i)]))
            else:
                print(Outicator+("{:>%d}" % maxlen).format(i)+connect+str(NumberedList[IntList.index(i)]))
        return Int
    printNumberedList(Int,Indicator)
    yes = True
    while yes == True:
        ip = input()
        try:
            Index = (int(ip) - StartWithZeroOrOne) % len(NumberedList)
            Int = Index + StartWithZeroOrOne
            if Accept == True:
                break
        except:
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
        printNumberedList(Int,Indicator)
    # 0 = item in list, 1 = index of that item in list
    return NumberedList[IntList.index(Int)],Int-StartWithZeroOrOne

#**chooseFromKeysList** allows you to print and select from items in a given list
#by entering the key or moving the selector up and down with the plus and minus
#signs, or with brackets pointing left (backward) or right (forward), also
#multiple of those in one input.
#The function requires one list of (min) four to (max) seven elements:
#the NotNumberedList: the given [list, with, the, items] to choose from
#the Keys List:       the list with all possible keys to enter on input. Both
#                     lists MUST be equal in length
#                     the Case:            "U"pper, "l"ower or "C"ase sensitive
#                     the Default Choice:  The the default option key in the KeysList
#Optional1 (string):  a customized indicator: Can contain a colour code
#                     (don't forget to close it with "\033[0m"!). Default
#                     string length is 3, but you can also change the length
#                     to make it stand out. If it is "O", the first three
#                     characters of the chosen key are used.
#Optional2 (list):    A list with valid options that are not shown in the
#                     KeysList - recommended for repeating exit options.
#                     ATTENTION: It returns only the chosen option, twice!
#Optional3 (integer): 0: move the indicator to the chosen position and wait for
#                        the next input, accept only on "Enter" (except for
#                        options in the optional "HiddenList", which are always
#                        immediately accepted).
#                     1: immediately accept the input if the input is a valid
#                        option (default if omitted)
#It returns the selected item in the list and the corresponding key.
def chooseFromKeysList(Import):
    NotNumberedList =               Import[0] # provide as list
    KeysList =                      Import[1] # provide as list
    UpperOrLower =                  Import[2] # provide as str
    DefaultOption =                 Import[3] # provide as str
    DefaultIndicator =              "-> "     # provide as str,  Import[4]
    DefaultHiddenList =             []        # provide as list, Import[4] or Import[5]
    DefaultAccept =                 True      # provide as int,  Import[4] or Import[5] or Import[6]
    # Import[4]
    try:
        if type(Import[4]) == str:
                Indicator = Import[4]
    except:
        Indicator =  DefaultIndicator
    try:
        if type(Import[4]) == list:
            HiddenList = Import[4]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    try:
        if type(Import[4]) == int:
            if Import[4] == 0:
                Accept == False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    # Import[5]
    try:
        if type(Import[5]) == list:
            HiddenList = Import[5]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    try:
        if type(Import[5]) == int:
            if Import[5] == 0:
                Accept == False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    # Import[6]
    try:
        if type(Import[6]) == int:
            if Import[6] == 0:
                Accept = False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    Outicator = "   "
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
    def printNotNumberedList(Option,Indicator):
        maxlen = len(max(KeysList,key = len))
        PrOption = KeysList[KeysList.index(Option)]
        for i in KeysList:
            if i == PrOption:
                if Indicator.upper() == "O":
                    try:
                        Indicator = "{:^3}".format(NotNumberedList[KeysList.index(i)])[:3]
                    except:
                        Indicator = "{:^3}".format(i)[:3]
                print(Indicator+("{:>%d}" % maxlen).format(i)+connect+str(NotNumberedList[KeysList.index(i)]))
            else:
                print(Outicator+("{:>%d}" % maxlen).format(i)+connect+str(NotNumberedList[KeysList.index(i)]))
        return Option
    printNotNumberedList(Option,Indicator)
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
            if Accept == True:
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
        printNotNumberedList(Option,Indicator)
    # 0 = item in list, 1 = chosen option
    return NotNumberedList[KeysList.index(Option)],Option

#**chooseFromList** allows you to print and select from items in a given list by
#moving the selector up and down with the plus and minus signs, or with brackets
#pointing left (backward) or right (forward), also multiple of those in one
#input.
#The function requires one list of (min) two to (max) four elements:
#the List:            the given [list, with, the, items] to choose from
#the Default Option:  an index number in the List
#Optional1 (string):  a customized indicator: Can contain a colour code
#                     (don't forget to close it with "\033[0m"!). Default
#                     string length is 3, but you can also change the length
#                     to make it stand out. If it is "O", the first three
#                     characters of the chosen key are used.
#Optional2 (list):    A list with valid options that are not shown in the
#                     List - recommended for repeating exit options. ATTENTION:
#                     It returns only the chosen option, twice!
#It returns the selected item in the list and its index number in that list.
def chooseFromList(Import):
    List =              Import[0] # provide as list
    Int =               Import[1] # provide as str
    DefaultIndicator =  "-> "     # provide as str,  Import[2]
    DefaultHiddenList = []        # provide as list, Import[2] or Import[3]
    # Import[2]
    try:
        if type(Import[2]) == str:
                Indicator = Import[2]
    except:
        Indicator =  DefaultIndicator
    try:
        if type(Import[2]) == list:
            HiddenList = Import[2]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    # Import[3]
    try:
        if type(Import[3]) == list:
            HiddenList = Import[3]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    Outicator = "   "
    connect = " : "
    def printList(Int,Indicator):
        if Indicator.upper() == "O":
            try:
                Indicator = "{:^3}".format(List[Int])[:3]
            except:
                Indicator = "{:^3}".format(Int)[:3]
        Index = Int
        for i in List:
            if List.index(i) == Int:
                print(Indicator+str(i))
            else:
                print(Outicator+str(i))
        return Int
    printList(Int,Indicator)
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
        printList(Int,Indicator)
    # 0 = item in list, 1 = index of that item in list
    return List[Int],Int

# **chooseFromDictionary** allows you to print and select from items in a given
# dictionary by entering (a fragment of) the key or moving the selector up and
# down with the plus and minus signs, or with brackets pointing left (backward)
# or right (forward), also multiple of those in one input.
# The function requires one list of (min) three to (max) six elements:
# the Dictionary:     the given dictionary with the keys and values to choose
#                     from.
# the Showing option: The line with the indicator is always printed, plus:
#                     0: don't show a line if its value is ""
#                     1: print all lines, buf if its value is "", print only the
#                        key
#                     2: print all lines, including the connector and the empty
#                        value
#                     3: print only the lines with an empty value
#                     the Default Option: an existing key in the dictionary
# Optional1 (string): a customized indicator: Can contain a colour code (don't
#                     forget to close it with "\033[0m"!). Default string length
#                     is 3, but you can also change the length to make it stand
#                     out. If it is "O", the first three characters of the chosen
#                     key are used.
# Optional2 (list):   A list with valid options that are not shown in the
#                     Dictionary - recommended for repeating exit options.
#                     ATTENTION: It returns only the chosen option,
#                     twice!
# Optional3 (integer): 0: move the indicator to the chosen position and wait for
#                         the next input, accept only on "Enter" (except for
#                         options in the optional "HiddenList", which are always
#                         immediately accepted).
#                      1: immediately accept the input if the input is a valid
#                         option (default if omitted)
# It returns the selected value and its key.
def chooseFromDictionary(Import):
    Dictionary =        Import[0] # provide as dict
    ShowEmpty =         Import[1] # provide as int
    DefaultOption =     Import[2] # provide as int
    DefaultIndicator =  "-> "     # provide as str,  Import[4]
    DefaultHiddenList = []        # provide as list, Import[4] or Import[5]
    DefaultAccept =     True      # provide as int,  Import[4] or Import[5] or Import[6]
    # Import[3]
    try:
        if type(Import[3]) == str:
                Indicator = Import[3]
    except:
        Indicator =  DefaultIndicator
    try:
        if type(Import[3]) == list:
            HiddenList = Import[3]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    try:
        if type(Import[3]) == int:
            if Import[3] == 0:
                Accept == False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    # Import[5]
    try:
        if type(Import[4]) == list:
            HiddenList = Import[4]
        else:
            HiddenList = DefaultHiddenList
    except:
        HiddenList = DefaultHiddenList
    try:
        if type(Import[4]) == int:
            if Import[4] == 0:
                Accept == False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
    # Import[6]
    try:
        if type(Import[5]) == int:
            if Import[5] == 0:
                Accept = False
            else:
                Accept = DefaultAccept
    except:
        Accept = DefaultAccept
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
    nexti =     [")","}","]",">","+"]
    previ =     ["(","{","[","<","-"]
    Outicator = "   "
    connect =   " : "
    Key =       DefaultOption
    IList =     []
    JList =     []
    for i,j in Dictionary.items():
        IList.append(i)
        JList.append(j)
    def printDictionary(Key,Indicator):
        KeysList = []
        for i in IList:
            KeysList.append(str(i))
        maxlen = len(max(KeysList,key = len))
        for i in IList:
            if Indicator == "O":
                try:
                    Indicator = "{:^3}".format(JList[i])[:3]
                except:
                    Indicator = "{:^3}".format(i)[:3]
            if ShowEmpty == 0:
                if i == Key:
                    print(Indicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                elif str(JList[IList.index(i)]) == "":
                    pass
                else:
                    print(Outicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
            elif ShowEmpty == 1:
                if i == Key:
                    print(Indicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                elif str(JList[IList.index(i)]) == "":
                    print(Outicator+("{:>%d}" % maxlen).format(i))
                else:
                    print(Outicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
            elif ShowEmpty == 2:
                if i == Key:
                    print(Indicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                else:
                    print(Outicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
            else:
                if i == Key:
                    print(Indicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                elif str(JList[IList.index(i)]) == "":
                    print(Outicator+("{:>%d}" % maxlen).format(i)+connect+str(JList[IList.index(i)]))
                else:
                    pass
        return Key
    printDictionary(Key,Indicator)
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
                if Accept == True:
                    yes = False
                    break
        for k in NewKey:
            if k in nexti:
                Key = IList[(IList.index(Key) + 1) % len(Dictionary)]
            elif k in previ:
                Key = IList[(IList.index(Key) - 1) % len(Dictionary)]
        printDictionary(Key,Indicator)
    # 0 = item in Dictionary, 1 = Key of that item in Dictionary
    return Dictionary[Key],Key

#TestList = [
#        "Als",
#        2,
#        "Catania",
#        None,
#        "Etna",
#        "Fakkelt"
#        ]
#TestKeysList = [
#        "A",
#        "B",
#        "C",
#        "D",
#        "E",
#        "F"
#        ] 
#TestDictionary = {
#        "A": "Als",
#        "B": None,
#        "C": "",
#        "D": True,
#        "E": "Etna",
#        "F": "Fakkelt"
#        }
#TestHiddenList = [
#        ":q",
#        ":u",
#        ":w"
#        ]
#what, where = chooseFromNumberedList([TestList, "D", 2, 2, "O", TestHiddenList, 1])
#print(what, where)
#what, where = chooseFromKeysList([TestList, TestKeysList, "U", "c", "O", TestHiddenList, 1])
#print(what, where)
#what, where = chooseFromList([TestList, 0, "\033[32m"+"---"+"\033[0m", TestHiddenList, 1])
#print(what, where)
#what, where = chooseFromDictionary([TestDictionary, 1, "B", "o",TestHiddenList,0])
#print(what, where)
