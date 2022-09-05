# CARGO CUSTOMER INFORMATION APPLICATION
import pathlib
def showOutput():
    with open("KerKarCargo.txt","r",encoding="utf-8")as file:
      for i in file:
        print(i,end="")

def deleteTheFile():  
    file=pathlib.Path("KerKarCargo.txt")
    file.unlink()
    
def customer_information():
    customerID=input('Customer ID:')
    name=input('Customer Name:')
    surname=input('Customer Surname:')
    city=input('City:')
    district=input('District:')
    address=input('Address:')
    price=input('Product Price:')
    phoneNumber=input('Phone Number:')
    IBAN=input('IBAN:')
    with open("KerKarCargo.txt","a",encoding="utf-8") as file:
        file.write(customerID+') '+name+', '+surname+', '+city+', '+district+'\n'+price+'\n'+address+', '+phoneNumber+', '+IBAN+'\n')

while True:
    process=input('1-Enter the Customer Information\n2-Delete the file\n3-Show data in the output\n4-Exit\n')
    if process=='1':
        customer_information()
    elif process=='2':
        deleteTheFile()
    elif process=='3':
        showOutput()
    else:
        break




