# got source code from moodle provided by lecturer
class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def remove(self,n): #n = node  #removed function which was added by me
            if n.prev != None: 
                  n.prev.next = n.next # previouse node of n will skip n and go to the next node
            else:
                  self.head = n.next # reached the head
            if n.next != None: 
                  n.next.prev = n.prev # next node of n will skip n and go to the previouse one
            else:
                  self.tail = n.prev # read the tail which is the end
      '''
      the way you can remove and element from a linked list is by
      changing the link from the previouse item to point to the next item,
      so the one after that item.

      if the the previouse node of the node you want to delete is not nothing
      then
      so the node you want to delete will be skipped and will be deleted by python using
      automatic garbage collector
      else
      the head will be skipped
      '''
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
         
if __name__ == '__main__':
    l=List()
    A = Node(4)
    B = Node(6)
    C = Node(8)
    l.insert(None,(A))
    l.insert(l.head,(B))
    l.insert(l.head,(C))
    l.display()
    l.remove(A)
    l.display()
    
