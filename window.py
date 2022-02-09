from asyncio.windows_events import NULL
from tkinter import *
from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeWindow :
    barcodeNumber = 'fwfw'
    ent = NULL
    def __init__(self):
        pass

    def start():
        root = Tk()
        root.title("Barcode")
        root.geometry("640x480")
        BarcodeWindow.ent =Entry(root,width=30,insertwidth=12)
        BarcodeWindow.ent.pack()
        
        
        bn = Button(root, text="출력",command=BarcodeWindow.bncmd)
        bn.pack()

        
        root.mainloop()
        return


    def bncmd():
        BarcodeWindow.barcodeNumber = BarcodeWindow.ent.get()
        print(BarcodeWindow.barcodeNumber)
        
        num= BarcodeWindow.barcodeNumber
        my_code = Code128(num, writer=ImageWriter())
        my_code.save("barcode")
        return

    


BarcodeWindow.start() 