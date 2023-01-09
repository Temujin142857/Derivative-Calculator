#author Tomio Nagano, temujin142857@gmail.com

def quotientRule(function1,function2):
    """list,list -> list,list
        takes two functions as lists of componnents, returns two functions in the same format, one being the denominator, the other the numerator"""
    functionD1=getDerivativeOfFunction(function1)
    functionD2=getDerivativeOfFunction(function2)
    fD1xf2=multiplyTwoFunctions(functionD1,function2)
    fD2xf1=multiplyTwoFunctions(functionD2,function1)
    f2xf2=multiplyTwoFunctions(function2,function2)
    functionNumerator=subtractTwoFunctions(fD1xf2,fD2xf1)
    functionNumerator=collectTerms(functionNumerator)
    functionDenominator=collectTerms(f2xf2)    
    return functionNumerator,functionDenominator
    

def multiplyTwoFunctions(function1,function2):
    """list,list->list"""
    import basicBuildingBlocksD as basicBlocks
    unsimplified=basicBlocks.multiplyTwoFunctions(function1,function2)
    return unsimplified

def getDerivativeOfFunction(function):
    """list->list"""
    import basicBuildingBlocksD as basicBlocks
    functionD=basicBlocks.getDerivativeOfFunction(function)
    return functionD

def subtractTwoFunctions(function1,function2):
    """list,list->list"""
    import basicBuildingBlocksD as basicBlocks
    functionDifference=basicBlocks.subtractTwoFunctions(function1,function2)
    return functionDifference

def collectTerms(function):
    """list->list"""
    import collectingLikeTermsD as collect
    functionSimplified=collect.collectLikeTerms(function[0],function[1],function[2])
    return functionSimplified

function1=[[1,2],["x","x"],[2,4]]
function2=[[4,5],["x","x"],[8,10]]
numerator,denominator=quotientRule(function1,function2)
print(numerator)
print(denominator)
