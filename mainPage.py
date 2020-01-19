
# Node of a doubly linked list
class Node:
    def __init__(self, next=None, prev=None, data=None):     # setting the constructor __init__(self)
        self.next = next # reference to next node in DLL      # next is set to None
        self.prev = prev # reference to previous node in DLL  # prev is set to None
        self.data = data                                       # data is set to None

        # Adding a node at the front of the list
        def push(self, new_data):                               # the push function is for adding new data, and
            # 1 & 2: Allocate the Node & Put in the data          # setting the head to null
            new_node = Node(data=new_data)

            # 3. Make next of new node as head and previous as NULL
            new_node.next = self.head
            new_node.prev = None

            # 4. change prev of head node to new node
            if self.head is not None:                                 # with push since the head is set to null,
                self.head.prev = new_node                             # the previous is set to the new data

                        # 5. move the head to point to the new node
                self.head = new_node



            # Given a node as prev_node, insert
            # a new node after the given node

            def insertAfter(self, prev_node, new_data):

                # 1. check if the given prev_node is NULL
                if prev_node is None:
                    print("This node doesn't exist in DLL")
                    return

                # 2. allocate node  & 3. put in the data
                new_node = Node(data=new_data)

                # 4. Make next of new node as next of prev_node
                new_node.next = prev_node.next

                # 5. Make the next of prev_node as new_node
                prev_node.next = new_node

                # 6. Make prev_node as previous of new_node
                new_node.prev = prev_node

                # 7. Change previous of new_node's next node */
                if new_node.next is not None:
                    new_node.next.prev = new_node

                    #  This code is contributed by jatinreaper

Node()

def Main():

    nodeClass = Node()

    mylist = ([3, 6, 9])

    print(mylist)

    Node.



Main()
