import requests
from bs4 import BeautifulSoup as bs
import json
from url import courses_url
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR)


#Function to retrive all the list of courses available in iNeuron Website
def get_courses():
        try:
            response = requests.get(courses_url)
            soup = bs(response.content, 'html.parser')
            courses_data = soup.find("script", {"id": "__NEXT_DATA__"})
            courses_json = json.loads(courses_data.text)
            courses_meta = courses_json['props']['pageProps']['initialState']['init']['courses']
            courses = []
            for cname,desc in courses_meta.items():
                course = {}
                course['title']=cname
                course['description'] = desc['description']
                course['slug'] = cname.replace(" ","-")
                course['categoryId'] = desc['categoryId']
                courses.append(course)
            instructors_dict = {}
            for cname, desc in courses_meta.items():
                instructor_details = desc.get('instructorsDetails', [])
                for instructor in instructor_details:
                    instructor_id = instructor['_id']
                    instructor_name = instructor['name']
                    instructors_dict[instructor_id] = instructor_name
            return courses,instructors_dict
           
        except Exception as e:
            logging.exception("An error occurred while getting course list: {}".format(str(e)))
            return None