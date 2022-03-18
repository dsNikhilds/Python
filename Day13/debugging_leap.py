year = input("Which year do you want to check?") # Debugging errors: convert str to int

if year % 4 == 0:
  if year % 100 == 0: # Debugging errors: it should be elif instead of if
    if year % 400 == 0: 
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
