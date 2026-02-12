s=input()
t=input()
s=s.lower()
t=t.lower()
s=s.replace(" ","")
t=t.replace(" ","")
if(len(s)!=len(t)):
  print("False")
else:
  if(sorted(s)==sorted(t)):
    print("True")
  else:
    print("False")


s=input()
t=input()
print(sorted(s)==sorted(t))
