# rockme
A script that takes a user string and checks it against known password wordlists.


# Notes
Wordlist text files should be saved in the same directory where rockme.py is being ran, or use absolute file path. If there are issues with reading the files due to encoding issues, modify `with open` function to include a third argument `encoding="utf-8`.

rockme.py is for educational and security awareness purposes only.

# Updates
- Fixed main menu validation code, which was causing issues with checking user string against wordlist for matches, thus incorrectly always returning no matches found [08/10/2023]
  
- Added the wordlist 'darkweb2017-top10000.txt'

- Added red text color when displaying invalid input error message


# Future Developments
- Add additional popular wordlists
  
- Allow user to move back into outer menu

- Validate user submenu choices

