
#Nodklass för att skapa nod med ett värde och två pekare (right och left)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


#klass med 3 st funktioner från uppgiftsbeskrivningen
class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        if self.root == None:
            self.root = Node(newvalue)      
        else:
            putta(newvalue, self.root)

    def __contains__(self,value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")
            
#Funkion som lägger till nya värden i trädet
def putta(newvalue, root):
    node = root
     
    if newvalue < node.value and root.left == None:
        root.left = Node(newvalue)
        #print("a") test för att se vilken rad som exekveras
        return root
      
    elif newvalue < node.value and root.left != None:
        putta(newvalue, node.left)
        #print("b") test för att se vilken rad som exekveras

    elif newvalue > node.value and root.right == None:
        root.right = Node(newvalue)
        #print("c") test för att se vilken rad som exekveras
        return root
    
    elif newvalue > node.value and root.right != None:
        putta(newvalue, node.right)
        #print("d") test för att se vilken rad som exekveras

    #om ord som redan finns försöker läggas in informeras användaren. Inga dubletter i trädet.
    else:
        print("dubletter ej tillåtna")

#Funktion som kollar om ett visst värde (ord) finns i trädet
def finns(root, value):

    if root == None:
        return False
    
    elif value == root.value:
        return True

    elif value < root.value:
        return finns(root.left,value)
    
    elif value > root.value:
        return finns(root.right,value)
    
    

#funktion som skriver ut trädet innehåll i inorder enl. kod från boken
def skriv(node):
    if node!=None:
        skriv(node.left)
        print(node.value)
        skriv(node.right)



















