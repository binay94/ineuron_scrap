# ineuron scrapping :

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
  
  ![Screenshot_6](https://github.com/binay94/ineuron_scrap/assets/116953493/708edec8-f3ed-4d88-ae9b-7f4c9278ba17)

  
![Screenshot_5](https://github.com/binay94/ineuron_scrap/assets/116953493/10ff3a3e-5b3b-4313-95de-b0c4a349ce5b)
    
  ## Results Page:
  
![Screenshot_7](https://github.com/binay94/ineuron_scrap/assets/116953493/fd2d1248-3ec1-4f24-8ad6-fb64b2d85eab)
  
  ## Mongodb:
  
![Screenshot_3](https://github.com/binay94/ineuron_scrap/assets/116953493/a271e073-cca6-48c9-913c-b0e59ec5a470)

  
  ## PDF: 
 
  ![Screenshot_9](https://github.com/binay94/ineuron_scrap/assets/116953493/0707612a-dc1d-4c1f-a695-dab76b0b536c)
  
  
  
  

