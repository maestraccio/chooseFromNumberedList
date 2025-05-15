#!/usr/bin/python
nexti = [")","}","]",">","_","+"]
previ = ["(","{","[","<","^","-"]
this = "-> "
thisnot = "   "
connect = " : "
def chooseFromNumberedList(NumberedList,StartWithZeroOrOne,DefaultOption):
    i = NumberedList[DefaultOption % len(NumberedList)-StartWithZeroOrOne]
    # print arrow+number+connector+listitem with first item on top
    # The arrow goes where the targeted number is
    def printNumberedList(i):
        for j in NumberedList:
            if i == j:
                print(this+("{:>2}").format(NumberedList.index(j)+StartWithZeroOrOne)+connect+j)
            else:
                print(thisnot+("{:>2}").format(NumberedList.index(j)+StartWithZeroOrOne)+connect+j)
    printNumberedList(i)
    yes = True
    while yes == True:
        ip = input()
        try:
            i = NumberedList[int(ip) % len(NumberedList)-StartWithZeroOrOne]
        except:
            if ip == "":
                break
            for k in ip:
                if k in nexti:
                    try:
                        i = NumberedList[NumberedList.index(i)+1]
                    except:
                        i = NumberedList[0]
                elif k in previ:
                    i = NumberedList[NumberedList.index(i)-1]
                else:
                    pass
        printNumberedList(i)
    # 0 = item in list, 1 = chosen number (not index!)
    return i,NumberedList.index(i)+StartWithZeroOrOne
