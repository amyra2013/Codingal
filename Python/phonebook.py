import sys
def initial_phonebook():
    columns=5
    rows=int(input("Enter the number of contacts you wish to have"))
    phone_book = []

    for i in range(rows):
        print("Enter the details for contact #",i+1)
        print("NOTE: The asterisk(*) indicates mandatory fields.")
        temp = []
        for j in range(columns):
            if j==0:
                temp.append(input("Enter name*:"))
                if temp[j]=="" or temp[j]==" ":
                    sys.exit("This is a mandatory field. Process exiting")
            if j==1:
                temp.append(int(input("Enter phone number*:")))
            if j==2:
                temp.append(input("Enter the email address:"))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]= None
            if j==3:
                temp.append(input("Enter date of birth (dd/mm/yy):"))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]= None
            if j==4:
                temp.append(input("Enter category of contact(Work/Family/Friends/Others):"))
                if temp[j]=="" or temp[j]==" ":
                    temp[j]= None
        phone_book.append(temp)

    print(phone_book)
    return(phone_book)

def menu():
    print("*************************************************************************************");print("\t\t\tSMARTPHONE DIRECTORY, flush=False");
    print("*************************************************************************************");print("\tYou can now perform the following operations on this phonebook\n");
    print("1. Add a new contact");
    print("2. Remove an existing contact");
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice=int(input("Please enter your choice:" ))

    return choice

def add_contact(pb):
   dip=[]
   for i in range(len(pb[0])) :
    if i==0:
        dip.append(str(input("Enter name:"))) 
    if i==1:
        dip.append(int(input("Enter number:")))
    if i==2:
        dip.append(str(input("Enter e-mail address:")))
    if i==3:
        dip.append(str(input("Enter date of birth(dd/mm/yy):")))
    if i==4:
        dip.append(str.input("Enter category(Family/Firnds/Work/Others:)"))

    pb.append(dip)

    return pb 
def remove_existing(pb):
       query=str(input("Please enter the name of the contact you wish to remove:"))
       temp=0
       for i in range          









    