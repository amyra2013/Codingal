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



            



    