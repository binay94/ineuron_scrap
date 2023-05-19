import sqlite3
from pymongo import MongoClient
from utility import ineuron_scraping as ins
from user_cred import username, password, file_path
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def sql_op():
    try:
        categories = ins.get_categories()
            
        # Connect to the SQLite database
        conn = sqlite3.connect(f'{file_path}courses.db')
        c = conn.cursor()

        # Create tables for categories, subcategories, and courses
        c.execute('''CREATE TABLE IF NOT EXISTS categories (
                            category_name TEXT
                        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS subcategories (
                            subcategory_name TEXT,
                            category_id INTEGER
                        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS courses (
                            course_name TEXT,
                            subcategory_id INTEGER,
                            course_details TEXT
                        )''')

        for category_name, subcategories in categories.items():
            # Insert category into the 'categories' table
            c.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name,))
            category_id = c.lastrowid

            for subcategory_name, courses in subcategories.items():
                # Insert subcategory into the 'subcategories' table
                c.execute("INSERT INTO subcategories (subcategory_name, category_id) VALUES (?, ?)",
                              (subcategory_name, category_id))
                subcategory_id = c.lastrowid

                for course_name in courses:
                    # Insert course into the 'courses' table
                    course_details = ins.get_course_details(course_name)
                    c.execute("INSERT INTO courses (course_name, subcategory_id, course_details) VALUES (?, ?, ?)",
                                  (course_name, subcategory_id, str(course_details)))

            # Commit the changes and close the connection
        conn.commit()
        conn.close()            
        print("Courses added to the database.")
        logging.info("Courses added to the database.")
            
    except Exception as e:
        logging.error(f"Error in SQL operation: {str(e)}")



def mongodb_op():
    try:
        categories = ins.get_categories()       

        # Connect to MongoDB
        client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ojgbawe.mongodb.net/?retryWrites=true&w=majority")
        db = client['ineuron_courses']
        categories_collection = db['categories']
        subcategories_collection = db['subcategories']
        courses_collection = db['courses']

        for category_name, subcategories in categories.items():
            # Insert category into the 'categories' collection
            category = {'category_name': category_name}
            category_id = categories_collection.insert_one(category).inserted_id

            for subcategory_name, courses in subcategories.items():
                # Insert subcategory into the 'subcategories' collection
                subcategory = {'subcategory_name': subcategory_name, 'category_id': category_id}
                subcategory_id = subcategories_collection.insert_one(subcategory).inserted_id

                for course_name in courses:
                    # Insert course into the 'courses' collection
                    course_details = ins.get_course_details(course_name)
                    course = {'course_name': course_name, 'subcategory_id': subcategory_id, 'course_details': course_details}
                    courses_collection.insert_one(course)

        print("Courses added to MongoDB.")
        logging.info("Courses added to MongoDB.")
    except Exception as e:
        logging.error(f"Error in MongoDB operation: {str(e)}")
    

sql_op()
mongodb_op()


