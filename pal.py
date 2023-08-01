#Palindrome
import sys,subprocess
while True:
 n=input("Enter your text ==> ")
 print("")
 if n[::1]==n[::-1]:
     print(n,"is Palindrome")
 else:
     print(n,"is not Palindrome")
 print("")
 input("Press enter to continue...")
 subprocess.run("cls",shell=True)
