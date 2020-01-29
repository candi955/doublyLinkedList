# Github repository: https://github.com/candi955/doublyLinkedList

# This module is being utilized as a set-up and conceptuality page for the doubly-linked list concept.  A user can call
# the various functions from the class DoublyLinkedList() to implement various doubly-linked list processes.
# The output at this time fulfills the requirements of MS549 project Linked List, Phase 1, Testing, as well as the
# insertion and deletion of random numbers.

# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

# Another reference that was not used for this project but could be used for future projects that are similar:
# https://www.tutorialcup.com/linked-list/delete-node-without-head.htm


# 1/19/2020 @ 15:10 - This assignment is for MS549, Project: Linked List.  Initially I was attempting to either 'reinvent
# the wheel' and create an entirely new programming code for the doubly linked list in python.  I began to realize that
# all of the training online or in books appeared to be in a template format.  The formats did not seem to sway much
# from each other, and there appeared to be little room for individuality within the foundational code utilized
# to create a double-linked list.
# As I came to this conclusion, I re-read the assignment instructions and noticed that it appeared to stated the linked
# list class 'should be implemented using generics', and even mentioned the utilization of templates.  I found the
# below generic template code for python doubly linked lists at the following reference:
# https://stackabuse.com/doubly-linked-list-with-python-examples/
# I created a Main() class at the bottom of my code, and as per the initial code template by StackAbuse, I initialized
# a variable to stand for the DoublyLinkedList() class, named new_linked_list.
# I practiced traversing the list with a copy of an example from the referenced StackAbuse website, and now am ready to
# begin the project by implementing various functionality including Find, Insert, Remove (data), Remove (node), and
# Print.
# 1/19/2020 @ 19:21 - I have begun working on the Menu page for the user-menu.
# 1/20/2020 @ 01:58 pm - I just realized that I might have done a little more than the assignment asked by creating
# my Menu.py module program for a user, but I'm glad I did in that the concept might be a useful template for future
# list-building projects of which I wish to have user-interaction when it comes to list creation or modification.  It
# was a good learning experience.
# Now I am going to continue with the last parts of the project, with random number addition and deletion and timing
# of these processes (on the DoublyLinkedListPage.py module.   I will then video my project and turn it in.

# importing 'random' due to the random integers required for the final phase of the project
# also importing 'time' in order to implement timing of the various random number experiments at the end of the
# project, concerning arrays versus lists (timing comparisons of number insert and number deletion between both
# types of lists)
# 1/21/2020 @ 14:24pm - I have completed creating the creation/deletion, and timing of such functionality concerning
# the doubly linked lists of 100, 1000, and 10000 random numbers. Importing matplotlib.pyplot as plt to help with
# the creation of the table.

import random
import time
import numpy as np
import pandas as pd


# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
Node(data=None)

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    # inserting data into an empty list (Insert at end of list)
    def insert_in_emptylist(self, data):
            if self.start_node is None:
                new_node = Node(data)
                self.start_node = new_node
            else:
                print("list is not empty")


    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n


    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node


    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;

     # deleting elements at the end of the list
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    # deleting elements by value
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    # Reversing a doubly linked list
    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

    # Attempting to create a function for 'find'
    def find_element_by_value(self, x):

        # for checking first node and finding the beginning number
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                print('Item found.')

            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            print("The number", x, "is the first number located on the list.")
            self.start_node = self.start_node
            self.start_node.pref = None
            return
        # for finding the middle numbers
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                print("The number", x, "is one of the numbers located in the middle of the list.")
                break
            n = n.nref

        # for finding the end number
        if n.nref is not None:
            #n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                print("The number", x, "is the last number on the list.")
            else:
                print("Element not found")

    def delete_AllElementsOfList(self, object):

        for i in object:
            if i + 1:
                while True:
                    try:


                        if self.start_node is None:
                            print("The list has no element to delete")
                            return
                        if self.start_node.nref is None:
                            self.start_node = None
                            return
                        self.start_node = self.start_node.nref
                        self.start_prev = None;

                    except ValueError:
                        print('There has been an error')
                    else:
                        break

DoublyLinkedList()


# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

