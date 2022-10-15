# write a program to fill in a letter template given below with name and date
# letter = ''' Dear <|NAME|>,
#              you are selected!
#              <|DATE|>'''

letter = ''' Dear <|NAME|>,
             you are selected!
             Date:<|DATE|>'''
            
name = input("enter your name :\n")
date = input("enter date :\n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)
            
