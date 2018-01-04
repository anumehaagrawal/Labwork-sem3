class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        self.head=ListNode()
        self.head1=ListNode()
        """Create a new list with a Sentinel Node"""

    def insert(self,x,p):
        temp=ListNode()
        p.next=temp
        temp.value=x
        self.head1=p
        # self.printlst()




    def delete(self,p):
        p.next=p.next.next
        """Delete the node following node p in the linked list."""
        

    def printlst(self):
        it=self.head
        while it is not None:
            print(it.value, end=' ')
            it=it.next
           

        """ Print all the elements of a list in a row."""
        

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        it=self.head
        for m in range(0,i):
            it=it.next
        temp=ListNode()
        temp.next=it.next
        temp.value=x
        it.next=temp

        
       
    def search(self,x):
        it=self.head
        r=None
        while r is None:
        	if it.next.data == x :
        		r=it.next
        	else:
        		it=it.next
        return(r)			



        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
       

    def len(self):
        it=self.head
        ans=0
        while it.next is not None:
            ans+=1
            it=it.next
        return ans    
        
        """Return the length (the number of elements) in the Linked List."""
        
    def isEmpty(self):
        if self.head.next is None:
            return True
        else:
            return False	
        """Return True if the Linked List has no elements, False otherwise."""
        


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt
    

class hashtable:

    def insertht(self,key,value,T,M):
        if T[key] is None:
            T[key]=ListNode()
            T[key].value=value
            M.head=T[key]
            M.head1=T[key]
            

        else:
            M.insert(value,M.head1)
    def keys(self,T):
        l=[]
        for i in range(30):
            
            if T[i] is not None:
                it=T[i]

                while it is not None:
                    
                    print(it.value, end=' ')
                    l.append(it.value)
                    it=it.next
        
        return l
        

    def searchel(self,T,find):
        l1=[]
        l1=self.keys(T)
        if find in l1:
            print("Found")
        else:
            print("not found")

                    


def main():
    L = LinkedList()
    A=hashtable()
    keylist=[]

    vallist=[]
     
    T = [None for i in range(30)]
    n=int(input("enter num"))
    for i in range(n):
        a=input()
        summ=0
        for k in a:
            summ=summ+ord(k)
        v=summ
        keyv=summ%30
        vallist.append(a)
        if not keyv in keylist:
            keylist.append(keyv)
            m='a'
            M=m+str(keyv)
            M=LinkedList()
        A.insertht(keyv,a,T,M)
    A.keys(T)
    A.searchel(T,'anu')
   

if __name__ == '__main__':
    main()