import smtplib
from tkinter import *
#import win32compat 
#clicks = 0
#Excel=win32api.client.Dispatch("Excel.Application")
def click_button():
    #wb=Excel.Workbooks.Open(u'C:\\Users\\Rez\\Downloads\\Задание\\Задание\\Фрагмент Бд.xlsx')
    #sheet=wb.ActiveSheet
    val=sheet.Cells(1,1).Value
    print(val)
   # s=smtplib.SMTP('smtp.mail.ru',25)
    #s.starttls()
    #s.login("kabarov.anton@mail.ru","######")
    #message="Hello hi"
    #s.sendmail("kabarov.anton@mail.ru","kabarov.anton@mail .ru",message)
    #s.quit()


root = Tk()  
root.title("GUI на Python") 
root.geometry("300x250")
btn = Button(text="Click Me", background="#555", foreground="#ccc",
                 padx="16", pady="8", font="13 ", command=click_button)   
btn.place(x=70,y=10)
#btn.pack()
root.mainloop()


#gb = glob.glob(r,'.\Lib\.py')
#gb.append("/out:StdLib")
#pyc.Main(["/target:dll"]+gb)
#gb=["/main:WindowsApplication2.py","WindowsApplication2.py","/target:exe","/out:Fred_Download_Tool"]
#import clr
#import sys
#sys.path.append(r'.\Lib.zip')
#clr.AddReference("System.Windows.Forms")

#from System.Windows.Forms import Application, Form

#class HabrForm(Form):

#     def __init__(self):
#         self.Text = 'Habr!'
#         self.Name = 'Habr!'

# form = HabrForm()
# Application.Run(form)