from fpdf import FPDF
from utility import ineuron_scraping as ins
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR)

def create_pdf(course_name,filepath):
    try:
    
        course_details = ins.get_course_details(course_name)

        if not isinstance(course_details, dict):
            raise ValueError("Invalid course details")

        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # Set font and size for the title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, course_details["Title"], ln=True, align="C")
        
        pdf.set_font("Arial", size=12)
        
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Description:", ln=True)
        pdf.set_font("Arial", size=12)
        description = course_details["Description"]
        lines = pdf.multi_cell(0, 10, description, align="L")
        
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Instructors:", ln=True)
        pdf.set_font("Arial", size=12)
        instructors = course_details.get('Instructors')
        instructors = instructors if instructors else ""  # Replace None with an empty string
        if isinstance(instructors, list):
            instructors = ', '.join(map(str, filter(None, instructors)))
        else:
            instructors = str(instructors)  # Convert instructors to a string if it's not a list
        pdf.multi_cell(0, 10, instructors, align="L")
        pdf.ln(10)


        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Duration:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, course_details["Duration"], ln=True)

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Language:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, course_details["Language"], ln=True)

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Price:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, str(course_details["Price"]), ln=True)

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Requirements:", ln=True)
        pdf.set_font("Arial", size=12)
        requirements = ', '.join(course_details['Requirements'])
        pdf.multi_cell(0, 10, requirements, align="L")
        pdf.ln(10)

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Features:", ln=True)
        pdf.set_font("Arial", size=12)
        features = ', '.join(course_details['Features'])
        pdf.multi_cell(0, 10, features, align="L")
        pdf.ln(10)

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Learn:", ln=True)
        pdf.set_font("Arial", size=12)
        learn = ', '.join(course_details['Learn'])
        pdf.multi_cell(0, 10, learn, align="L")
        pdf.ln(10)

        # Add curriculum
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Curriculum:", ln=True)
        pdf.set_font("Arial", size=12)
        for section, lessons in course_details['Curriculum'].items():
            pdf.cell(0, 10, f"- {section}:", ln=True)
            for lesson in lessons:
                pdf.cell(0, 10, f"  - {lesson}", ln=True)
        

            # Save the PDF file
        pdf.output(filepath)
        print(f"File Successfully Saved to {filepath}")

    except Exception as e:
        logging.exception("An error occurred while getting course details: {}".format(str(e)))
        return None




