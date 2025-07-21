#!/usr/bin/python

# Version 2.36
# Date 20250721

#**chooseFromNumberedList** allows you to print and select from items in a given
#list by entering the number or moving the selector up and down with the plus
#and minus signs, or with a series of brackets pointing left (lower options) or
#right (higher options).
#The function requires one list of (min) four to (max) eight elements:
#the NumberedList:    the given [list, with, the, items] to choose from
#the Sorting Method:  "A" = Ascending, "D" = Descending, "R" = Random (LOL)
#the Starting Number: common are 0 or 1, but any positive number can be given
#the Default Option:  a number in the numbering list, between the lowest and
#                     the highest number in the list (inclusive)
#Optional1 (string):  a customized indicator: Can contain a colour code
#                     (don't forget to close it with "\033[0m"!). Default
#                     string length is 3, but you can also change the length
#                     to make it stand out. If it is "O", the first three
#                     characters of the chosen key are used.
#Optional2 (list):    A list with valid options that are not shown in the
#                     NumberedList - recommended for repeating exit options.
#                     ATTENTION: It returns only the chosen option, twice!
#Optional3 (integer): 0: move the indicator to the chosen position and wait for
#                        the next input, accept only on "Enter" (except for
#                        options in the optional "HiddenList", which are always
#                        immediately accepted).
#                     1: immediately accept the input if the input is a valid
#                        option (default if omitted)
#Optional4 (boolean): True:  MultipleChoice: Create a list of chosen items.
#                            Items can be added in one comma separated input,
#                            or one-by-one, or both.
#                     False: Accept only one choice. This is the default.
#It returns the selected item in the list and its index number in that list,
#unless MultipleChoice is True. In that case two lists, one with items and the
#other with indexes, are returned.
def chooseFromNumberedList(Import):
    NumberedList =                  Import[0] # provide as list
    AscendingOrDescendingOrRandom = Import[1] # provide as str
    StartWithZeroOrOne =            Import[2] # provide as int
    DefaultOption =                 Import[3] # provide as int
    DefaultIndicator =              "-> "     # provide as str,  Import[4]
    DefaultHiddenList =             []        # provide as list, Import[4] or Import[5]
    DefaultAccept =                 1         # provide as int,  Import[4] or Import[5] or Import[6]
    DefaultMultChoice =             False     # provide as bool, Import[4] or Import[5] or Import[6] or Import[7]
    Indicator =  DefaultIndicator 
    HiddenList = DefaultHiddenList
    Accept =     DefaultAccept
    MultChoice = DefaultMultChoice
    LenOpt =     len(Import) - 4
    if len(Import) == 4:
        pass
    else:
        Optionals =  Import[-LenOpt:]
        for i in Optionals:
            if type(i) == str:
                Indicator = i
            elif type(i) == list:
                HiddenList = i
            elif type(i) == int:
                Accept = i
            elif type(i) == bool:
                MultChoice = i

    nexti     = [")","}","]",">","+"]
    previ     = ["(","{","[","<","-"]
    Outicator = "   "
    connect   = " : "
    Int = DefaultOption
    Index = Int - StartWithZeroOrOne
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
    StrList = []
    for i in IntList:
        StrList.append(str(i))
    maxlen = len(max(StrList,key = len))
    def printNumberedList(Int,Indicator):
        if Indicator.upper() == "O":
            Indicator = "{:^3}".format(Int)[:3]
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
    IndexList = []
    MultChoiceList = []
    WaitForEnter = False
    yes = True
    while yes == True:
        ip = input().strip()
        if MultChoice == True:
            iplist = ip.split(",")
            if ip == "":
                Index = (Int - StartWithZeroOrOne) % len(NumberedList)
                if Index not in IndexList:
                    IndexList.append(Index)
                    MultChoiceList.append(NumberedList[Index])
                if Accept == 0:
                    if WaitForEnter == True:
                        WaitForEnter = False
                    else:
                        return MultChoiceList,IndexList
                else:
                    return MultChoiceList,IndexList
            elif ip in HiddenList:
                return ip,ip
            else:
                try:
                    ipi = int(ip)
                    Index = (int(ip) - StartWithZeroOrOne) % len(NumberedList)
                    Int = Index + StartWithZeroOrOne
                    if Index not in IndexList:
                        IndexList.append(Index)
                        MultChoiceList.append(NumberedList[Index])
                    if Accept == 0:
                        pass
                    else:
                        return MultChoiceList,IndexList
                except:
                    for i in iplist:
                        ipt = i.strip()
                        try:
                            ipi = int(i)
                            Index = (ipi - StartWithZeroOrOne) % len(NumberedList)
                            Int = Index + StartWithZeroOrOne
                            if Index not in IndexList:
                                IndexList.append(Index)
                                MultChoiceList.append(NumberedList[Index])
                        except:
                            for k in i:
                                if k in nexti:
                                    try:
                                        Index += 1
                                        NumberedList[Index]
                                    except:
                                        Index = 0
                                    WaitForEnter = True
                                elif k in previ:
                                    Index -= 1
                                    if Index == -1:
                                        Index = len(NumberedList)-1
                                    WaitForEnter = True
                                Int = Index+StartWithZeroOrOne
                    if WaitForEnter == True:
                        pass
                    else:
                        if Accept == 0:
                            pass
                        else:
                            return MultChoiceList,IndexList
            if len(IndexList) != 0:
                print("-"*(maxlen+len(Outicator)+1)+"+"+"-"*(len(Outicator)))
                for i in IndexList:
                    print("%s : %s" % (("{:>%d}" % (maxlen+len(Outicator))).format(i+StartWithZeroOrOne),NumberedList[i]))
                print("-"*(maxlen+len(Outicator)+1)+"+"+"-"*(len(Outicator)))
        else:
            try:
                Index = (int(ip) - StartWithZeroOrOne) % len(NumberedList)
                Int = Index + StartWithZeroOrOne
                if Accept == 1:
                    return NumberedList[IntList.index(Int)],Int-StartWithZeroOrOne
            except:
                if ip in HiddenList:
                    return ip,ip
                for k in ip:
                    if k in nexti:
                        Index = (Int - StartWithZeroOrOne + 1) % len(NumberedList)
                        Int = Index + StartWithZeroOrOne
                    elif k in previ:
                        Index = (Int - StartWithZeroOrOne - 1) % len(NumberedList)
                        Int = Index + StartWithZeroOrOne
                if ip == "":
                    return NumberedList[IntList.index(Int)],Int-StartWithZeroOrOne
        printNumberedList(Int,Indicator)
    # 0 = item in list, 1 = index of that item in list

