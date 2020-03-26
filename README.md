* # Pass-Man
    ## Description
    An easy to use Password manager with in-built multi-purpose password generator
    <br>

    # Submodules
    * User authentication system
    * Password manager
    * Password generator

    What it does?
    * Authenticates user login
    * Shows a panel of user passwords
    * User can add title, login, passwords, their corresponding websites and any other detail
    * User can edit entries
    * User can delete entries
    * Stores passwords in a database file in hashed format using SHA256 encryption technique
    * Passwords can be easily copied to clipboard
    * User can generate strong random passwords with the option to include digits, capitals and/or special characters
    * Ability to recover forgotten master password
    
        
    ## Technologies used:
        * python3
        * tkinter library
        * sqlite3 database

    ## How to install requirements:
        pip install tkinter
        pip install sqlite3
        pip install passlib
        
    ## Create your own executable
        pip install pyinstaller
        cd script_folder
        pyinstaller script.py                       //for executable with dependencies
        pyinstaller --onefile script.py             //standalone executable file with terminal
        pyinstaller --onefile -w script.py          //standalone executable without terminal
        
    **The executable will be located in the script_folder/dist directory**
      <br>
    *To create a setup use NSIS open source software*
    <br>
    *To compress the exe significantly use strip.exe then UPX*
