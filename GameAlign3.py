#Name:Subham Swastik Dora
#ID: 2014B2A70644P

#The align3 game is implemented using both the minimax and alpha beta pruning algorithm. 
#The board and coins are displayed using turtle Graphis whereas inputs for the move made by human is taken from console.
#Moves by human are represented by blue coins and that of machine by green coins.
#When alignment of three coins is achieved the coins are highlighted by red color.
#The inputs for the move made by human are row no. and column no.
#Rows are numbered from top to bottom. Top most row is numbered 0 whereas bottom most row is numbered 3.
#Columns are numbered from left to right. Left most column is numbered 0 whereas Right most column is numbered 3.
# Internally the board is represented by a 4x4 matrix in which 1 represents green coins and 2 represents blue coins.
#All the other required inputs are to be given from console on prompt.
#Several tricks are implemented to improve time and space and time complexity for minimax to run in reasonable time.
#Recursion is done using backtracking so that a single matrix representing the state of board is modified as moves are made.
#utility function defined achieves both terminal test and utility values in one go.
#Successor function is not explicitly implemented but achieved using a for loop.
#recursion limit is increases to accomodate the large no. of positions in the initial states of the board.
#please ensure that your system allows appropriate recursion limits.

import sys
import timeit
import turtle
turtle.speed(0)
sys.setrecursionlimit(100000)

#################################################GRAPHICS###################################################################################
size=40
class Board(object): #represents graphics of board and coins
    def __init__(self):#instatiation displays empty board
        turtle.title("Game")
        turtle.shape("arrow")
        turtle.color("black", "black")
        turtle.bgcolor("white") 
        turtle.hideturtle()
        for k in range(0,size*4,size):
            for j in range(0,size*4,size):
        
                turtle.sety(j)
                turtle.setx(k)
                for i in range(4):
                   
                   turtle.right(90)
                   turtle.forward(size)
            
        
        turtle.setx(0)
        turtle.sety(0)
        self.ox=0
        self.oy=0

    def winMove(self,r,c):#highlights the alignment of three coins
        turtle.color("red","black")
        r=2-r
        c=c-1
        turtle.up()
        turtle.goto(c*size+float(size/2),r*size+float(size/2))
        turtle.down()
        turtle.dot(size)
        turtle.up()
        turtle.goto(0,0)
        return
    def playerMove(self,r,c):#displays human move
        turtle.color("blue","black")
        r=2-r
        c=c-1
        turtle.up()
        turtle.goto(c*size+float(size/2),r*size+float(size/2))
        turtle.down()
        turtle.dot(size)
        turtle.up()
        turtle.goto(0,0)
        return
    def computerMove(self,r,c):#displays computer move
        turtle.color("green","black")
        r=2-r
        c=c-1
        turtle.up()
        turtle.goto(c*size+float(size/2),r*size+float(size/2))
        turtle.down()
        turtle.dot(size)
        turtle.up()
        turtle.goto(0,0)
        return
