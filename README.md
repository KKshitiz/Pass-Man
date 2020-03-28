* # Pass-Man
    ## Description
    An easy to use Password manager with in-built multi-purpose password generator
    <br>

    # Submodules
    * User authentication system
    * Password manager
    * Password generator

    # Features:
    ## User login:
    * User can enter their username and master-password to open the vault
    * Supports multiple users
    * If the account doesn't exist, user can create a new account
    * All the passwords are stored in hashed format using SHA256 encryption technique
    * The entered username and master-password will be checked against the details stored in the sqlite database
    * Forget password option to create new master-password

    ## Password manager
    * A table consiting of stored passwords
    * Add multiple entries consisting of title, login-id, password, website and any other extra detail
    * User can update or delete existing entries
    * Passwords can be easily copied to clipboard with a click
    * Important entries can be starred
    * Bulk deletion option
    * Opening URL directly from the entry

    ## Password generator
      User can generate strong random passwords with following options:
    * Set the length
    * Enable/disable Uppercase characters
    * Enable/disable digits
    * Enable/disable special characters
        
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
