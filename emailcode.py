import random
import string


def email_gen():

    chars_after_at = int(input("How many character mail do you want after @gmail.com between 4 and 100: "))
    
    if(chars_after_at <4 or chars_after_at >100):
        print("Please use characters between 4 and 100 ")
        exit()
    else:
        while True:
         letters_list =[string.digits,string.ascii_lowercase , string.ascii_uppercase]

         letters_list_to_str = "".join(letters_list)


         email_format = "@gmail.com"

         email_generated = "".join(random.choices(letters_list_to_str ,k=chars_after_at)) + email_format
   
         print(email_generated)
while True:

#call the email generator function
           email_gen()

