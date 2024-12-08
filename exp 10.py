import re

def is_valid_email (email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re .match(email_pattern, email):
        return True
    else:
        return False
def main():
     test_emails=[
         "user@example.com",
         "user.name@domain.co",
         "user_name123@sub.domain.com",
         "invalid-email@.c0m",
         "missing-at-symbol.com",
         "user@domain.c",
         "user@doamin_with_underscore.com",
         ]
     print("email validation results:")
     for email in test_emails:
        result = is_valid_email(email)
        print(f"{email}: {'valid' if result else 'invalid'}")
main()   


    

        




    

          

    
            
        
            