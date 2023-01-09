#Author Tomio Nagano, temujin142857@gmail.com
#basicBuildingBlocksD contains functions that the Rule programs use for their calculations

def multiplyTwoFunctions(function1,function2):
    unsimplified=[],[],[]
    for i in range(0,len(function1[0])):
        for j in range(0,len(function2[0])):
            unsimplified[0].append(function1[0][i]*function2[0][j])#mulitplies the coefficients, they are now dealt with
            if function1[1][i]==function2[1][j]:
                unsimplified[1].append(function1[1][i])
                unsimplified[2].append(function1[2][i]+function2[2][j])
            elif function1[2][i]==0:
                unsimplified[1].append(function2[1][i])
                unsimplified[2].append(function2[2][i])
            elif function2[2][i]==0:
                unsimplified[1].append(function1[1][i])
                unsimplified[2].append(function2[2][i])
            else:                
                unsimplified[1].append(list([function1[1][i],function2[1][j]]))
                unsimplified[2].append(list([function1[2][i],function2[2][j]]))
    return unsimplified

def getDerivativeOfFunction(function):
    functionD=[],[],[]
    for i in range(0,len(function[0])):
        c,e=powerRule(function[0][i],function[2][i])
        functionD[0].append(c)
        functionD[1].append(function[1][i])
        functionD[2].append(e)        
    return functionD


def addTwoFunctions(function1,function2):
    function1[0].extend(function2[0])
    function1[1].extend(function2[1])
    function1[2].extend(function2[2])
    return function1

def subtractTwoFunctions(function1,function2):
    for i in range(0,len(function2[0])):
        function2[0][i]=function2[0][i]*-1
    Difference=addTwoFunctions(function1,function2)
    return Difference
                   


def powerRule(oldC,oldE):
    """float,float->float,float
        takes the exponnent and coefficient of a nomial, and applies power rule"""
    if oldE==0:
        return oldC,oldE
    newC = oldE*oldC
    newE = oldE-1
    return newC,newE
