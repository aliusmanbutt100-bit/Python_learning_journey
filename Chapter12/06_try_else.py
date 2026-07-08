try:
  a=int(input("Enter the number:"))
  print(a)
except Exception as e:
  print(e)
  print("there is an error")
else:
  print("hey im in the else")
# when try runs successfully it goes into the else 