# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.





















if __name__ == "__main__":
    class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

    class LinkedList: 
            # Function to initialize head 
            def __init__(self): 
                    self.head = None
            # Function to insert a new node at the beginning 
#            def push(self, new_data): 
#                    new_node = Node(new_data) 
#                    new_node.next = self.head 
#                    self.head = new_node 
                    
            def push(self, new_data): 
                    new_data = input("Type in a number: ")
                    new_node = Node(new_data) 
                    new_node.next = self.head 
                    self.head = new_node
            # Add contents of two linked lists and return the head 
            # node of resultant list 
            def addTwoLists(self, first, second): 
                    prev = None
                    temp = None
                    carry = 0
                    # While both list exists 
                    while(first is not None or second is not None): 
                            # Calculate the value of next digit in 
                            # resultant list 
                            # The next digit is sum of following things 
                            # (i) Carry 
                            # (ii) Next digit of first list (if ther is a 
                            # next digit) 
                            # (iii) Next digit of second list ( if there 
                            # is a next digit) 
                            fdata = 0 if first is None else first.data 
                            sdata = 0 if second is None else second.data 
                            Sum = carry + fdata + sdata 

                            # update carry for next calculation 
                            carry = 1 if Sum >= 10 else 0

                            # update sum if it is greater than 10 
                            Sum = Sum if Sum < 10 else Sum % 10

                            # Create a new node with sum as data 
                            temp = Node(Sum) 

                            # if this is the first node then set it as head 
                            # of resultant list 
                            if self.head is None: 
                                    self.head = temp 
                            else : 
                                    prev.next = temp 

                            # Set prev for next insertion 
                            prev = temp 

                            # Move first and second pointers to next nodes 
                            if first is not None: 
                                    first = first.next
                            if second is not None: 
                                    second = second.next

                    if carry > 0: 
                            temp.next = Node(carry) 

            # Utility function to print the linked LinkedList 
            def printList(self): 
                    temp = self.head 
                    while(temp): 
                            print temp.data, 
                            temp = temp.next
            def reverse(self): 
                prev = None
                current = self.head 
                while(current is not None): 
                    next = current.next
                    current.next = prev 
                    prev = current 
                    current = next
                self.head = prev 



list1 = LinkedList()
list2 = LinkedList()

#list1.push(1)
#list1.push(2)
#list1.push(3)
#list1.push(4)
#list1.push(5)
#list1.push(6)
#list1.push(6)
#list1.push(7)
#list1.push(8)
#list1.push(9)
#list1.push(0)
#list1.push(1)
#list1.push(2)
#list1.push(3)
#list1.push(4)
#list1.push(5)
#list1.push(6)
#list1.push(7)
#list1.push(8)
#list1.push(9)
#
#
#list2.push(8)
#list2.push(7)
#list2.push(6)
#list2.push(5)
#list2.push(4)
#list2.push(3)
#list2.push(2)
#list2.push(1)
#list2.push(0)
#list2.push(9)
#list2.push(8)
#list2.push(7)
#list2.push(6)
#list2.push(5)
#list2.push(4)
#list2.push(3)
#list2.push(2)
#list2.push(1)
#list2.push(0)



sum = LinkedList()

sum.addTwoLists(list1.head, list2.head)
sum.reverse()
#sum.printList()
print("Welcome to my Python Infinity addition Calculator!")

while True:
       print("Here are your instructions!")  
       print("1. Add an element")
#       print("2. Print the list")
#       print("3. Size of the list")
       menu = int(input("Choose an action:"))

       if menu == 1:
               list1.insert()
       elif menu == 2:
               MyList.print()
       elif menu == 3:
               MyList.size()