class Main():

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced
    new_linked_list = DoublyLinkedList()


    # Showing that the list is empty
    print("Printing the empty list:")
    printEmptyStart = time.time()
    new_linked_list.traverse_list()
    printEmptyEnd = time.time()
    printEmptyDuration = printEmptyEnd - printEmptyStart
    print('\nThe time duration for printing an empty doubly linked list is: ', printEmptyDuration)

    print('\n')


    # From the StackAbuse example being referenced, inserting the number 50 into the list (technically at the end of the list
    print("Adding the number 50 to the empty list:")
    Adding50Start = time.time()
    new_linked_list.insert_in_emptylist(50)
    Adding50End = time.time()
    Adding50Duration = Adding50End - Adding50Start
    new_linked_list.traverse_list()
    print('\nThe time duration for adding 50 numbers to an empty doubly linked list is: ', Adding50Duration)
    print('\n')

    # From the StackAbuse example being referenced, inserting the numbers 10, 5, and then 18 to the beginning of the list
    print("Adding the numbers 10, then 5, then 18 to beginning of the list:")
    new_linked_list.insert_at_start(10), new_linked_list.insert_at_start(5), new_linked_list.insert_at_start(18)
    new_linked_list.traverse_list()
    print('\n')

    print("Inserting 300 to the end of the list, to fulfill 'insert at end of list by creating a new node at end of list':")
    new_linked_list.insert_at_end(300)
    new_linked_list.traverse_list()
    print('\n')

    print("Demonstrating removing node specified via value (pointer/reference); will remove the value 50 from the list:")
    new_linked_list.delete_element_by_value(50)
    new_linked_list.traverse_list()
    print('\n')

    print("Finding the number 300 to fulfill the assignment 'finding an element by value:")
    new_linked_list.find_element_by_value(300)
    print('\n')


    print("Finding the number 5 to fulfill the assignment 'finding an element by value:")
    new_linked_list.find_element_by_value(5)
    print('\n')


    print("Finding the number 10 to fulfill the assignment 'finding an element by value:")
    new_linked_list.find_element_by_value(10)
    print('\n')

    print("Finding the number 18 to fulfill the assignment 'finding an element by value:")
    new_linked_list.find_element_by_value(18)
    print('\n')


    print("Attempting to find a number not actually on the list (number 4) to fulfill the assignment 'finding an element by value:")
    new_linked_list.find_element_by_value(4)
    print('\n')

    # Changing the list to an empty list
    print("Deleting four numbers from the list, one-by-one:")
    deleteFourStart = time.time()
    new_linked_list.delete_element_by_value(10), new_linked_list.delete_element_by_value(5), new_linked_list.delete_element_by_value(18),
    new_linked_list.delete_element_by_value(300)
    deleteFourEnd = time.time()
    deleteFourDuration = deleteFourEnd - deleteFourStart
    new_linked_list.traverse_list()
    print('\nThe amount of time it takes to delete four numbers from the doubly link list, to empty it, one-by-one ' +
          ', is:', deleteFourDuration)
    print('\n')

    print("Now that the list is empty, will try to find the value 300:")
    new_linked_list.find_element_by_value(300)
    print('\n')

    print("Attempting to create a new list of (6, 3, 50, 10, 300, 1) utilizing insert_at_start, insert_after_item, and insert_at_end:")
    new_linked_list.insert_at_start(6), new_linked_list.insert_after_item(6, 3), new_linked_list.insert_after_item(3, 50),
    new_linked_list.insert_after_item(50, 10), new_linked_list.insert_after_item(10, 300), new_linked_list.insert_at_end(1)
    new_linked_list.traverse_list()
    print('\n')

# __________________________________________________________________________________________________________________

    # Beginning the testing phase of the project
    # I will be timing how long it takes to create arrays versus linked lists of random numbers, as well as how
    # long it takes to delete the numbers.  I have decided to use the same amount of numbers for sampling, in case
    # sampling might be a factor in the time (I will use 10,001, as the greatest amount of numbers I will choose
    # for this experiment is 10,000, and I have to choose at least one more number (10,001), in order for the
    # sampling to work in that case.  I understand proportion might also play some factor, but for the purposes of
    # this experiment, maintaining integrity of sampling numbers across the various components should satisfy the
    # requirements.

