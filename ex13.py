list = [5 ,4,7,3,2,8,1,0]

def bleh(list):
    blehlebleh = []
    for x in list:
        if x not in blehlebleh:
            blehlebleh.append(x)
    for x in blehlebleh:
        print(x)

bleh(list)