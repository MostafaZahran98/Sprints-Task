string = "abracadabra" #this is the string that we will work on it
def mut(s,i,charac) : #function to mutate in the string
    string1 = list(s) #converting the string to a list in order to change it
    string1[i] = charac #replacing the charcater with a given index
    print (string1) # printing the string after changing it

print ("this is the string before the mutation : "+ string)

print ("this is the string after the mutation" )
mut(string , 5 , 'k')