###########################################UTILITY-VALUE (ALSO USED AS TERMINAL TEST)#######################################################
def utility(matrix,r,c,val):#returns 1,-1,0 in case computer wins,human wins or tie respectively and returns 1000 if terminal is not reached
  flag=False                #value represents which player can move in this move(1 for computer and 2 for human)(only the player who made  
  temp=None                #the last move can win)
  if(val==1):
    temp=1
  if(val==2):
    temp=-1
  #cases where the last coin is in the middle of an alignment of three coins(if achieved)
  if(r==1 or r==2):
    if(matrix[r-1][c]==val and matrix[r][c]==val and matrix[r+1][c]==val ) :
      return temp
    if(c==1 or c==2):
      if(matrix[r-1][c-1]==val and matrix[r][c]==val and matrix[r+1][c+1]==val ) :
        return temp
      if(matrix[r-1][c+1]==val and matrix[r][c]==val and matrix[r+1][c-1]==val ) :
        return temp
  if(c==1 or c==2):
    if(matrix[r][c-1]==val and matrix[r][c]==val and matrix[r][c+1]==val ) :
      return temp
  #cases where the last coin is in the end of an alignment of three coins(if achieved)
  if(c==0 or c==1):
    if(matrix[r][c]==val and matrix[r][c+1]==val and matrix[r][c+2]==val):
      return temp 
  if(c==2 or c==3):
    if(matrix[r][c]==val and matrix[r][c-1]==val and matrix[r][c-2]==val):
      return temp
    
  if(r==0 or r==1):
    if(matrix[r][c]==val and matrix[r+1][c]==val and matrix[r+2][c]==val):
      return temp
  if(r==2 or r==3):
    if(matrix[r][c]==val and matrix[r-1][c]==val and matrix[r-2][c]==val):
      return temp
   
  if((r==0 and c==0)or(r==0 and c==1)or(r==1 and c==0)or(r==1 and c==1)):
    if(matrix[r][c]==val and matrix[r+1][c+1]==val and matrix[r+2][c+2]==val):
      return temp
  if((r==2 and c==2)or(r==2 and c==3)or(r==3 and c==2)or(r==3 and c==3)):
    if(matrix[r][c]==val and matrix[r-1][c-1]==val and matrix[r-2][c-2]==val):
      return temp
  if((r==2 and c==0)or(r==2 and c==1)or(r==3 and c==0)or(r==3 and c==1)):
    if(matrix[r][c]==val and matrix[r-1][c+1]==val and matrix[r-2][c+2]==val):
      return temp
  if((r==0 and c==2)or(r==0 and c==3)or(r==1 and c==2)or(r==1 and c==3)):
    if(matrix[r][c]==val and matrix[r+1][c-1]==val and matrix[r+2][c-2]==val):
      return temp
 #check for tie 
  count =0
  for i in range(4):
    for j in range(4):
      if(matrix[i][j]!=0):
        count=count +1
  if(count>=16):
    return 0
  
  return 1000
##########################################FINDS UTILITY-VALUE AND CHANGES THE COLOR OF WINNING COINS TO RED ################################
def graphicsUtility(matrix,r,c,val):
#returns 1,-1,0 in case computer wins,human wins or tie respectively and returns 1000 if terminal is not reached
 #value represents which player can move in this move(1 for computer and 2 for human)(only the player who made  
#the last move can win)
  flag=False
  temp=None
  if(val==1):
    temp=1
  if(val==2):
    temp=-1
   #cases where the last coin is in the middle of an alignment of three coins(if achieved) 
  if(r==1 or r==2):
    if(matrix[r-1][c]==val and matrix[r][c]==val and matrix[r+1][c]==val ) :
      board.winMove(r-1,c)
      board.winMove(r,c)
      board.winMove(r+1,c)
      return temp
    if(c==1 or c==2):
      if(matrix[r-1][c-1]==val and matrix[r][c]==val and matrix[r+1][c+1]==val ) :
        board.winMove(r-1,c-1)
        board.winMove(r,c)
        board.winMove(r+1,c+1)
        return temp
      if(matrix[r-1][c+1]==val and matrix[r][c]==val and matrix[r+1][c-1]==val ) :
        board.winMove(r-1,c+1)
        board.winMove(r,c)
        board.winMove(r+1,c-1)
        return temp
  if(c==1 or c==2):
    if(matrix[r][c-1]==val and matrix[r][c]==val and matrix[r][c+1]==val ) :
      board.winMove(r,c-1)
      board.winMove(r,c)
      board.winMove(r,c+1)
      return temp
