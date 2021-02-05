from operation import Operation



class Menu(Operation):#אתחול תפריט 
    def __init__(self):
        Operation.__init__(self)#ירושה Operation
        Operation.__new__(self)
        
        while True:#בדיקת קלט yes or no 
          self.to_open = input("\n\nDo you want to overwrite the content or add characters to file ?\nyes = add characters\nno = overwrite\n\n").lower()
          if self.to_open == 'yes':
                self.run_yes()
          elif self.to_open == 'no':
                self.run_no()
          else:
                print(" Please enter only yes or no\n")
    
    def display_menu(self):#הצגת תפריט אפשרויות
        print("""
        Menu:"what would you like to do ? 
        1. write with *****.
        2. write with ####.
        3. write with your own character.
        4. like before.
        5. show me file.
        6. delete file.
        7. if you want to exit.\n
        """)

    def run_yes(self):#הפעלת תפריט כאשר בחורים yes
        while True:
          self.display_menu()# תפריט  אפשרויות
          choice = input("Enter an option:\t")
          action = self.choices.get(choice)#בחירת פעולה מתבקשת ירושה של פונקציות class Menu(Operation)
          if action:
              action()
          else:
              print("{0} is not a valid choice".format(choice))
    
    def run_no(self):#הפעלת תפריט כאשר בחורים no
          self.delete_file()  #במידה ובחרנו NO 
                              #תתבצע דריסת הקובץ     
          while True:
            self.display_menu()# תפריט  אפשרויות
            choice = input("Enter an option:\n")
            action = self.choices.get(choice)#בחירת פעולה מתבקשת ירושה של פונקציות class Menu(Operation)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
  



    