#**chooseFromKeysList** allows you to print and select from items in a given
#list by entering the number or moving the selector up and down with the plus
#and minus signs, or with a series of brackets pointing left (lower options) or
#right (higher options).
#The function requires one list of (min) four to (max) eight elements:
#the NotNumberedList: the given [list, with, the, items] to choose from
#the Keys List:       the list with all possible keys to enter on input. Both
#                     lists MUST be equal in length
#the Case:            "U"pper, "l"ower or "C"ase sensitive
#the Default Choice:  The the default option key in the KeysList
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
#Optional4 (boolean): True:  MultipleChoice: Create a list of chosen items.
#                            Items can be added in one comma separated input,
#                            or one-by-one, or both.
#                     False: Accept only one choice. This is the default.
#It returns the selected item in the list and its corresponding key, unless
#MultipleChoice is True. In that case two lists, one with items and the other
#with keys, are returned.
def chooseFromKeysList(Import):
    NotNumberedList =               Import[0] # provide as list
    KeysList =                      Import[1] # provide as list
    UpperOrLower =                  Import[2] # provide as str
    DefaultOption =                 Import[3] # provide as str
    DefaultIndicator =              "-> "     # provide as str,  Import[4]
    DefaultHiddenList =             []        # provide as list, Import[4] or Import[5]
    DefaultAccept =                 1         # provide as int,  Import[4] or Import[5] or Import[6]
    DefaultMultChoice =             False     # provide as bool, Import[4] or Import[5] or Import[6] or Import[7]
    Indicator =  DefaultIndicator 
    HiddenList = DefaultHiddenList
    Accept =     DefaultAccept
    MultChoice = DefaultMultChoice
    LenOpt =     len(Import) - 4
    if len(Import) == 4:
        pass
    else:
        Optionals =  Import[-LenOpt:]
        for i in Optionals:
            if type(i) == str:
                Indicator = i
            elif type(i) == list:
                HiddenList = i
            elif type(i) == int:
                Accept = i
            elif type(i) == bool:
                MultChoice = i
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
    maxlen = len(max(KeysList,key = len))
    def printNotNumberedList(Option,Indicator):
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
    MCList = []
    IndexList = []
    MultChoiceList = []
    WaitForEnter = False
    yes = True
    while yes == True:
        if UpperOrLower.upper() == "U":
            ip = input().upper().strip()
        elif UpperOrLower.lower() == "l":
            ip = input().lower().strip()
        else:
            ip = input().strip()
        if MultChoice == True:
            iplist = ip.split(",")
            if ip == "":
                Index = KeysList.index(Option)
                if Option not in MCList:
                    MCList.append(Option)
                    MultChoiceList.append(NotNumberedList[Index])
                if Accept == 0:
                    if WaitForEnter == True:
                        WaitForEnter = False
                    else:
                        return MultChoiceList,MCList
                else:
                    return MultChoiceList,MCList
            elif ip in HiddenList:
                return ip,ip
            elif ip in KeysList:
                Option = ip
                Index = KeysList.index(Option)
                if Option not in MCList:
                    MCList.append(Option)
                    MultChoiceList.append(NotNumberedList[Index])
                if Accept == 0:
                    pass
                else:
                    return MultChoiceList,MCList
            else:
                for i in iplist:
                    ipt = i.strip()
                    if ipt in KeysList:
                        Option = ipt
                        Index = KeysList.index(Option)
                        if Option not in MCList:
                            MCList.append(Option)
                            IndexList.append(Index)
                            MultChoiceList.append(NotNumberedList[Index])
                    else:
                        for k in i:
                            if k in nexti:
                                try:
                                    Index = KeysList.index(Option)+1
                                    KeysList[Index]
                                except:
                                    Index = 0
                                Option = KeysList[Index]
                                WaitForEnter = True
                            elif k in previ:
                                Index = KeysList.index(Option)-1
                                Option = KeysList[Index]
                                WaitForEnter = True
                if Accept == 0:
                    if WaitForEnter == True:
                        WaitForEnter = False
                    else:
                        if Option not in MCList:
                            MCList.append(Option)
                            IndexList.append(Index)
                            MultChoiceList.append(NotNumberedList[Index])
                        return MultChoiceList,MCList
                else:
                    if Option not in MCList:
                        MCList.append(Option)
                        IndexList.append(Index)
                        MultChoiceList.append(NotNumberedList[Index])
                    return MultChoiceList,MCList
            if len(MCList) != 0:
                print("-"*(maxlen+len(Outicator)+1)+"+"+"-"*(len(Outicator)))
                for i in MCList:
                    print("%s : %s" % (("{:>%d}" % (maxlen+len(Outicator))).format(i),MultChoiceList[MCList.index(i)]))
                print("-"*(maxlen+len(Outicator)+1)+"+"+"-"*(len(Outicator)))
        else:
            if ip in HiddenList:
                return ip,ip
            elif ip in KeysList:
                Option = ip
                if Accept == 1:
                    return NotNumberedList[KeysList.index(Option)],Option
            else:
                if ip == "":
                    return NotNumberedList[KeysList.index(Option)],Option
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

