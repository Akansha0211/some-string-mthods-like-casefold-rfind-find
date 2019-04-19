# 1. casefold()
'''The casefold() method is removes all case distinctions present in a string. It is used for caseless matching, i.e. ignores cases when comparing.
casefold() Parameters
The casefold() method doesn't take any parameters.'''


str=input("Enter a string")
print(str.casefold())                                                          

#Application of casefold()
#comparision using casefold()
str1="i lOve MaGgiE"
str2="I LoVe mAGGIE"
if str1.casefold()==str2.casefold():
    print("strings are equal")
else:
    print("strings are not equal")

# 2. rfind()
'''The rfind() method returns the highest index of the substring (if found). If not found, it returns -1.'''
str=input("Enter a string")
result=str.rfind('ha')
print(result)
if result!=-1:
    print("Highest index:",result)
else:
    print("String not found")
# rfind() with start and end argument
str="Akansha Bharadwaj"
result=str.rfind('ha',2,7)
print(result)

# 3.  use of find() and casefold() together
'''The find() method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.'''
str=input("Enter a string")
str_changed=str.casefold()
result=str_changed.find('ha')
print(result)
if result!=-1:
    print("lowest index:",result)
else:
    print("String not found")
