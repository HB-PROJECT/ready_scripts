from pyqrcode import create
import tkinter as tk
import qrcode

root = tk.Tk()
user_input = tk.StringVar(root)

def verify():
    xmb_file : str = create(user_input.get()).xbm(scale=10)
    print(create("w").code)
    
    qrimage = tk.BitmapImage(data = xmb_file)
    label = tk.Label(root, image = qrimage)
    label.pack()
    qr = qrcode.make(user_input.get())
    qr.save('{}.png'.format("123"))
    
    # label.destroy()
    

entry = tk.Entry(root, textvariable=user_input)
entry.pack()
check = tk.Button(root, text='make QR', command = verify)
check.pack()

root.mainloop()