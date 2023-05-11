def checkBalancedBrackets(brackets):
    counter= 0
    answer=False
    for i in brackets:
        if i == "(" or i == "{" or i == "[":
            counter +=1
        elif i == ")" or i == "}" or i == "]":
            counter-= 1
        if counter < 0:
            return answer
    if counter==0:
        return not answer
    return answer
while True:
    brackets = input("Please Enter the string of brackets you want to check: ")
    if(checkBalancedBrackets(brackets)==True):
        print("Yes! The brackets is balanced")
    if(checkBalancedBrackets(brackets)==False):
        print("No! The brackets is not balanced")

    answer=input("if you want to check more brackets write continue if you want to stop write stop ")
    if(answer=="continue"):
       continue
    if(answer=="stop"):
        break