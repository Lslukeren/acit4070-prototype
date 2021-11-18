import random
import locationFinder
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Norwegian Rails")

homeText = Label(root, text="Home")
homeText.grid(row=1, column=0, columnspan=3)
numberOfSeats = 0
payCount = 0

def getDeparture():
    global errorText
    global errorText2
    global payCount
    global payConfirm
    global payConfirm2
    global priceShow
    global doubleCheck
    a = str(departure.get())
    b = str(destination.get())
    c = locationFinder.findDistance(a, b)

    #Removes error labeles before each call to ensure the removal of bugs
    try:
        priceShow.grid_forget()
    except NameError:
        pass
    try:
        errorText.grid_forget()
        errorText2.grid_forget()
    except NameError:
        pass

    if c:
        try:
            errorText.grid_forget()
        except NameError:
            pass

    if numberOfSeats > 0:
        try:
            errorText2.grid_forget()
        except NameError:
            pass

    if c and numberOfSeats > 0:
        if payCount == 0:
            doubleCheck = numberOfSeats
            price = c*2 + doubleCheck*5
            payCount = 1
            try:
                payConfirm.grid_forget()
            except NameError:
                pass
            try:
                priceShow.grid_forget()
            except NameError:
                pass
            try:
                payConfirm2.grid_forget()
            except NameError:
                pass
            print("Price is: " + str(price) + "kr")
            priceShow= Label(root, text="Price is: " + str(price) + "kr")
            priceShow.grid(row=7, columnspan=3)
            payConfirm = Label(root, text="Click 'Pay' again to confirm purchase")
            payConfirm.grid(row=8, columnspan=3)
        elif doubleCheck != numberOfSeats:
            payCount = 0
            doubleCheck = numberOfSeats
            price = c * 2 + doubleCheck * 5
            payCount = 1
            try:
                payConfirm.grid_forget()
            except NameError:
                pass
            try:
                priceShow.grid_forget()
            except NameError:
                pass
            try:
                payConfirm2.grid_forget()
            except NameError:
                pass
            print("Price is: " + str(price) + "kr")
            priceShow = Label(root, text="Price is: " + str(price) + "kr")
            priceShow.grid(row=7, columnspan=3)
            payConfirm = Label(root, text="Click 'Pay' again to confirm purchase")
            payConfirm.grid(row=8, columnspan=3)

        elif payCount == 1:
            payCount = 0
            payConfirm.grid_forget()
            priceShow.grid_forget()
            payConfirm2 = Label(root, text="Payment confirmed!")
            payConfirm2.grid(row=8, columnspan=3)
            print("Payment confirmed!")
            ticketPrint = open("ticket.txt", "w")
            ticketPrint.write(a + " -> " + b)
            ticketPrint.close()


    elif numberOfSeats == 0:
        errorText2 = Label(root, text="Please select seats")
        errorText2.grid(row=7, columnspan=3)
        payCount = 0
        try:
            payConfirm.grid_forget()
        except NameError:
            pass
        try:
            payConfirm2.grid_forget()
        except NameError:
            pass
        if c:
            try:
                errorText.grid_forget()
            except NameError:
                pass
        if not c:
            errorText = Label(root, text="Please enter a valid departure and destination")
            errorText.grid(row=6, columnspan=3)

    elif not c:
        errorText = Label(root, text="Please enter a valid departure and destination")
        errorText.grid(row=6, columnspan=3)
        payCount = 0
        try:
            payConfirm.grid_forget()
        except NameError:
            pass
        try:
            payConfirm2.grid_forget()
        except NameError:
            pass
        if numberOfSeats > 0:
            try:
                errorText2.grid_forget()
            except NameError:
                pass

        if numberOfSeats == 0:
            errorText2 = Label(root, text="Please select seats")
            errorText2.grid(row=7, columnspan=3)


