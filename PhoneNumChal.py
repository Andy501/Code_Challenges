
import re

def valid_phone_number(phone_number):

    try: 
        capture = re.findall("[^1,2,3,4,5,6,7,8,9,0,(,), ,-]", phone_number)
        # All remaining chars that we dont want, if greater than 1 not a phone number
        print(len(capture))
        if phone_number[0] == "(" and  phone_number[4] == ")" and phone_number[5] == " " and phone_number[9] == "-" and len(capture) == 0:
            phone_number = ''.join(re.findall(r'\d', phone_number))
            # If not 10 digits, not a phone number
            if len(phone_number) != 10 : 
                qual = False    
            else:
                qual = True
        else: 
            print(phone_number + " there")
            qual = False
    # If origianl string not long enough for index set up, rejected not a phone number
    except IndexError:
        qual = False
    return (qual)

print(valid_phone_number("(888) 889-4sdf038"))