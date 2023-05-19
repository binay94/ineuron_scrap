1. This API helps to scrape course details from iNeuron website.
2. First user needs to update the user_input.py file with their MongoDB username, password, file path to save the course details pdf.
3. pip install requirements.txt to install the required modules to run the api.
4. Run application.py to select course category, course subcategory, course name to get course details of the selected course name.
5. Once the result page is displayed user can find a file with "selected course name.pdf" in the file path provided above.
6. User needs to run db_op.py to add all the available courses to MongoDB & a SQL database with filename courses.db is generated in the file path mentioned above.
7. The application uses logging to log all the information.
8. Data is scraped only for learning purpose and is deleted.
  
  
  
  # Output as shown below:
  
  
  ## Homepage:
  

    
  ## Results Page:
  

  
  ## Mongodb:
  

  
  ## PDF: 
 
  
  
  
  
  

