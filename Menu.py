from DoublyLinkedListPage import Node, DoublyLinkedList

nodey = Node(data=None)
doubList = DoublyLinkedList()

def mainMenu():

    print("Program choice key:\n" +
          "1 - for Enter number in empty list\n" +
          "2 - for Insert number at start of list\n" +
          "3 - Insert number after another number of your choice" +
          "4 - ")
    userChoice = input('Please enter your command to utilize the DoublyLinkedList: ')
    print(userChoice)

    userNumber = input('Please enter what number you would like to work with: ' )

    if userChoice == 1:
        doubList(userNumber)


mainMenu()