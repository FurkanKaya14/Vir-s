import pyautogui, time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
pyautogui.click()
pyautogui.doubleClick(45, 26, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(57, 167, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(66, 284, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(48, 407, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(59, 511, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(52, 651, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(49, 785, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.doubleClick(45, 900, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1789, 112) 
for i in range(1): #Yeni klasör oluşturma
 pyautogui.rightClick(1789, 112, duration=2, tween=pyautogui.easeInOutQuad)
 time.sleep(0.5)
 pyautogui.click(1505, 310, duration=2, tween=pyautogui.easeInOutQuad)
 time.sleep(0.5)
 pyautogui.doubleClick(1259, 310, duration=2, tween=pyautogui.easeInOutQuad)
for i in range(1): #Yeni metin belgesi oluşturma
 pyautogui.rightClick(1789, 112, duration=2, tween=pyautogui.easeInOutQuad)
 time.sleep(0.5)
 pyautogui.click(1505, 310, duration=2, tween=pyautogui.easeInOutQuad)
 time.sleep(0.5)
 pyautogui.doubleClick(1286, 481, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1912, 2) #Masaüstündeki her şeyi silme
pyautogui.mouseDown(button='left')
pyautogui.moveTo(18, 990, 1)
time.sleep(1)
pyautogui.rightClick(18, 990, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.click(203, 990, duration=1, tween=pyautogui.easeInOutQuad)
time.sleep(10)
pencere = Tk() #Silme işleminden sonra TC kimlik numarası isteyen pencere açma
pencere.title("10 saniyen var!")
pencere.geometry("400x200")
pencere.configure(bg='black')
path = r"C:\orumcek.png" #Pencereye ikon ekleme
load = Image.open(path)
ikon = ImageTk.PhotoImage(load)
pencere.iconphoto(False, ikon)
pencere.after(10000, lambda: pencere.destroy()) #10 saniye sonra pencereyi otomatik kapatma
def Buton():
 messagebox.askyesno("Teşekkür ederiz...", "Hizmetimizden memnun kaldınız mı?") #Butona tıklandığında açılan pencere
Buton1 = Button(pencere, text ="Yazdım", command = Buton, fg='black', bg='red')
Buton1.place(x=320, y=80, height=30)
yazi1 = Label(pencere, text="TC kimlik yaz!", fg='black', bg='red')
yazi1.place(x=20, y=80, width=140, height=30)
girdi1 = Entry(pencere, bd =5, fg='black', bg='red')
girdi1.insert(0, "31841438394") #Pencere açıldığında kişinin TC'sini entry'e son üç hanesi eksik olarak getirme
girdi1.delete(8,11)
girdi1.place(x=170, y=80,width=140, height=30)
pencere.mainloop()
pencere1 = Tk() #TC girilen pencere kapatıldığında açılan pencere
pencere1.title("Yanlış cevap")
pencere1.configure(bg='black')
path = r"C:\orumcek.png"
load = Image.open(path)
ikon = ImageTk.PhotoImage(load)
pencere1.iconphoto(False, ikon)
uyari = StringVar() #İkinci pencerede çıkan uyarı yazısı
yazi2 = Label(pencere1, textvariable=uyari, relief=RAISED, fg='black', bg='red')
uyari.set("Yarışmaya katıldığınız için teşekkür ederiz...")
yazi2.place(x=10, y=80, width=380, height=40)
pencere1.geometry("400x200")
pencere1.mainloop()
pencere2 = Tk() #İkici pencere kapatıldıktan sonra açılan üçüncü pencere
pencere2.title('Son Aşama')
pencere2.geometry('1800x1050')
path = r"C:\orumcek.png"
load = Image.open(path)
ikon = ImageTk.PhotoImage(load)
pencere2.iconphoto(False, ikon)
pencere2.config(bg='black')
def calismayan_tus(): #Pencere kapatma tuşunu işlevsiz kılma
 pass
def mesaj():
 for i in range(10):
  messagebox.showinfo('Geçersiz İşlem', 'Tekrar Deneyiniz') #Penceredeki 'Kapat' butonuna basıldığında uyarı penceresi açma
pencere2.protocol("WM_DELETE_WINDOW", calismayan_tus)
Button(pencere2, text='Kapat', command=mesaj, bg='red').pack(pady=50)
pencere2.mainloop()