#cases where the last coin is in the end of an alignment of three coins(if achieved)
  if(c==0 or c==1):
    if(matrix[r][c]==val and matrix[r][c+1]==val and matrix[r][c+2]==val):
      board.winMove(r,c)
      board.winMove(r,c+1)
      board.winMove(r,c+2)
      return temp 
  if(c==2 or c==3):
    if(matrix[r][c]==val and matrix[r][c-1]==val and matrix[r][c-2]==val):
      board.winMove(r,c)
      board.winMove(r,c-1)
      board.winMove(r,c-2)
      return temp
    
  if(r==0 or r==1):
    if(matrix[r][c]==val and matrix[r+1][c]==val and matrix[r+2][c]==val):
      board.winMove(r,c)
      board.winMove(r+1,c)
      board.winMove(r+2,c)
      return temp
  if(r==2 or r==3):
    if(matrix[r][c]==val and matrix[r-1][c]==val and matrix[r-2][c]==val):
      board.winMove(r,c)
      board.winMove(r-1,c)
      board.winMove(r-2,c)
      return temp
   
  if((r==0 and c==0)or(r==0 and c==1)or(r==1 and c==0)or(r==1 and c==1)):
    if(matrix[r][c]==val and matrix[r+1][c+1]==val and matrix[r+2][c+2]==val):
      board.winMove(r,c)
      board.winMove(r+1,c+1)
      board.winMove(r+2,c+2)
      return temp
  if((r==2 and c==2)or(r==2 and c==3)or(r==3 and c==2)or(r==3 and c==3)):
    if(matrix[r][c]==val and matrix[r-1][c-1]==val and matrix[r-2][c-2]==val):
      board.winMove(r,c)
      board.winMove(r-1,c-1)
      board.winMove(r-2,c-2)
      return temp
  if((r==2 and c==0)or(r==2 and c==1)or(r==3 and c==0)or(r==3 and c==1)):
    if(matrix[r][c]==val and matrix[r-1][c+1]==val and matrix[r-2][c+2]==val):
      board.winMove(r,c)
      board.winMove(r-1,c+1)
      board.winMove(r-2,c+2)
      return temp
  if((r==0 and c==2)or(r==0 and c==3)or(r==1 and c==2)or(r==1 and c==3)):
    if(matrix[r][c]==val and matrix[r+1][c-1]==val and matrix[r+2][c-2]==val):
      board.winMove(r,c)
      board.winMove(r+1,c-1)
      board.winMove(r+2,c-2)
      return temp
 #check for tie 
  count =0
  for i in range(4):
    for j in range(4):
      if(matrix[i][j]!=0):
        count=count +1
  if(count>=16):
    return 0
  
  return 1000
  

########################################################################### NODE ########################################################## 
class Node:
   count=None 	#stores no. of nodes generated.Print this after first move by computer to get the no. of nodes generate in one 
                 #minimax/alpha-beta pruning decision.Print after the game ends to get the total no. of nodes generated in the game 
   maxDepth=None 	# stores maximum recursion depth
   time=None	#stores time takes.Print this after first move by computer to get the time taken in one minimax/alpha beta pruning
                #decision.Print after the game ends to get the total time taken in the game 
   def __init__(self, matrix):
      self.matrix = matrix
      self.utilityValue = None
      self.move = None
      self.depth=None
      Node.count+=1
############################################# MINIMAX ######################################################################################
def minimaxDecision(node):
  print 'wait....'
  start = timeit.default_timer()  # time is calculated for each move by computer and added to total time
  v=maxValue(node,0,0)
  stop = timeit.default_timer() 
  totalTime = stop - start
  Node.time+=totalTime
  return node.move
    
def maxValue(node,r,c):       #r,c are the coordinates of the current move to be used by utility.
  u=utility(node.matrix,r,c,2) # uses r,c and 2 to check if human has won(since latest move is made by human)
  if(u!=1000):
    if(node.depth>=Node.maxDepth):  #checks if current recursion depth is more than the maximum
      Node.maxDepth=node.depth
    node.utilityValue=u             #utility value is stored in the node
    return u
  v=-10000
  temp1=None
  for i in range(4):            #to find next move (achieves the work of successor function)
    for j in range(4):           #to find the proper row in which the coin can be placed  
      if(node.matrix[j][i]==0): 
        node.matrix[j][i]=1
        newnode=Node(node.matrix)
        newnode.depth=node.depth+1  #recursion depth is increased
        temp=minValue(newnode,j,i)
        if(temp>v):
          v=temp
          temp1=i
        node.matrix[j][i]=0 #for backtracking purposes the move is undoed
        break
  node.move=temp1+1   #move made is stored in the node
  node.utilityValue=v #utility value is stored in the node
  return v


