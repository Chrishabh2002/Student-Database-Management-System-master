import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def studentData():
    """Initialize the student database and create the student table if it doesn't exist."""
    try:
        with sqlite3.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    id INTEGER PRIMARY KEY,
                    StdID TEXT,
                    Firstname TEXT,
                    Surname TEXT,
                    DoB TEXT,
                    Age TEXT,
                    Gender TEXT,
                    Address TEXT,
                    Mobile TEXT
                )
            """)
            con.commit()
            logging.info("Student table created or already exists.")
    except sqlite3.Error as e:
        logging.error(f"Error creating student table: {e}")

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    """Add a new student record to the database."""
    try:
        with sqlite3.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO student (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
            con.commit()
            logging.info(f"Added student record: {StdID}, {Firstname} {Surname}")
    except sqlite3.Error as e:
        logging.error(f"Error adding student record: {e}")

def viewData():
    """Retrieve and return all student records from the database."""
    try:
        with sqlite3.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            logging.info("Retrieved all student records.")
            return rows
    except sqlite3.Error as e:
        logging.error(f"Error retrieving student records: {e}")
        return []

def deleteRec(id):
    """Delete a student record by ID."""
    try:
        with sqlite3.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM student WHERE id=?", (id,))
            con.commit()
            logging.info(f"Deleted student record with ID: {id}")
    except sqlite3.Error as e:
        logging.error(f"Error deleting student record: {e}")

def searchData(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    """Search for student records based on provided criteria."""
    try:
        with sqlite3.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("""
                SELECT * FROM student 
                WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?
            """, (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
            rows = cur.fetchall()
            logging.info(f"Found {len(rows)} matching student records.")
            return rows
    except sqlite3.Error as e:
        logging.error(f"Error searching student records: {e}")
        return []

def dataUpdate(id, StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    """Update a student record by ID with provided data."""
    try:
        with sqlite3.connect("student.db") as con:
            cur = con.cursor()
            cur.execute("""
                UPDATE student 
                SET StdID=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?
                WHERE id=?
            """, (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
            con.commit()
            logging.info(f"Updated student record with ID: {id}")
    except sqlite3.Error as e:
        logging.error(f"Error updating student record: {e}")

# Initialize the database and table
studentData()