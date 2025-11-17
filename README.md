# Project_contact_Book
This Contact Book Application is a terminal-based contact management system that allows you to store, search, edit, and manage your contacts with persistent data storage.

—>Features implemented 

	Core Features: 

-Add Contact: — Create new contacts with validation 
-View All contacts: — Display all contacts sorted alphabetically 
-Search Contact: — Find contacts by name 
-Edit Contact: — Modify existing contact information 
-Delete Contact: — Remove contacts with confirmation 
-Save and Exit: — Automatically save data to JSON file

	Validation Features: 

-Email Validation: Ensures a proper email format (example: karl@gmail.com)
-Phone Validation: Validates phone numbers (8-15 digits, international formats accepted)
-Duplicate Check: Prevents adding contacts with the same name
-Empty fields check: Ensures required fields are not empty

	Other Features: 

Save/Load: Contacts are  saved to and loaded from ‘contacts.json’
JSON Format for contacts
Handling FileNotFoundError when loading

	Optional Enhancements  implemented in the code: 

-Sorting contacts alphabetically when viewing
-Validations (phone numbers and emails)
-OOP classes: Contact and Contact_Book

	Running the code:

Prerequisites: Python 3 installed on the system/computer
Some packages need to be imported: pandas, numpy, json, os, re

	Instructions:

1. Save the code as « contact_book.py »
2.Open terminal/command prompt. Navigate to the directory containing ‘contact_book.py’ and run the python ‘contact_book.py’
3. The application: The menu will appear with options 1-6; follow the prompt for each operation. At the end, choose 6 to save and exit. 

	Menu Options

1. Add Contact: Enter full name, phone number and Email address. Automatic validation of phone and email format is implemented. 
2. View all contacts: Displays all contacts in alphabetical order 
3. Search contact: search by name (partial matches supported), case-insensitive search
4. Edit contacts: Modify name, phone or email; Leave fields blank to keep current values; Validation applied to new entries
5. Delete contact : remove by name; A confirmation prompt is printed before deletion. The function handles multiple matches correctly
6. Save and Exit: Saves all changes to ‘contacts.json’ and exits the application.

	File structure

- ‘contact_book.py’: Main application file 
- ‘contacts.json’: Data file (created automatically)

	Technical Details

-Data storage: JSON format for easy readability 
-Validation: Regular expressions for email and phone validation 
-Search: Case-insensitive partial matching 
-Sorting: Alphabetical order by name
- Error Handling: Comprehensive exception handling 

	Usage Tips

-Phone numbers accept international format (+33, spaces, hyphens, parantheses)
-Email must follow standard format (Example: karl@domain.com)
-Contacts are automatically sorted by name
-Data is preserved between sessions and confirmation is required for deletion 

If the program doesn’t starts, make sure python 3.x is installed. If the contacts don’t save, check file permissions in the directory. For validation issues, ensure phone numbers contain only digits and email follow standard format. 










