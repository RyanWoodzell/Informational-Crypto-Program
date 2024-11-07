from cryptoclass import cryptoInfo
def main():
  #welcome
  print("Welcome to Ryan's CryptoCurrency Database!")
  runAgain=True

  #import data
  x=cryptoInfo()

  #while loop to run the program multiple times
  while runAgain==True:

     #user interface
    print("="*20)
    print("To find information about a specific Cryptocurrency, enter crypto name.")
    print("Press 1 for highest daily percent change")
    print("Press 2 for the lowest daily percent change")
    print("Press 3 for highest 3 month percent change.")
    print("Press 4 for lowest 3 month percent change. ")
    print("Press 5 to end program")
    a=str(input("Input: "))

    #if statements that call certain functions from the class cryptoInfo
    if a == "5":
      print("Have a Great Day!")
      break

    elif a == "4":
      x.findLowest90dChange()

    elif a == "3":
      x.findHighest90dChange()

    elif a == "2":
      x.findLowestDailyChange()

    elif a == "1":
      x.findHighestDailyChange()

    else:
      x.findCrypto(a)


    response=input("Research another Cryptocurrency? (Y/N): ")
    #ends program if user wishes
    if response.lower()!="y":
      runAgain=False
      print("Have a great day!")
      break

if __name__ == "__main__":
    main()

  