#**chooseFromList** allows you to print and select from items in a given list by
#entering the number or moving the selector up and down with the plus and minus
#signs, or with a series of brackets pointing left (lower options) or right
#(higher options).
#The function requires one list of (min) two to (max) six elements:
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
#Optional3 (integer): 0: move the indicator to the chosen position and wait for
#                        the next input, accept only on "Enter" (except for
#                        options in the optional "HiddenList", which are always
#                      immediately accepted). Only relevant if MultipleChoice
#                      is True
#                   1: immediately accept the input if the input is a valid
#                        option (default if omitted)
#Optional4 (boolean): True:  MultipleChoice: Create a list of chosen items.
#                            Items can be added in one comma separated input,
#                            or one-by-one, or both.
#                     False: Accept only one choice. This is the default.
#It returns the selected item in the list and its index number in that list,
#unless MultipleChoice is True. In that case two lists, one with items and the
#other with indexes, are returned.
def chooseFromList(Import):
    List =              Import[0] # provide as list
    Int =               Import[1] # provide as int
    DefaultIndicator =  "-> "     # provide as str,  Import[2]
    DefaultHiddenList = []        # provide as list, Import[2] or Import[3]
    DefaultAccept =     1         # provide as int,  Import[2] or Import[3] or Import[4]
    DefaultMultChoice = False     # provide as bool, Import[2] or Import[3] or Import[4] or Import[5]
    Indicator =  DefaultIndicator 
    HiddenList = DefaultHiddenList
    Accept =     DefaultAccept
    MultChoice = DefaultMultChoice
    LenOpt =     len(Import) - 2
    if len(Import) == 2:
        pass
    else:
        Optionals =  Import[-LenOpt:]
        for i in Optionals:
            if type(i) == str:
                Indicator = i
            elif type(i) == list:
                HiddenList = i
            elif type(i) == int:
                Accept = i
            elif type(i) == bool:
                MultChoice = i
    nexti = [")","}","]",">","+"]
    previ = ["(","{","[","<","-"]
    Outicator = "   "
    connect = " : "
    def printList(Int,Indicator):
        if Indicator.upper() == "O":
            try:
                Indicator = "{:^3}".format(List[Int])[:2] + " "
            except:
                Indicator = "{:^3}".format(Int)[:2] + " "
        Index = Int
        for i in List:
            if List.index(i) == Int:
                print(Indicator+str(i))
            else:
                print(Outicator+str(i))
        return Int
    printList(Int,Indicator)
    IndexList = []
    MultChoiceList = []
    yes = True
    WaitForEnter = False
    while yes == True:
        ip = input().strip()
        if ip in HiddenList:
            return ip,ip
        if MultChoice == True:
            if ip == "":
                if Int not in IndexList:
                    IndexList.append(Int)
                    MultChoiceList.append(List[Int])
                if Accept == 0:
                    if WaitForEnter == True:
                        WaitForEnter = False
                    else:
                        return MultChoiceList,IndexList
                else:
                    if Int not in IndexList:
                        IndexList.append(Int)
                        MultChoiceList.append(List[Int])
                    return MultChoiceList,IndexList
            for k in ip:
                if k in nexti:
                    Index = (Int + 1) % len(List)
                    Int = Index
                    WaitForEnter = True
                elif k in previ:
                    Index = (Int - 1) % len(List)
                    Int = Index
                    WaitForEnter = True
            if len(IndexList) != 0:
                print("+"+"-"*(len(Outicator)))
                for i in IndexList:
                    print(" %s" % (List[i]))
                print("+"+"-"*(len(Outicator)))
        else:
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
            # 0 = item in list, 1 = index of that item in list
            return List[Int],Int
        printList(Int,Indicator)

