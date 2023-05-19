from flask import Flask, render_template, request,send_file
import os
import logging
from user_cred import file_path
from getpdf import create_pdf
from utility import ineuron_scraping as ins
logging.basicConfig(filename='scraper.log', level=logging.ERROR)



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            selected_category = request.form.get('category')
            categories = ins.get_categories()
            subcategories = categories.get(selected_category) if selected_category in categories else None

            selected_subcategory = request.form.get('subcategory')
            course_names = subcategories.get(selected_subcategory) if subcategories and selected_subcategory in subcategories else None

            selected_course_name = request.form.get('course_name')

            subcategories_disabled = not subcategories
            course_names_disabled = not course_names

            if course_names and selected_course_name in course_names:
                course_detail = ins.get_course_details(selected_course_name)
                path = f"{file_path}{selected_course_name}.pdf"
                create_pdf(selected_course_name,path)
                return render_template('results.html', course=course_detail)

        else:
            selected_category = None
            subcategories = None
            selected_subcategory = None
            course_names = None
            selected_course_name = None
            subcategories_disabled = True
            course_names_disabled = True

        categories = ins.get_categories().items()



        return render_template('index.html', categories=categories, subcategories=subcategories,
                            course_names=course_names, selected_category=selected_category,
                            selected_subcategory=selected_subcategory, selected_course_name=selected_course_name,
                            subcategories_disabled=subcategories_disabled, course_names_disabled=course_names_disabled)
    
    except Exception as e:
        logging.exception("An error occurred: {}".format(str(e)))
        return "An error occurred: {}".format(str(e))
    
    

if __name__ == '__main__':
    app.run(debug=True)