def minValue(node,r,c):        #r,c are the coordinates of the current move to be used by utility.
  u=utility(node.matrix,r,c,1)# uses r,c and 1 to check if computer has won(since latest move is made by computer)
  if(u!=1000):
    if(node.depth>=Node.maxDepth): #checks if current recursion depth is more than the maximum
      Node.maxDepth=node.depth
    node.utilityValue=u          #utility value is stored in the node
    return u
  v=10000
  temp1=None
  for i in range(4):              #to find next move (achieves the work of successor function)
    for j in range(4):            #to find the proper row in which the coin can be placed
      if(node.matrix[j][i]==0): 
        node.matrix[j][i]=2
        newnode=Node(node.matrix)
        newnode.depth=node.depth+1 #recursion depth is increased
        temp=maxValue(newnode,j,i)
        if(temp<v):
          v=temp
          temp1=i
        node.matrix[j][i]=0  #for backtracking purposes the move is undoed
        break
  node.move=temp1+1   #move made is stored in the node
  node.utilityValue=v  #utility value is stored in the node
  return v

  
     
############################################# ALPHA-BETA-SEARCH ############################################################################
def alphaBetaSearch(node):
  print 'wait....' 
  start = timeit.default_timer()     # time is calculated for each move by computer and added to total time
  v=maxValuePruned(node,0,0,-100000,100000)
  stop = timeit.default_timer()
  totalTime = stop - start
  Node.time+=totalTime
  return node.move
    
def maxValuePruned(node,r,c,alpha,beta):#r,c are the coordinates of the current move to be used by utility.
  u=utility(node.matrix,r,c,2)          # uses r,c and 1 to check if computer has won(since latest move is made by computer)
  if(u!=1000):
    if(node.depth>=Node.maxDepth):     #checks if current recursion depth is more than the maximum
      Node.maxDepth=node.depth
    node.utilityValue=u                  #utility value is stored in the node
    return u
  v=-10000
  temp1=None
  for i in range(4):                  #to find next move (achieves the work of successor function)
    for j in range(4):                #to find the proper row in which the coin can be placed
      if(node.matrix[j][i]==0): 
        node.matrix[j][i]=1            
        newnode=Node(node.matrix)       
        newnode.depth=node.depth+1  #recursion depth is increased
        temp=minValuePruned(newnode,j,i,alpha,beta)
        if(temp>v):
          v=temp
          temp1=i
        
        if(v>=beta):     #ignores unachievable moves(achieves pruning)
          node.move=temp1+1  #move made is stored in the node
  	  node.utilityValue=v #utility is stored in the node
	  node.matrix[j][i]=0 #for backtracking purposes the move is undoed
	  return v         
	alpha=max(alpha,v)   # max value is chosen as alpha     
        node.matrix[j][i]=0 #for backtracking purposes the move is undoed
        break
  node.move=temp1+1    #move made is stored in the node
  node.utilityValue=v  #utility value is stored in the node
  return v


def minValuePruned(node,r,c,alpha,beta):#r,c are the coordinates of the current move to be used by utility.
  u=utility(node.matrix,r,c,1)          # uses r,c and 1 to check if computer has won(since latest move is made by computer)
  if(u!=1000):
    if(node.depth>=Node.maxDepth):      #checks if current recursion depth is more than the maximum
      Node.maxDepth=node.depth
    node.utilityValue=u                 #utility value is stored in the node
    return u
  v=10000
  temp1=None
  for i in range(4):                       #to find next move (achieves the work of successor function)
    for j in range(4):                    #to find the proper row in which the coin can be placed
      if(node.matrix[j][i]==0): 
        node.matrix[j][i]=2
        newnode=Node(node.matrix)
        newnode.depth=node.depth+1         #recursion depth is increased
        temp=maxValuePruned(newnode,j,i,alpha,beta)
        if(temp<v):
          v=temp 
          temp1=i
        
	if(v<=alpha):        #ignores unachievable moves(achieves pruning)
          node.move=temp1+1  #move made is stored in the node
  	  node.utilityValue=v #utility is stored in the node
	  node.matrix[j][i]=0 #for backtracking purposes the move is undoed
	  return v
        beta=min(beta,v)    #min value is chosen as beta
        node.matrix[j][i]=0  #for backtracking purposes the move is undoed
        break
  node.move=temp1+1       #move made is stored in the node
  node.utilityValue=v     #utility value is stored in the node
  return v



