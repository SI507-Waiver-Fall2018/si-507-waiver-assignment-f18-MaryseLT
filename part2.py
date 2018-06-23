
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\ Maryse Elizabeth Lundering-Timpano : MaryseLT [6379 5232] \\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\ SI 507 Fall 2018 Waiver (2/4) \\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ==============================================================
# ========== Instructions - PART 2: Work with SQLite3 ==========
# ==============================================================

    # FILENAME: part2.py
    # NOTE: Use sqlite3
    # USAGE SHOULD BE:
        #  python3 part2.py customers
        #  python3 part2.py employees
        #  python3 part2.py orders cust=<customer id>
        #  python3 part2.py orders emp=<employee last name>


# /////////////////////////////////////////////
# ////////// STEP 1 - Import Library //////////
# /////////////////////////////////////////////

    # these should be the only imports you need

import sys
import sqlite3

# /////////////////////////////////////////////////
# ////////// STEP 2 - Connect to SQLite3 //////////
# /////////////////////////////////////////////////

conn = sqlite3.connect('Northwind_small.sqlite') # My DB Filename
cur = conn.cursor()

# /////////////////////////////////////////////////
# ////////// STEP 3 - Process User Input //////////
# /////////////////////////////////////////////////

def begin_input():

    if len(sys.argv) == 0:
        print("\nPlease try again and enter a command.\n")
        exit() # Auto Exit Program to Avoid Crashing

    elif len(sys.argv) > 1 and sys.argv[1] == 'customers':
            customers()

    elif len(sys.argv) > 1 and sys.argv[1] == 'employees':
            employees()

    elif len(sys.argv) > 2 and 'cust=' in sys.argv[2]:
        c_order = sys.argv[2][5:] # User Input Param
        cust_orders(c_order)

    elif len(sys.argv) > 1 and 'emp=' in sys.argv[2]:
        emp_order = sys.argv[2][4:] # User Input Param
        #print(emp_order)
        emp_name(emp_order)

    else:
        print("\nPlease try again and enter a valid command.\n")
        exit() # Auto Exit Program to Avoid Crashing


# /////////////////////////////////////////////////////////
# ////////// OPTION 1 - sys.argv[1] == customers //////////
# /////////////////////////////////////////////////////////

def customers(): # No Param Needed

    stmt = '''
        SELECT Id, CompanyName
        FROM Customer AS c
    '''

    cur.execute(stmt)
    x = cur.fetchall()

    print("ID    | Customer Name")
    print("-"*50)
    for y in x:
        print("{} | {}".format(y[0],y[1]))
        print("-"*50)

    conn.commit()

# /////////////////////////////////////////////////////////
# ////////// OPTION 2 - sys.argv[1] == employees //////////
# /////////////////////////////////////////////////////////

def employees(): # No Param Needed

    stmt = '''
        SELECT Id,FirstName,LastName
        FROM Employee AS e
    '''

    cur.execute(stmt)
    x = cur.fetchall()

    print("ID |   Employee Name")
    print("-"*25)
    for y in x:
        print("{}  |   {} {}".format(y[0],y[1],y[2]))
        print("-"*25)

    conn.commit()

# ///////////////////////////////////////////////////////
# ////////// OPTION 3 - sys.argv[2] == 'cust=' //////////
# ///////////////////////////////////////////////////////

def cust_orders(c_order): # Param == User Input

    stmt = '''
        SELECT o.OrderDate
        FROM [Order] AS o
        JOIN Customer AS c
        ON o.CustomerId = c.Id
        WHERE c.Id = ? -- This is the User Input [params]
    '''

    params = (c_order, ) # User Input
    cur.execute(stmt, params)
    x = cur.fetchall()

    print("Order Dates")
    print("-"*15)
    for y in x:
        print("{}".format(y[0]))
        print("-"*15)

    conn.commit()

# //////////////////////////////////////////////////////
# ////////// OPTION 4 - sys.argv[2] == 'emp=' //////////
# //////////////////////////////////////////////////////

def emp_name(emp_order): # Param == User Input

    stmt = '''
        SELECT o.OrderDate
		FROM OrderDetail AS od
        JOIN [Order] AS o
        ON o.Id = od.OrderId
        JOIN Employee AS e
        ON o.EmployeeId = e.Id
        WHERE e.LastName = ? -- This is the User Input [params]
    '''

    params = (emp_order, ) # User Input
    cur.execute(stmt, params)
    x = cur.fetchall()

    print("Order Dates")
    print("-"*15)
    for y in x:
        print("{}".format(y[0]))
        print("-"*15)

    conn.commit()


# ---------------------------------------------------------
# ----- AUTOSTART: My Instructions for File Execution -----
# ---------------------------------------------------------

if __name__ == "__main__":
    begin_input() # First Defined Function
    #conn.close() # Close DB Connection when File Finishes Executing
