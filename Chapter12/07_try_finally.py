def main():
 try:
  a=int(input("Enter the number:"))
  print(a)
  return
 except Exception as e:
  print(e)
  print("there is an error")
  return
 finally:
  print("hey im inside the finally")
main()