# **************************************************************************************************************
    print('********************************************************************************************************' +
          '********************************************************************************************************')

    print('Starting my experiments with array lists of 100 random numbers by creating array list array100:')
    start_time100 = time.time()
    array100 = np.array(random.sample(range(1, 101), 100))
    end_time100 = time.time()
    duration100create = end_time100 - start_time100
    print(array100)
    print('\n')

    # Creating an array list of 100 numbers, and then clearing it all at once # creating and deleting new100
    new100 = np.array(random.sample(range(1, 101), 100))
    print('A new list of 100 random numbers, called new100: ', new100)
    startDelete100 = time.time()
    new100cleared = new100[0:0]
    endDelete100 = time.time()
    durationDelete100 = endDelete100 - startDelete100
    print("Printing the deleted array of 100 random numbers, cleared all at once using slice (new100[0:0]):", new100cleared)
    print('\n')

    # deleting the array list of 100 random numbers using np.delete and slice # deleting array100
    startDeleteSlice100 = time.time()
    anotherClearedList = np.delete(array100, np.s_[::],)
    endDeleteSlice100 = time.time()
    durationDeleteSlice100 = endDeleteSlice100 - startDeleteSlice100

    print('Printing the original list I created, array100, as cleared via np.delete and slice (np.delete(array100, np.s_[::],) : ', anotherClearedList)
    print('\n')

    # creating another random list of 100 and attempting slice in a different way to delete # myOther100array
    myOther100array = np.array(random.sample(range(1, 101), 100))
    print('Here is another list of 100 random integers called myOther100array:', myOther100array)
    print('\n')
    # deleting and timing the deletion of the elements from the array using slice
    startDeleteAnotherArray = time.time()
    myOther100array = myOther100array[99:0]
    endDeleteAnotherArray = time.time()
    durationDeleteAnotherArray = endDeleteAnotherArray - startDeleteAnotherArray
    print('Here is is myOther100array with all elements deleted using a form of slice myOther100array[99:0]:', myOther100array)
    print('\n')



    # printing all of the timing durations of the random 100 number array lists
    print("The duration of time it took to create an array list of 100 random numbers (array100), using np.array(random.sample(range(1, 101), 100)): ", duration100create)
    print('\n')

    print("The duration of time it took to delete the entire entire list, called newlist, array of 100 random " +
          "numbers using slice new100[0:0]: ", durationDelete100)
    print("The duration of time it took to delete the entire entire array100 list, the original array of 100 random numbers, " +
          "using np.delete and slice (np.delete(array100, np.s_[::],): ", durationDeleteSlice100)
    print("The duration of time it took to delete the entire entire myOther100 array list " +
        "myOther100array[99:0]: ", durationDeleteAnotherArray)
    print('\n')



# **************************************************************************************************************

    print('____________________________________________________________________________________________________')
    # Starting my experiments with array lists of 1000 random numbers:
    print('Starting my experiments with array lists of 1000 random numbers are as follows.')
    print('Printing the list array1000:')
    start_time1000 = time.time()
    array1000 = np.array(random.sample(range(1, 1001), 1000))
    end_time1000 = time.time()
    duration1000create = end_time1000 - start_time1000
    print(array1000)
    print('\n')

    # deleting and timing the deletion of 1000 elements from the array using slice
    startDeleteArray1000 = time.time()
    array1000 = array1000[99:0]
    endDeleteArray1000 = time.time()
    durationDeleteArray1000 = endDeleteArray1000 - startDeleteArray1000
    print('Here is is the array list array1000 with all elements deleted using a form of slice array1000[99:0]:', array1000)
    print('\n')


    # printing the timing durations of the random 1000 number array list creation and deletion
    print("The duration of time it took to create an array list of 1000 random numbers (array1000), using np.array " +
          "(random.sample(range(1, 1001), 1000)): ", duration1000create)
    print('\n')

    print("The duration of time it took to delete the entire entire the array1000 array list " +
        "array1000[99:0]: ", durationDeleteArray1000)
    print('\n')


