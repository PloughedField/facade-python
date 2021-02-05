import sys
from re import match
from os import path



class Operation(): 
    def __init__(self):
      self.character=None  #אתחול משתנה בחירת תו 
      self.choices = { #אתחול מילון אפשרויות משתמש
                "1": self.write_with_1,
                "2": self.write_with_2,
                "3": self.write_with_3,
                "4": self.like_before,
                "5": self.show_me_file,
                "6": self.delete_file,
                "7": self.quit
                }
      if not path.exists(self.file_name):#בדיקה שהקובץ קיים במערכת אם לא יוצר חדש
        self.write_new()
        print("\n\nThe file was created successfully\n") 

    def __new__(self):#singleton
      if not hasattr(self, 'instance'):#singleton
          self.file_name = input("\nplease insert the filename.txt:\n\n").lower()
          self.valid_file_name(self)#אימות שם משתמש נכון
          self.instance = super().__new__(self)#singleton
          self.instance.filename = self.file_name#singleton
      return self.instance 
      
   
    def valid_file_name(self):#אימות שם משתמש נכון
      while True:
        # if self.file_name.endswith('txt'):
        if match( r'^[\w,\s-]+\.[txt]{3}$', self.file_name):#בדיקה רגקס לשם הקובץרק TXT
            break
        else:
             self.file_name = input("Please enter a valid sample >>> filename.txt\n").lower()
    
    def valid_character(self):#אימות שהמשתמש הזין תו אחד בלבד כל פעם 
        if self.character == None:#  אם הלקוח לחץ באפשרות 4 על ההתחלה
          print("\nThe wrong action is not yet selected, selecting a character\n")
          self.character=input("Please select the character.\n")

        while len(self.character)!=1:#בדיקה שאכן נבחר תו 1 בלבד
           self.character = input("Please enter only one character.\n")

        
    def write_add(self, line:str):#פונקצית כתיבה והוספה לקובץ
      with open(self.filename, 'a+') as f:
        f.write(line+"\n")
    
    def write_new(self, line=None):#אתחול קובץ ודריסה
      with open(self.filename, 'w') as y:
        pass
    
    
    def write_with_1(self):#כתיבה מסוג כוכבית 
        wirte_file = input("Please write to the requested file.\n")
        self.write_add("*"*90)
        self.write_add(wirte_file)
        self.write_add("*"*90)
        self.character="*"

    def write_with_2(self):#כתיבה מסוג סולמית 
        wirte_file = input("Please write to the requested file.\n")
        self.write_add("#"*90)
        self.write_add(wirte_file)
        self.write_add("#"*90)
        self.character="#"
    
    def write_with_3(self):#כתיבה עם תו נבחר
        self.character = input("Please select the character.\n")
        self.valid_character()#אימות שהמשתמש הזין תו אחד בלבד כל פעם 
        wirte_file = input("Please write to the requested file.\n")
        self.write_add(self.character*90)
        self.write_add(wirte_file)
        self.write_add(self.character*90)
       

    
    def like_before(self):#המשך כתיבה עם התו האחרון שהיה בשימוש
          self.valid_character()# בדיקה האם עדיין לא נבחר תו אז נבחר תו 
          #בנוסף אם המשתמש הקיש 4 על תחילת העבודה במערכת
          wirte_file = input("Please write to the requested file.\n")
          self.write_add(self.character*90)
          self.write_add(wirte_file)
          self.write_add(self.character*90)
    
    def show_me_file(self):#הדפסת התוכן של הקובץ 
      with open( self.filename, 'r') as f:
        show_file =f.read()
        if len(show_file)==0:#אם הקובץ ריק 
          print("\nThe file you selected is empty")
        else:
          print(show_file)#הדפסה תוכן הקובץ

    def delete_file(self):#דריסת הקובץ והמידע הקיים
      with open( self.filename, 'r') as f:
        show_file =f.read()
        if len(show_file)==0:#אם הקובץ ריק 
          print("\nThe file you selected is empty")
        else:
          self.write_new()
          print("\nThe content of the file was successfully deleted")
        
    
    def quit(self):#סיום 
        print("\nThank you we would love to see you again.")
        sys.exit(0)