def purchaseTicket():
    global departure
    global destination
    global textHelp
    global frame
    global button_goBack
    global depText
    global destText
    global pay

    depText = Label(root, text="From:")
    depText.grid(row=0, column=0)
    departure = Entry(root, width=30)
    departure.grid(row=0, column=1)
    departure.insert(0, "")

    destText = Label(root, text="To:")
    destText.grid(row=1, column=0)
    destination = Entry(root, width=30)
    destination.grid(row=1, column=1)
    #destination.insert(0, "")

    #ticket = getDeparture(departure, destination)
    #print(ticket)
    homeText.grid_forget()
    ptButton.grid_forget()
    stButton.grid_forget()
    textHelp = Label(root,
                     text="Seats marked with A or the color green are available\n Seats marked with N or the color red are not available\n Seats marked with Y or the color yellow are your seats\n")
    textHelp.grid(row=4, columnspan=3)
    frame = LabelFrame(root, text="Click to choose", padx=6, pady=6)
    frame.grid(row=5, columnspan=3, pady=10)

    # Left side seats

    b1 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b1))
    b2 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b2))
    b3 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b3))
    b4 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b4))
    b5 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b5))
    b6 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b6))
    b7 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b7))
    b8 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b8))

    # Right side seats
    b11 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b11))
    b12 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b12))
    b13 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b13))
    b14 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b14))
    b15 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b15))
    b16 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b16))
    b17 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b17))
    b18 = Button(frame, text=generateText(), bg=generateColor(), state=generateState(),command=lambda: takeSeat(b18))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=1, column=0)
    b4.grid(row=1, column=1)
    b5.grid(row=2, column=0)
    b6.grid(row=2, column=1)
    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)

    # Column spacer
    spacer = Label(frame, text="  ")
    spacer.grid(column=2)

    b11.grid(row=0, column=3)
    b12.grid(row=0, column=4)
    b13.grid(row=1, column=3)
    b14.grid(row=1, column=4)
    b15.grid(row=2, column=3)
    b16.grid(row=2, column=4)
    b17.grid(row=3, column=3)
    b18.grid(row=3, column=4)

    #Bottom most buttons
    #print(getDeparture("Jessheim", "Oslo"))

    pay = Button(root, text="Pay", command=getDeparture)
    #pay = Button(root, text="Pay", command=lambda: getDeparture(str(departure), str(destination)))
    pay.grid(row=10, column=2, sticky=SE)

    button_goBack = Button(root, text="Go back", command=goBack)
    button_goBack.grid(row=10, column=0, sticky=SW)

def generateText():
    global a
    a = random.randrange(2)
    if a == 0:
        return " A "
    else:
        return " N "

def generateColor():
    if a == 0:
        return "green"
    else:
        return "red"

def generateState():
    if a == 0:
        return NORMAL
    else:
        return DISABLED


def showTicket():
    global frame2
    global ticket
    global textHelp2
    global button_goBack2
    global ticketDisplay2

    homeText.grid_forget()
    ptButton.grid_forget()
    stButton.grid_forget()
    textHelp2 = Label(root, text="Show this QR code to the conductor")
    textHelp2.grid(row=4, columnspan=3)
    qrCode = ImageTk.PhotoImage(Image.open("qr.png"))
    frame2 = LabelFrame(root, padx=6, pady=6)
    frame2.grid(row=6, columnspan=3, pady=10)
    ticket = Label(frame2, image=qrCode)
    ticket.grid(row=0, column=0)
    try:
        ticketDisplay = open("ticket.txt", "r")
        ticketDisplay2 = Label(root, text=ticketDisplay.read())
        ticketDisplay2.grid(row=5, columnspan=3)
    except FileNotFoundError:
        pass

    button_goBack2 = Button(root, text="Go back", command=goBack)
    button_goBack2.grid(row=10, column=0, sticky=SW)


def goBack():
    global ptButton
    global stButton
    global homeText
    global numberOfSeats
    global payCount

    payCount = 0

    homeText = Label(root, text="Home")
    homeText.grid(row=1, column=0, columnspan=3)
    ptButton = Button(root, text="Purchase ticket", command=purchaseTicket, padx=40, pady=100, state=NORMAL)
    ptButton.grid(row=2, column=0)

    stButton = Button(root, text="Show ticket", command=showTicket, padx=40, pady=100)
    stButton.grid(row=2, column=2)

    numberOfSeats = 0
    #All these try/excepts are here to ensure that labels and buttons get removed when going back
    try:
        priceShow.grid_forget()
    except NameError:
        pass
    try:
        ticketDisplay2.grid_forget()
    except NameError:
        pass
    try:
        payConfirm.grid_forget()
    except NameError:
        pass
    try:
        payConfirm2.grid_forget()
    except NameError:
        pass
    try:
        pay.grid_forget()
    except NameError:
        pass
    try:
        depText.grid_forget()
    except NameError:
        pass
    try:
        destText.grid_forget()
    except NameError:
        pass
    try:
        departure.grid_forget()
    except NameError:
        pass
    try:
        destination.grid_forget()
    except NameError:
        pass
    try:
        button_goBack.grid_forget()
    except NameError:
        pass
    try:
        frame.grid_forget()
    except NameError:
        pass
    try:
        textHelp.grid_forget()
    except NameError:
        pass
    try:
        textHelp2.grid_forget()
    except NameError:
        pass
    try:
        frame2.grid_forget()
    except NameError:
        pass
    try:
        ticket.grid_forget()
    except NameError:
        pass
    try:
        errorText.grid_forget()
    except NameError:
        pass
    try:
        errorText2.grid_forget()
    except NameError:
        pass
    try:
        button_goBack2.grid_forget()
    except NameError:
        pass



def takeSeat(button):
    global numberOfSeats
    if button["bg"] == "green":
        button["bg"] = "yellow"
        button["text"] = " Y "
        numberOfSeats+=1
    else:
        button["bg"] = "green"
        button["text"] = " A "
        numberOfSeats-=1

ptButton = Button(root, text="Purchase ticket", command=purchaseTicket, padx=40, pady=100, state=NORMAL)
ptButton.grid(row=2, column=0)

stButton = Button(root, text="Show ticket", command=showTicket, padx=40, pady=100)
stButton.grid(row=2, column=2)
print("Hei")

root.mainloop()
