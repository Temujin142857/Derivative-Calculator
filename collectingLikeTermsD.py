#Author Tomio Nagano, temujin142857@gmail.com

def collectLikeTerms(coefficients,variables,exponnents):
    """list,list,list -> list,list,list
        Coordinates other functions to return three lists having collected the like terms"""
    variablesE=list(map(addL,variables,exponnents))
    dictionary={}
    for i in range(0,len(variablesE)):
        buildDictionary(dictionary,variablesE[i],coefficients[i])
    newVariablesE=[]
    newCoefficients=[]
    newExponnents=[]
    newVariables=[]
    dictionaryToLists(dictionary,newVariablesE,newCoefficients)
    splitList(newVariablesE,newVariables, newExponnents)
    return newCoefficients,newVariables,newExponnents

def buildDictionary(dictionary,element1,element2):
    """dict,object,object -> NONE
        adds an element to a dictionary, using another element as the key"""
    try:
        coefficient=dictionary[element1]
    except:
        coefficient=0
    dictionary[element1]=coefficient+element2

def splitList(list1,list2,list3):
    """list -> NONE
        takes the numbers from list1 and adds them to list2, adds the letters to list3"""
    for s in list1:
        for i in range(0,len(s)):
            if s[i].isdigit():
                list2.append(s[:i])
                list3.append(s[i:])
                break            
    
def addL(variable, exponnent):
    """str,int -> str
        Takes variable and exponnent as any object that can be converted directly to str, returns thier combined string"""
    if type(variable)==list:
        return variable + exponnent
    else:
        return str(variable) + str(exponnent)
     

def dictionaryToLists(dictionary,keys,values):
    """list,list -> NONE
        stores the keys in the first list, and the values in the second"""
    for e in dictionary:
        keys.append(e)        
        values.append(dictionary[e])       

   
"""coefficients=[14,2,3,4,5,6]
variables=["x","x","z","z","y","y"]
exponnents=[51,2,1,1,3,3]
print(collectLikeTerms(coefficients,variables,exponnents))"""

 
