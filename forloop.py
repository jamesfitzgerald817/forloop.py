# This program displays a rectangular pattern
# of asterisks.
rows = int(input('How many rows? ')) # User will input a number for the amount of rows
cols = int(input('How many columns? '))# User will input a number for the amount columns
 
for r in range(rows): #System will display an * for number of rows and columns based on the users input.
      for c in range(cols):
         print('*', end='')
      print()

 

##### problem 2#######
# This step will display the # as 6 steps and print after the print statement displaying the number of columns and rows entered by the user.
num_steps = 6

for r in range(num_steps): # The for loop will end after running 6 times displaying a # each time it runs 
   for c in range(r):
      print(' ', end='')
   print('#')

##### problem 3 #######
# This step will define and print the user, language, and platform. A user name, language name, and platform name will be displayed and mirrored one using new information for each option. An additional 
def echo( user , lang , sys ) :
    print( 'User:' , user , 'Language:' , lang , 'Platform:' , sys )

echo( 'Mike' , 'Python' , 'Windows' )

echo( lang = 'Python' , sys = 'Mac OS' , user = 'Anne' )


def mirror(  user = 'Carole' , lang = 'Python' ) :
    print( '\nUser:' , user , 'Language:' , lang )

mirror()
mirror( lang = 'Java' )
mirror( user = 'Tony' )
mirror( 'Susan', 'C++' )