################################################ DRIVER ####################################################################################
while(True):
  option=None
  while(True):
    breakFlag=True
    option=input('\nEnter 1 to Display the empty board\nEnter 2 to Play the game using Minimax algorithm\nEnter 3 to Play the game using Alpha Beta pruning\nEnter 4 to Show all results R1-R12\nEnter 5 to exit\n ')
    if(option!=1 and option!=2 and option!=3 and option!=4 and option!=5 ):
      breakFlag=False
    if(breakFlag):
      break
    print'Enter Valid input'
  if(option==5):
    break
  if(option==1):
    turtle.clearscreen()
    board=Board() #displays empty board
    continue
  if(option==4):
    
    print 'R1:total no. of nodes generated in the minimax : 6761217 (for first move by computer) \n  '
    print 'R2:memory allocated to one node: 104 bytes\n'        
    print 'R3:maximum growth of implicit stack in the minimax game: 16\n'
    print 'R4:total time taken by computer to play the game using minimax: 36.65 secs (first move made by computer) \n'
    print 'R5:nodes generated in one micro second: 199.86\n'
    print 'R6:total no. of nodes generated in the alpha-beta : 6817(for first move by computer)\n'
    print 'R7:saving using pruning(R1 - R6)/R1 = 0.998\n'
    print 'R8:total time taken by computer to play the game using alpha-beta pruning: 0.0827 secs(first move made by computer)\n'
    print 'R9: Memory used in minimax = 754069472 bytes and in alpha-beta pruning =  841152 bytes \n'
    print 'R10: Average time taken by computer to play the game using minimax =  22.02 secs and alpha-beta pruning = 0.08682 secs\n'
    print 'R11: Out of ten games using minimax computer(M) wins 6 times and using alpha-beta pruning computer(M) wins 5 times'
    print '(Note: Almost in all cases in both algo the player making the first move wins)\n'
    print 'R12: Out of 20 games(first move is made by computer(M) in half the games) using minimax computer(M) wins 10 times and using alpha-beta pruning computer(M) wins 10 times'
    print '(As mentioned above computer(M) wins if and only if first move is made by it )\n'
    print 'Alpha-beta is about 7700 times faster than minimax'
    continue
  #initializations
  Node.maxDepth=0
  Node.time=0
  Node.count=0
  matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #represents initial state i.e. state is represented as matrix
  turtle.clearscreen()
  board=Board()
  computerFirst=-1
  
  inp=None
  while(True):
    breakFlag=True
    inp=input('Enter 0 if you want to make the First move or enter 1 if you want computer to make the first move: ')
    if(inp!=0 and inp!=1):
      breakFlag=False
    if(breakFlag):
      break
    print'Enter Valid input:'
  if(inp==1):
    computerFirst=1
  if(inp==0):
    computerFirst=0
  while(computerFirst==0): #if human makes the first move
    while(True):
      breakFlag=True
      r=input('Enter row: ')
      c=input('Enter column: ')
      if(r<0 or r>3 or c<0 or c>3 or matrix[r][c]!=0 ):
        print 'Enter Valid input!'
        breakFlag=False
      elif(r!=0 and matrix[r-1][c]==0):
        print 'Enter Valid input!'
        breakFlag=False
      if(breakFlag): 
        break  
    matrix[r][c]=2          #human move
    board.playerMove(r,c)    #displays human move on the board
    u=graphicsUtility(matrix,r,c,2) #terminal test along with highlighting the alignment of 3 coins
    if(u!=1000):
      if(u==-1):
        print 'You(H) won'
        print 'total no. of nodes generated in the game: ',
        print Node.count
	print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
	print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
        
      else:
        print 'Its a tie'
        print 'total no. of nodes generated in the game: ',
        print Node.count
	print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
	print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
    #initial node for minimax/alpha-beta pruning
    init=Node(matrix) 
    init.depth=0
    t=None
    if(option==2):
      t=minimaxDecision(init) #next move of computer
    if(option==3):
      t=alphaBetaSearch(init) #next move of computer
    #print 'a'
    r1=None
    c1=None
    for i in range(4):#computer move
      if(matrix[i][t-1]==0):
        matrix[i][t-1]=1
        r1=i
        c1=t-1
        break
    board.computerMove(r1,c1) #displays computer move on the board
    u=graphicsUtility(matrix,r1,c1,1) #terminal test along with highlighting the alignment of 3 coins
    if(u!=1000):
      if(u==1):
        print 'computer(M) won'
        print 'total no. of nodes generated in the game: ',
        print Node.count
        print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
        print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
        
      else:
        print 'Its a tie'
        print 'total no. of nodes generated in the game: ',
        print Node.count
	print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
	print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
        
  while(computerFirst==1): #if computer makes the first move
    #initial node for minimax/alpha-beta pruning
    init=Node(matrix)
    init.depth=0
    t=None
    if(option==2):
      t=minimaxDecision(init) #next move of computer
    if(option==3):
      t=alphaBetaSearch(init) #next move of computer
    r1=None
    c1=None
    for i in range(4): #computer move
      if(matrix[i][t-1]==0):
        matrix[i][t-1]=1
        r1=i
        c1=t-1
        break
    board.computerMove(r1,c1)      #displays computer move on the board
    u=graphicsUtility(matrix,r1,c1,1) #terminal test along with highlighting the alignment of 3 coins
    if(u!=1000):
      if(u==1):
        print 'computer(M) won'
        print 'total no. of nodes generated in the game: ',
        print Node.count
        print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
        print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
        
      else:
        print 'Its a tie'
        print 'total no. of nodes generated in the game: ',
        print Node.count
	print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
	print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
      
    
    while(True):
      breakFlag=True
      r=input('Enter row: ')
      c=input('Enter column: ')
      if(r<0 or r>3 or c<0 or c>3 or matrix[r][c]!=0 ):
        print 'Enter Valid input!'
        breakFlag=False
      elif(r!=0 and matrix[r-1][c]==0):
        print 'Enter Valid input!'
        breakFlag=False
      if(breakFlag): 
        break
    matrix[r][c]=2 #human move
    board.playerMove(r,c) #displays human move on the board
  
    u=graphicsUtility(matrix,r,c,2) #terminal test along with highlighting the alignment of 3 coins
    if(u!=1000):
      if(u==-1):
        print 'You(H) won'
        print 'total no. of nodes generated in the game: ',
        print Node.count
	print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
	print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
        
      else:
        print 'Its a tie'
        print 'total no. of nodes generated in the game: ',
        print Node.count
	print 'memory allocated to one node:',sys.getsizeof(Node),' bytes'        
	print 'maximum growth of implicit stack in the game: ',
        print Node.maxDepth
        print 'total time taken by computer to play the game: ',
        print Node.time,'secs'
	print 'nodes generated in one micro second:', float(Node.count/(Node.time*1000))
        print 'Total Memory Used:',sys.getsizeof(Node)*Node.count,'bytes'
        break
       
  while(True):
    breakFlag=True
    inp1=input('\nEnter 1 if you want to play another game else enter 0 to exit: ')
    if(inp1!=0 and inp1!=1):
      breakFlag=False
    if(breakFlag):
      break
    print'Enter Valid input:'

  if(inp1==0):
    break
############################################################ END ###########################################################################
