#**chooseFromDictionary** allows you to print and select from items in a given
#dictionary by entering the number or moving the selector up and down with the
#plus and minus signs, or with a series of brackets pointing left (lower
#options) or right (higher options).
#The function requires one list of (min) three to (max) seven elements:
#the Dictionary:     the given dictionary with the keys and values to choose
#                    from.
#the Showing option: The line with the indicator is always printed, plus:
#                    0: don't show a line if its value is ""
#                    1: print all lines, buf if its value is "", print only the
#                       key
#                    2: print all lines, including the connector and the empty
#                       value
#                    3: print only the lines with an empty value
#the Default Option: an existing key in the dictionary
#Optional1 (string): a customized indicator: Can contain a colour code (don't
#                    forget to close it with "\033[0m"!). Default string length
#                    is 3, but you can also change the length to make it stand
#                    out. If it is "O", the first three characters of the chosen
#                    key are used.
#Optional2 (list):   A list with valid options that are not shown in the
#                    Dictionary - recommended for repeating exit options.
#                    ATTENTION: It returns only the chosen option,
#                    twice!
#Optional3 (integer): 0: move the indicator to the chosen position and wait for
#                        the next input, accept only on "Enter" (except for
#                        options in the optional "HiddenList", which are always
#                        immediately accepted).
#                     1: immediately accept the input if the input is a valid
#                        option (default if omitted)
#Optional4 (boolean): True:  MultipleChoice: Create a list of chosen items.
#                            Items can be added in one comma separated input,
#                            or one-by-one, or both.
#                     False: Accept only one choice. This is the default.
#It returns the selected item in the list and its corresponding key, unless
#MultipleChoice is True. In that case two lists, one with items and the other
#with keys, are returned.
def chooseFromDictionary(Import):
    Dictionary =        Import[0] # provide as dict
    ShowEmpty =         Import[1] # provide as int
    DefaultOption =     Import[2] # provide as str
    DefaultIndicator =  "-> "     # provide as str,  Import[3]
    DefaultHiddenList = []        # provide as list, Import[3] or Import[4]
    DefaultAccept =     1         # provide as int,  Import[3] or Import[4] or Import[5]
    DefaultMultChoice = False     # provide as bool, Import[3] or Import[4] or Import[5] or Import[6]
    Indicator =  DefaultIndicator 
    HiddenList = DefaultHiddenList
    Accept =     DefaultAccept
    MultChoice = DefaultMultChoice
    LenOpt =     len(Import) - 3
    if len(Import) == 3:
        pass
    else:
        Optionals =  Import[-LenOpt:]
        for i in Optionals:
            if type(i) == str:
                Indicator = i
            elif type(i) == list:
                HiddenList = i
            elif type(i) == int:
                Accept = i
            elif type(i) == bool:
                MultChoice = i
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
    maxlen = len(max(IList,key = len))
    def printDictionary(Key,Indicator):
        KeysList = []
        for i in IList:
            KeysList.append(str(i))
        maxlen = len(max(KeysList,key = len))
        for i in IList:
            if Indicator.upper() == "O":
                if i == Key:
                    try:
                        Indicator = "{:^3}".format(JList[IList.index(i)])[:3]
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
    print(Key)
    printDictionary(Key,Indicator)
    MCList = []
    MultChoiceList = []
    IndexList = []
    WaitForEnter = False
    yes = True
    while yes == True:
        NewKey = input().strip()
        NewKeyList = NewKey.split(",")
        if MultChoice == True:
            if NewKey in HiddenList:
                return NewKey,NewKey
            else:
                if NewKey == "":
                    Index = IList.index(Key)
                    if WaitForEnter == True:
                        if Key not in MCList:
                            MCList.append(IList[Index])
                            IndexList.append(Index)
                            MultChoiceList.append(JList[Index])
                        WaitForEnter = False
                    else:
                        if Key not in MCList:
                            MCList.append(IList[Index])
                            IndexList.append(Index)
                            MultChoiceList.append(JList[Index])
                        return MultChoiceList,MCList
                else:
                    for k in NewKey:
                        if k in nexti:
                            try:
                                Index = IList.index(Key)+1
                                IList[Index]
                            except:
                                Index = IList.index(DefaultOption)
                            Key = IList[Index]
                            WaitForEnter = True
                        elif k in previ:
                            Index = IList.index(Key)-1
                            Key = IList[Index]
                            WaitForEnter = True
                    if Accept == 0:
                        pass
                    else:
                        if NewKey in IList:
                            if NewKey not in MCList:
                                Index = IList.index(NewKey)
                                MCList.append(NewKey)
                                IndexList.append(Index)
                                MultChoiceList.append(JList[Index])
                    for j in NewKeyList:
                        if j in IList:
                            Index = IList.index(j)
                            NewKey = j
                            if NewKey not in MCList:
                                MCList.append(NewKey)
                                IndexList.append(Index)
                                MultChoiceList.append(JList[Index])
                    if Accept == 0:
                        pass
                    else:
                        return MultChoiceList,MCList
                    if NewKey in IList:
                        if NewKey not in MCList:
                            MCList.append(IList[Index])
                            IndexList.append(Index)
                            MultChoiceList.append(JList[Index])
                            if Accept == 0:
                                pass
                            else:
                                return MultChoiceList,MCList
                    if Accept == 0:
                        pass
                    else:
                        return MultChoiceList,MCList
            if len(MCList) != 0:
                print("-"*(maxlen+len(Outicator)+1)+"+"+"-"*(len(Outicator)))
                for i in MCList:
                    print("%s : %s" % (("{:>%d}" % (maxlen+len(Outicator))).format(i),MultChoiceList[MCList.index(i)]))
                print("-"*(maxlen+len(Outicator)+1)+"+"+"-"*(len(Outicator)))
        else:
            if NewKey == "":
                break
            elif NewKey in HiddenList:
                return NewKey,NewKey
            for j in IList:
                if NewKey in j:
                    Key = j
                    if Accept == 1:
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
#        "Bij",
#        "Catania",
#        "De",
#        "Etna",
#        "Fakkelt"
#        ]
#TestKeysList = [
#        "A",
#        "BB",
#        "CCC",
#        "D",
#        "E",
#        "F"
#        ] 
#TestDictionary = {
#        "A": "Als",
#        "B": None,
#        "C": "Catania",
#        "D": "",
#        "E": "Etna",
#        "F": "Fakkelt"
#        }
#TestHiddenList = [
#        ":Q",
#        ":U",
#        ":W",
#        ":q",
#        ":u",
#        ":w"
#        ]
#Import = [TestList,"A",1,1,"O",TestHiddenList,0,True]
#for i in Import:
#    print(type(i), i)
#what, where = chooseFromNumberedList(Import)
#print(what, where)
#Import = [TestList, TestKeysList, "U", TestKeysList[2], ">+-", TestHiddenList, 1,False]
#for i in Import:
#    print(type(i), i)
#what, where = chooseFromKeysList(Import)
#print(what, where)
#Import = [TestList, 0, "\033[32m"+"---"+"\033[0m", TestHiddenList, 1, True]
#for i in Import:
#    print(type(i), i)
#what, where = chooseFromList(Import)
#print(what, where)
#Import = [TestDictionary, 1, "B", "O",TestHiddenList,0,True]
#for i in Import:
#    print(type(i), i)
#what, where = chooseFromDictionary(Import)
#print(what, where)
