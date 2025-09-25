print("Prime numbers between 1 to 10 are: ")
print(1,3,5,7)
print("It is fun")
print("Total joy")
print("Blissed out")

print("String palindrome")
def is_palindrome():
 x=eval(input("Enter a string to cheak:"))

 if x==x[::-1]:
   return True
 else:
   return False

print("String palindrome:", is_palindrome)

def is_anagram():
  s1= input("Enter the first string:")
  s2=input("Enter the seconfd string:")

  s1= "".join(s1.lower().split())
  s2= "".join(s2.lower().split())

  if sorted(s1)==sorted(s2):
    return True
  else:
    return False