# **************************************************************************************************************
    print('____________________________________________________________________________________________________')
    # Starting my experiments with array lists of 10,000 random numbers:
    print('Starting my experiments with array lists of 10,000 random numbers are as follows.')
    print('Printing the list array10000:')
    start_time10000 = time.time()
    array10000 = np.array(random.sample(range(1, 10001), 10000))
    end_time10000 = time.time()
    duration10000create = end_time10000 - start_time10000
    print(array10000)
    print('\n')

    # deleting and timing the deletion of 1000 elements from the array using slice
    startDeleteArray10000 = time.time()
    array10000 = array10000[99:0]
    endDeleteArray10000 = time.time()
    durationDeleteArray10000 = endDeleteArray10000 - startDeleteArray10000
    print('Here is is the array list array10000 with all elements deleted using a form of slice array10000[99:0]:', array10000)
    print('\n')


    # printing the timing durations of the random 10000 number array list creation and deletion
    print("The duration of time it took to create an array list of 10000 random numbers (array10000), using np.array " +
          "(random.sample(range(1, 10001), 10000)): ", duration10000create)
    print('\n')

    print("The duration of time it took to delete the entire entire the array10000 array list " +
        "array10000[99:0]: ", durationDeleteArray10000)
    print('\n')

###

    # **************************************************************************************************************
    print('____________________________________________________________________________________________________')
    # Starting my experiments with array lists of 100,000 random numbers:
    print('Starting my experiments with array lists of 100,000 random numbers are as follows.')
    print('Printing the list array100,000:')
    start_time100000 = time.time()
    array100000 = np.array(random.sample(range(1, 100001), 100000))
    end_time100000 = time.time()
    duration100000create = end_time100000 - start_time100000
    print(array100000)
    print('\n')

    # deleting and timing the deletion of 100,000 elements from the array using slice
    startDeleteArray100000 = time.time()
    array100000 = array100000[99:0]
    endDeleteArray100000 = time.time()
    durationDeleteArray100000 = endDeleteArray100000 - startDeleteArray100000
    print('Here is is the array list array100000 with all elements deleted using a form of slice array100000[99:0]:',
          array100000)
    print('\n')

    # printing the timing durations of the random 100,000 number array list creation and deletion
    print("The duration of time it took to create an array list of 100,000 random numbers (array100000), using np.array " +
          "(random.sample(range(1, 100001), 100000)): ", duration100000create)
    print('\n')

    print("The duration of time it took to delete the entire entire the array100,000 array list " +
          "array100000[99:0]: ", durationDeleteArray100000)
    print('\n')

    # **************************************************************************************************************
    print('********************************************************************************************************' +
          '********************************************************************************************************')

    print('\n\nStarting my experiments with doubly linked lists of 100 random numbers by creating doublylinked list linkedList100:')

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced

    # The variables for the variable main utilization, doubly linked list classes with associated functions
    linkedList100 = DoublyLinkedList()

    # Showing that the doubly linked list linkedList100 is empty
    print("Printing the empty doubly linked list linkedList100:")
    linkedList100.traverse_list()
    print('\n')


    # Inserting 100 random numbers into linkedList100
    print("Inserting 100 random numbers into doubly linked list, linkedList100: ")
    startLinkedList100 = time.time()
    randomNums100 = np.array(random.sample(range(1, 101), 100))
    linkedList100.insert_in_emptylist(randomNums100)
    endLinkedList100 = time.time()
    durationLinkedList100 = endLinkedList100 - startLinkedList100
    linkedList100.traverse_list()
    print('\n')

    # Reference for attempting deletion:
    # https://www.geeksforgeeks.org/delete-occurrences-given-key-doubly-linked-list/


    # deleting and timing the deletion of 1000 elements from mynewlinkedList100
    startDeleteLinked100 = time.time()
    linkedList100.delete_AllElementsOfList(randomNums100)
    endDeleteLinked100 = time.time()
    durationDeleteLinked100 = endDeleteLinked100 - startDeleteLinked100
    print('Here is the list, linkedList100, after calling the function delete_AllElementsOfList():')
    linkedList100.traverse_list()
    print('\n')


    # Printing the timing durations of the random 1000 number array list creation and deletion
    print("The duration of time it took to create a doubly linked list of 100 random numbers (linkedList100), using " +
          "the function insert_in_emptylist: ", durationLinkedList100)
    print('\n')

    print("The duration of time it took to delete the entire entire the mynewLinkedList100 doubly linked list " +
        "the function delete_AllElementsOfList: ", durationDeleteLinked100)
    print('\n')

    # **************************************************************************************************************
    # Beginning to insert 1000 random numbers into a doubly linked list, and then delete all and time all of the various
    # functionalities

    print('____________________________________________________________________________________________________')

    print('Starting my experiments with doubly linked lists of 1000 random numbers by creating doublylinked list linkedList1000:')

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced

    # The variables for the variable main utilization, doubly linked list classes with associated functions
    linkedList1000 = DoublyLinkedList()

    # Showing that the doubly linked list linkedList1000 is empty
    print("Printing the empty doubly linked list linkedList1000:")
    linkedList1000.traverse_list()
    print('\n')


    # Inserting 1000 random numbers into linkedList1000
    print("Inserting 1000 random numbers into doubly linked list, linkedList1000: ")
    startLinkedList1000 = time.time()
    randomNums1000 = np.array(random.sample(range(1, 1001), 1000))
    linkedList1000.insert_in_emptylist(randomNums1000)
    endLinkedList1000 = time.time()
    durationLinkedList1000 = endLinkedList1000 - startLinkedList1000
    linkedList1000.traverse_list()
    print('\n')

    # Reference for attempting deletion:
    # https://www.geeksforgeeks.org/delete-occurrences-given-key-doubly-linked-list/


    # deleting and timing the deletion of 1000 elements from mynewlinkedList1000
    startDeleteLinked1000 = time.time()
    linkedList1000.delete_AllElementsOfList(randomNums1000)
    endDeleteLinked1000 = time.time()
    durationDeleteLinked1000 = endDeleteLinked1000 - startDeleteLinked1000
    print('Here is the list, linkedList1000, after calling the function delete_AllElementsOfList():')
    linkedList1000.traverse_list()
    print('\n')


    # Printing the timing durations of the random 1000 number array list creation and deletion
    print("The duration of time it took to create a doubly linked list of 1000 random numbers (linkedList1000), using " +
          "the function insert_in_emptylist: ", durationLinkedList1000)
    print('\n')

    print("The duration of time it took to delete the entire entire the mynewLinkedList1000 doubly linked list " +
        "the function delete_AllElementsOfList: ", durationDeleteLinked1000)
    print('\n')



    # **************************************************************************************************************
    # Beginning to insert 10,000 random numbers into a doubly linked list, and then delete all and time all of the various
    # functionalities

    print('____________________________________________________________________________________________________')

    print('Starting my experiments with doubly linked lists of 10,000 random numbers by creating doublylinked list linkedList10000:')

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced

    # The variables for the variable main utilization, doubly linked list classes with associated functions
    linkedList10000 = DoublyLinkedList()

    # Showing that the doubly linked list linkedList1000 is empty
    print("Printing the empty doubly linked list linkedList10000:")
    linkedList10000.traverse_list()
    print('\n')


    # Inserting 10000 random numbers into linkedList1000
    print("Inserting 10,000 random numbers into doubly linked list, linkedList10000: ")
    startLinkedList10000 = time.time()
    randomNums10000 = np.array(random.sample(range(1, 10001), 10000))
    linkedList10000.insert_in_emptylist(randomNums10000)
    endLinkedList10000 = time.time()
    durationLinkedList10000 = endLinkedList10000 - startLinkedList10000
    linkedList10000.traverse_list()
    print('\n')

    # Reference for attempting deletion:
    # https://www.geeksforgeeks.org/delete-occurrences-given-key-doubly-linked-list/


    # deleting and timing the deletion of 10,000 elements from mynewlinkedList10000
    startDeleteLinked10000 = time.time()
    linkedList10000.delete_AllElementsOfList(randomNums10000)
    endDeleteLinked10000 = time.time()
    durationDeleteLinked10000 = endDeleteLinked10000 - startDeleteLinked10000
    print('Here is the list, linkedList10000, after calling the function delete_AllElementsOfList():')
    linkedList10000.traverse_list()
    print('\n')


    # Printing the timing durations of the random 10,000 number array list creation and deletion
    print("The duration of time it took to create a doubly linked list of 10,000 random numbers (linkedList10000), using " +
          "the function insert_in_emptylist: ", durationLinkedList10000)
    print('\n')

    print("The duration of time it took to delete the entire entire the mynewLinkedList10000 doubly linked list " +
        "the function delete_AllElementsOfList: ", durationDeleteLinked10000)
    print('\n')


    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

    ###

    # **************************************************************************************************************
    # Beginning to insert 100,000 random numbers into a doubly linked list, and then delete all and time all of the various
    # functionalities

    print('____________________________________________________________________________________________________')

    print(
        'Starting my experiments with doubly linked lists of 100,000 random numbers by creating doublylinked list linkedList10000:')

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced

    # The variables for the variable main utilization, doubly linked list classes with associated functions
    linkedList100000 = DoublyLinkedList()

    # Showing that the doubly linked list linkedList100,000 is empty
    print("Printing the empty doubly linked list linkedList100000:")
    linkedList100000.traverse_list()
    print('\n')

    # Inserting 100,000 random numbers into linkedList100000
    print("Inserting 100,000 random numbers into doubly linked list, linkedList100000: ")
    startLinkedList100000 = time.time()
    randomNums100000 = np.array(random.sample(range(1, 100001), 100000))
    linkedList100000.insert_in_emptylist(randomNums100000)
    endLinkedList100000 = time.time()
    durationLinkedList100000 = endLinkedList100000 - startLinkedList100000
    linkedList100000.traverse_list()
    print('\n')

    # Reference for attempting deletion:
    # https://www.geeksforgeeks.org/delete-occurrences-given-key-doubly-linked-list/

    # deleting and timing the deletion of 100,000 elements from mynewlinkedList10000
    startDeleteLinked100000 = time.time()
    linkedList100000.delete_AllElementsOfList(randomNums100000)
    endDeleteLinked100000 = time.time()
    durationDeleteLinked100000 = endDeleteLinked100000 - startDeleteLinked100000
    print('Here is the list, linkedList100000, after calling the function delete_AllElementsOfList():')
    linkedList100000.traverse_list()
    print('\n')

    # Printing the timing durations of the random 100,000 number array list creation and deletion
    print(
        "The duration of time it took to create a doubly linked list of 100,000 random numbers (linkedList100000), using " +
        "the function insert_in_emptylist: ", durationLinkedList100000)
    print('\n')

    print("The duration of time it took to delete the entire entire the mynewLinkedList100000 doubly linked list " +
          "the function delete_AllElementsOfList: ", durationDeleteLinked100000)
    print('\n')

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

    # **************************************************************************************************************
    print('********************************************************************************************************' +
          '********************************************************************************************************')

    # Creating a table to show the time durations for various processes implemented throughout this project
    # main reference: https://pandas.pydata.org/pandas-docs/version/0.15/10min.html
    # other references: https://matplotlib.org/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py
    # https://matplotlib.org/gallery/index.html
    # https://matplotlib.org/api/table_api.html?highlight=table#module-matplotlib.table
    print('\nCreating a table to show the time durations for various processes implemented throughout this project:\n')

    data = pd.DataFrame({ '|' : ('Creating empty doubly linked list |', 'Adding 50 numbers to empty doubly linked list |',
                        'Deleting 4 numbers from the list, one-by-one |', 'Insert 100 Random |', 'Insert 1000 Random |',
                        'Insert 10,000 Random |','Insert 100,000 Random |', 'Delete 100 Random |', 'Delete 1000 Random |', 'Delete 10,000 Random |', 'Delete 100,000 Random |'),
                        'Custom' : (printEmptyDuration, Adding50Duration, deleteFourDuration, 'NA','NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'),
                        'Array/Vector (Random #s)' : ('NA', 'NA', 'NA', duration100create, duration1000create, duration10000create, duration100000create, durationDeleteAnotherArray,
                        durationDeleteArray1000, durationDeleteArray10000, durationDeleteArray100000),
                        'Doubly-Linked(Random #s' : ('NA', 'NA', 'NA', durationLinkedList100, durationLinkedList1000, durationLinkedList10000, durationLinkedList100000,
                        durationDeleteLinked100, durationDeleteLinked1000, durationDeleteLinked10000, durationDeleteLinked100000)})

    # reference for how to print entire dataset and not just part of it, as shown below:
    # https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


    print(data)


Main()
