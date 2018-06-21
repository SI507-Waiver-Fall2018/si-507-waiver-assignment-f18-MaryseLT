# these should be the only imports you need
import sys
import sqlite3


# FILENAME: part2.py

# NOTE: Use sqlite3.

# ////////////////////////////////////////////
# /////////////// Start Coding ///////////////
# ////////////////////////////////////////////

# write your code here
# usage should be
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>


# /////////////////////////////////////////////
# ////////// Connect to the Database //////////
# /////////////////////////////////////////////

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

# ///////////////////////////////////////////////
# ////////// Actions Passed in by User //////////
# ///////////////////////////////////////////////

def begin_input():

    if len(sys.argv) == 0:
        print("\nPlease try again and enter a command.\n")
        exit()

    elif len(sys.argv) > 1 and sys.argv[1] == 'customers':
            customers()

    elif len(sys.argv) > 1 and sys.argv[1] == 'employees':
            employees()

    elif len(sys.argv) > 2 and 'cust=' in sys.argv[2]:
        c_order = sys.argv[2][5:]
        cust_orders(c_order)

    elif len(sys.argv) > 1 and 'emp=' in sys.argv[2]:
        emp_order = sys.argv[2][4:]
        print(emp_order)
        emp_name(emp_order)

    else:
        print("\nPlease try again and enter a valid command.\n")
        exit()


# //////////////////////////////////////////////
# ////////// sys.argv[1] == customers //////////
# //////////////////////////////////////////////

def customers():

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

# //////////////////////////////////////////////
# ////////// sys.argv[1] == employees //////////
# //////////////////////////////////////////////

def employees():

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

# ////////////////////////////////////////////
# ////////// sys.argv[2] == 'cust=' //////////
# ////////////////////////////////////////////

def cust_orders(c_order):

    stmt = '''
        SELECT o.OrderDate
        FROM [Order] AS o
        JOIN Customer AS c
        ON o.CustomerId = c.Id
        WHERE c.Id = ? -- This is the user input parameter
    '''

    params = (c_order, )
    cur.execute(stmt, params)

    x = cur.fetchall()

    print("Order Dates")
    print("-"*15)
    for y in x:
        print("{}".format(y[0]))
        print("-"*15)

    conn.commit()

# ////////////////////////////////////////////
# ////////// sys.argv[2] == 'emp=' //////////
# ////////////////////////////////////////////

def emp_name(emp_order):

    stmt = '''
        SELECT o.OrderDate
		FROM OrderDetail AS od
        JOIN [Order] AS o
        ON o.Id = od.OrderId
        JOIN Employee AS e
        ON o.EmployeeId = e.Id
        WHERE e.LastName = ? -- This is where the paramater goes (employee last name)
    '''

    params = (emp_order, )
    cur.execute(stmt, params)

    x = cur.fetchall()

    print("Order Dates")
    print("-"*15)
    for y in x:
        print("{}".format(y[0]))
        print("-"*15)

    conn.commit()


if __name__ == "__main__":
    begin_input()
    conn.close() # Close the Database Connection
