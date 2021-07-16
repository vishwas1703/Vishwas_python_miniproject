# ***Design*** 

## **Main function**
***
In this project a existed excel file is opened and used for read and write operation.The number of rows,coloumns,number of sheets and their names are used to traverse along the cells.
"openpyxl" package is imported to handle reading and writing of excel file.when the program runs it opens the file mentioned and shows the list of ps numbers in 1st coloumn and ask to select any one from available number,after that it shows sheet names available and ask to select a prefered sheet.Then program copies the content from the specified list and paste into a new excel file.


### **Functions:**
---
Functions defined and used in the project are. 
1. Finding 
- To find the row number of selected ps 
- Function iterates through out the first coloumn of all rows.
- When row cell value equals the ps number program comes out of for loop by returning the row number.
2.  checking
- Function is used to check the sheet name entered by user is exist or not.
- When function is invoked,for loop iterates through the names of sheet to ensure user entered sheet name is exist in excel file. 

### **Working of program**
---
- Program prints the ps number and asks to enter any one number.
- Program prints the sheet names from which data needs to extracted and asks to enter sheet name.
-Program copies the data from selected sheet name to new excel file.
-At the end of program a new excel file is created containg specified data.
### **Use Case Diagram**
Figure below shows case diagram of project.
![case](case diagram.PNG)
