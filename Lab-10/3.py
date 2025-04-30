# Accept user input
number=int(input("Enter the Number of contact:"))
file=open("contact.vcf", "a")

for i in range(0,number):
    name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")


    vcard = f"""BEGIN:VCARD
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

    file.write(vcard)

print(f"\nvCard saved as. You can import it on your phone.")
