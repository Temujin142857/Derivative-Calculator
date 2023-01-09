#author Tomio Nagano, temujin142857@gmail.com
import operator


def getInput():
    print("Naming rules:\nPlease write any subtractiion as the addition of a negative.\nPlease use ^ for exponnents")
    eRough=input("What's the equation?")
    return eRough

def detectQuestion(eRough):
    if eRough.conatains("\*"):
        functions = eRough.split("\*")
        return functions,"product"
    elif eRough.contains("/"):
        functions = eRough.split("/")
        return functions,"quotient"

def getNomials(function):
    """str -> list
        takes a polynomial equation and splits it by addition"""
    if function.contains("\+"):
        nomials = function.split("\+")      
    return nomials

def getPriority(function):
    i=len(function)-1
    count=0
    depth=-1
    while i in range(0,len(function)) and function.contains(")"):
        if !mark:
            depth=depth+1
        if function[i]==")":
            count=count+1            
        if function[i]=="(":
            count=count-1                   
        if function[i]=="(" and depth==0:
            start=i
            function[depth].append(function[start:])
            if start !=0:
                operator[depth].append(function[start-1])
                getPriority(function[:start])
            #read operator at functtion[end+1]
        i=i-1
        

def readOperator():
    if operator=="*":
        
    elif operator=="/":

    elif operator=="^":

    elif operator=="+":

    elif operator=="-":
        
        

def splitNomials(nomials):
    """list -> list,list,list
        takes a list of strings containing nomials made up of a coefficient, a variable, and an exponnent
        splits each nomial into it's three componnents and returns a list for each componnent"""
    coefficients=[]
    exponnents=[]
    variables=[]
    for n in nomials:
        nomial=splitNomial(n)
        coefficients.append(nomial[0])
        exponnents.append(nomial[1])
        variables.append(nomial[2])
            
    return coefficients,variables,exponnents

def splitNomial(nomial):
    """str -> str,str,str
        takes a nomial and returns it's coefficient, variable, and exponnent"""
    for c in nomial:
            if c.isalpha():
                temp=nomial.split(c)
                coefficient=temp[0]
                exponnent=temp[1]
                variable=c
    return coefficient,variable,exponnent


def collectTerms(coefficients,variables,exponnents):
    """list,list,list -> list, list,list
        takes three lists and uses program collectingLikeTermsD to collect the like terms"""
    import collectingLikeTermsD as collect
    return collect.collectLikeTerms(coefficients,variables,exponnents)

def productRule(function1,function2):
    """list,list -> list,list,list
        takes two functions as lists each containing three lists, coefficients, veriables, exponnents
        uses program productRuleD to do this"""
    import productRuleD as productR
    return productR.productRule(function1,function2)

def quotientRule(function1,function2):
    return

def chainRule(function1,function2):
    return temp

Equation={}
question=getInput()





