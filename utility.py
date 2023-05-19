import requests
from bs4 import BeautifulSoup as bs
import json
from url import courses_url,thumbnail_url
from courses import get_courses
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR)

class ineuron_scraping:
    #Function to get the courses segregated into different categories and subcategories
    def get_categories():
        try:
            courses,instructors_dict = get_courses()
            response = requests.get(courses_url)
            soup = bs(response.content, 'html.parser')
            courses_data = soup.find("script", {"id": "__NEXT_DATA__"})
            courses_json = json.loads(courses_data.text)
            categories = courses_json['props']['pageProps']['initialState']['init']['categories']
            
            all_categories = {}
            for category_id, category_data in categories.items():
                sub_categories = category_data.get('subCategories', {})
                sub_category_titles = {}
                
                for sub_category_id, sub_category_data in sub_categories.items():
                    course_names = [course['title'] for course in courses if course['categoryId'] == sub_category_id]
                    sub_category_titles[sub_category_data['title']] = course_names
                
                all_categories[category_data['title']] = sub_category_titles
            
            return all_categories
        except Exception as e:
            logging.exception("An error occurred while getting categories: {}".format(str(e)))
            return None

    #Function to get the selected course details
    def get_course_details(cname):
        try:
            course_url = "https://ineuron.ai/course/" + cname
            res = requests.get(course_url)
            soup = bs(res.content, 'html.parser')
            course_data = soup.find("script", {"id": "__NEXT_DATA__"})
            course_json = json.loads(course_data.text)
            data = course_json['props']['pageProps']['data']
            details = course_json['props']['pageProps']['data']['details']
            meta = course_json['props']['pageProps']['data']['meta']
            courses,instructors_dict = get_courses()
            price_data = details["pricing"]
            curriculum = {
                c["title"]: [t["title"] for t in c["items"]]
                for c in meta["curriculum"].values()
            }
            
            course_details = {
                "Title": data["title"],
                "Description": details["description"],
                "Instructors": [instructors_dict.get(instructor_id) for instructor_id in data['meta']['instructors']],
                "img_url": thumbnail_url+ details["img"],
                "Duration": meta["duration"],
                "Language": meta["overview"]["language"],
                "Price": 0 if price_data['isFree'] else price_data['IN'],
                "Requirements": meta["overview"]["requirements"],
                "Features": meta["overview"]["features"],
                "Learn": meta["overview"]["learn"],
                "Curriculum": curriculum
            }
            
            return course_details
        
        except Exception as e:
            logging.exception("An error occurred while getting course details: {}".format(str(e)))
            return None