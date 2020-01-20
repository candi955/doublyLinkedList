# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/


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
            print("This is the item2.")
            self.start_node = self.start_node
            self.start_node.pref = None
            return
        # for finding the middle numbers
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                print("This could be the item.")
                break
            n = n.nref

        # for finding the end number
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                print("This is the item3.")
            else:
                print("Element not found")

DoublyLinkedList()

# Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

class Main():

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/
    # creating a variable to call the DoublyLinkedList() class, from the StackAbuse example being referenced
    new_linked_list = DoublyLinkedList()

    # Showing that the list is empty
    print("Printing the empty list:")
    new_linked_list.traverse_list()
    print('\n')


    # From the StackAbuse example being referenced, inserting the number 50 into the list (technically at the end of the list
    print("Adding the number 50 to the empty list:")
    new_linked_list.insert_in_emptylist(50)
    new_linked_list.traverse_list()
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

    print("Finding the number 10 to fulfill the assignment 'finding an element by value:")
    new_linked_list.find_element_by_value(300)
    print('\n')
    new_linked_list.traverse_list()
    print('\n')

    # Reference: https://stackabuse.com/doubly-linked-list-with-python-examples/

Main()



