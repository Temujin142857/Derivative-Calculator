#author Tomio Nagano, temujin142857@gmail.com

def productRule(function1,function2):
    """takes two functions, each as lists of componnents, lists in the list of compnnents are a result of two variables multiplied by each other"""    
    functionD1=getDerivativeOfFunction(function1)
    functionD2=getDerivativeOfFunction(function2)
    FD1xF2=multiplyTwoFunctions(functionD1,function2)
    FD2xF1=multiplyTwoFunctions(functionD2,function1)
    unsimplified=addTwoFunctions(FD1xF2,FD2xF1)
    functionProduct=collectTerms(unsimplified)
    return functionProduct
        
                
def multiplyTwoFunctions(functionD,function):
    """list,list->list"""
    import basicBuildingBlocksD as basicFunctions
    unsimplified=basicFunctions.multiplyTwoFunctions(functionD,function)
    return unsimplified
    
def addTwoFunctions(function1,function2):
    """list,list->list"""
    import basicBuildingBlocksD as basicFunctions
    functionSum=basicFunctions.addTwoFunctions(function1,function2)
    return functionSum
            
def getDerivativeOfFunction(function):
    """list->list"""
    import basicBuildingBlocksD as basicFunctions
    functionD=basicFunctions.getDerivativeOfFunction(function)
    return functionD

def collectTerms(function):
    """list->list"""
    import collectingLikeTermsD as collect
    functionSimplified=collect.collectLikeTerms(function[0],function[1],function[2])
    return functionSimplified


function1=[[1,2],["x","x"],[2,4]]
function2=[[4,5],["x","x"],[8,10]]
import collectingLikeTermsD as collect
c,v,e=productRule(function1,function2)
print(collect.collectLikeTerms(c,v,e))
