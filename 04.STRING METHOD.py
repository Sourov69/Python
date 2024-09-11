str = 'congratulation stupid'
print(str.upper())                         # All capital
print(str.rstrip('stupid'))                # delet last element 
print(str.replace('stupid', 'good'))       # replace stupid into(,) good 
print(str.split(' '))                      # convert sting into list ('',_, ,-," ")
print(str.center(25))                      # centering to middle or last or firs

blogheading = "introDucTion tO jS"
print(blogheading.capitalize())            # Introduction to Js
print(blogheading.swapcase())              # convert opposite letter

b = 'wellcome to the the the console !!!' 
print(len(b))                              # length of the string b
print(b.find('console'))                   # find where this is exist
print(b.count('the'))                      # 3 times here the      
print(b.startswith('wellcome'))            # True
print(b.endswith('!!!'))                   # True
print(b.title())                           # Every first letter of any word covert into capital

# to check
# Use -isalnum(), isalpha(), islower(), istitle(), 
