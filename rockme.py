###### rockme.py is for educational and security awareness purposes only #####

### Display main menu
while True:
    print("=======================================")
    print("  Please select a wordlist from below  ")
    print("=======================================")
    print("[1] - rockyou-75.txt")
    print("[ ] -")
    print("[ ] -")
    print("[ ] -")
    print("[ ] -")
    print("[Q] - Quit")
    
    # Prompts user to enter a choice and converts it to a string
    main_choice = str(input("Enter: "))

    # Displays submenu related to RockYou
    if main_choice == "1":
        print("=======================================")
        print("            rockyou-75.txt             ")
        print("=======================================")
        print("[1] - Check password")
        print("[2] - Display content")
        print("[3] - What is RockYou.txt?")
        print("[ ] ")
        print("[Q] - Quit")

        # Prompts user to enter a subchoice and converts it to a string
        sub_choice = str(input("Enter: "))

        # Begin logic for subchoice 1
        if sub_choice == "1":
            # Assigns the file to var. Ensure wordlist file is saved in same directory as script, or use absolute path and filename
            import_file = "rockyou-75.txt"
            
            # Opens file in "r" mode. Reads and assign the file's content to var and turns it into a list, where each element is separated by a content's line break
            with open(import_file, "r") as file:
                password_list = file.read().splitlines()
            
            # Prompts the user to enter a password they would like to check against wordlist content
            user_pw = str(input("What is the password you would like to check: "))

            # For loop iterates each element within the wordlist
            for password in password_list:

                # Logic compares user's password against current element being checked
                # var password_index keeps track of the index location of the matching password
                # Notifies the user a match has been found and it's index location
                # Otherwise, indicate no match and quit the script
                if user_pw == password:
                    password_index = password_list.index(password)
        
                    print(f'A match has been identified to password "{user_pw}" at index position {password_index}')
                    quit()
                else:
                    print("No match was identified")
                    quit()
        
        # Begin logic for subchoice 2
        if sub_choice == "2":
            # Assigns the file to var. Ensure wordlist file is saved in same directory as script, or use absolute path and filename
            import_file = "rockyou-75.txt"
            
            # Opens file in "r" mode. Reads and assign the file's content to var and turns it into a list, where each element is separated by a content's line break
            with open(import_file, "r") as file:
                password_list = file.read().splitlines()

            # For logic iterates through each element in wordlist, and displays it to user. Quit script when finished
            for password in password_list:
                print(password)
            quit()

        # Begin logic for subchoice 3
        if sub_choice == "3":
            print("")
            print("In 2009, a social app named RockYou experienced a massive cyberattack which led to over 32 million user passwords becoming exposed due to being stored in plaintext")
            print("The leaked passwords have since been compiled into a wordlist commonly known as 'RockYou.txt', and used by security professionals and malicious actors")
            print("as part of a password dictionary attack and penetration testing, as the wordlist is derived from real-life passwords.")
            print("")
            quit()

    # if main choice is Q, then quit script
    if main_choice.lower() == "q":
        quit()

    ### User input validation
    if main_choice.lower() != "1" or "q":
        print("Invalid choice, try again")




################################################ FOOTNOTES ################################################

#############################
# Version:    1.00          #
# Date:       08/07/2023    #
# Coder:      CH @chan2git  #
#############################

# rockyou-75.txt is from https://github.com/danielmiessler