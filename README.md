### Book Library Project
By Konrad Kantorski
### Project Objective and overview

•	To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.
The book library app will aim to enable users to:
Create – by being able to add readers and books
Read – by being able to view all readers and all books 
Update – by being able to update already existing information regarding readers and books
Delete – by being able to delete readers and books

The application will be coded in python using the flask micro-framework which will provide front end functionality and usability with http servers. In order to make the app more user friendly the python template jinja2 will be used to create HTML and return to the http response. The app will also include a relational database which will allow to store data for the duration of the project. Furthermore, to ensure quality standards of the code, the app will include a series of unit tests using python, integration tests using selenium and automated tests to validate the application. Lastly, the code will be fully integrated with a version control system (Git - github) that will allow our continuous integration system (Jenkins) to pull the code using a webhook and subsequently deploy the application on a Google cloud based virtual machine using gunicorn. 

### Documentation and Design

At the beginning of the project I decided to use 4 tables. However, this proved to be too complicated to tackle given the time constraints and thus I reverted back to the recommendation from the project specifications of creating a minimum viable product. Thus, as depicted in the entity relationship diagram below, the app utilises two tables of readers and books, with a one to many relationship that allows readers to input multiple books that they are currently reading. 

![image](https://user-images.githubusercontent.com/108797859/183068493-0cf72282-7c22-4d13-8159-8d7518b36008.png)

Furthermore, nullable fields were deemed as optional as readers could find those out from the rest of the information. More information regarding the reader was deemed not necessary as this is not supposed to be a business, this can be changed into the future should I wish to make further versions which may include a newsletter etc. 

##### Kaban boards and to do lists

During the project I used simple Kanban boards, as well as physical to do lists that allowed me to plan my work ahead and ensure that I was going to complete the project before the deadline. An example of a Kanban board I used can be seen below.

![image](https://user-images.githubusercontent.com/108797859/183068590-431b1dda-c526-4a4f-be0c-957509bc731b.png)

In addition, I found that brief journaling and reflection at the end of the day was helpful with identifying any problems, accomplishments and if I was making good progress in the project. This has also allowed me to become better at planning for the next stages. 

##### User Stories
Generating user stories during the design phase helped me producing a better idea of how the application should work. Here are some examples:

•	As a user I wish to easily navigate across the application so that I can add myself as a reader, add any books which I am reading, as well as displaying that I am reading those books

•	As a user I want to update information regarding my name and surname if I change my mind and wish not to share personal details

•	As a user I wish to update any books I am reading if I start to believe that a different description is more suitable

•	As a user I wish to delete both myself and the book so that the information I provided is no longer displayed

•	As a user I wish to see other users and also see what they are reading

•	As a developer I wish to have a functioning application that allows user to store their data 

•	As a developer I wish to utilise google cloud platform for virtual machines so that I do need extra tools locally 

•	As a developer I wish to be able to make updates to the application so that I can make improvements 

•	As a developer I want to have a high coverage of tests to ensure that the code is robust

#### Risk Assessment 
Conducting a basic risk assessment with the tools I use in mind has helped me to think about what issues I may encounter and what measures I should take to prevent them

![image](https://user-images.githubusercontent.com/108797859/183068716-2b4afaf2-5ac7-4d20-a814-17f6f22b4b87.png)

#### Front End display

The homepage display welcomes with a short message about the app.

![image](https://user-images.githubusercontent.com/108797859/183075566-31f07e79-9c8d-4008-aa7a-303e1594cea5.png)

It also contains hyperlinks to easily navigate through the app, allowing users to easily access CRUD functions.

![image](https://user-images.githubusercontent.com/108797859/183075795-8b83d1b0-6e2c-42a9-b32f-263944af485d.png)

![image](https://user-images.githubusercontent.com/108797859/183075901-684d4d9e-36c0-4bec-b4ee-f92d0107f201.png)

![image](https://user-images.githubusercontent.com/108797859/183076024-116a3eeb-79c1-4316-8ad7-29f5e20d7351.png)
 
 
Readers can access their reader page and add books directly from there.

![image](https://user-images.githubusercontent.com/108797859/183076336-f751b977-55c7-43a7-b9ab-055224c28eb0.png)



#### Testing 

I began the testing with unit tests that allowed me to test the CRUD functionality and routing. The intial get and post tests ran smoothly after correcting some spelling mistakes as well as ensuring that everything matches case sensitivity wise – I completed this process by reading the terminal output, which guided me. Although the update book test passed, not all all fields can be updated and I was unable to find the root of the problem and correct it. 

I then moved onto integration testing that allowed me to test the forms. I began with  the add reader form. Results from these tests are depicted below.

![image](https://user-images.githubusercontent.com/108797859/183068819-5c446bc5-77c7-4565-bcf8-a0317fd741de.png)

I was slightly confused by the high coverage as I did not test all the forms. I decided to run more tests to ensure that everything was running smoothly. I encountered problems with the add book integration test as depicted below.

![image](https://user-images.githubusercontent.com/108797859/183068917-a7a3a2b0-d170-4f96-963f-b594810be9c4.png)

I was unable to solve the problem with the use of the output as the console was not producing an xpath index for the book description text area. I also experimented with different inputs but that did not work either - I encountered this problem while I was conducting the add reader test and it worked, however I got an number for all the xpaths from the console. 

Automated testing through jenkins proved to be difficult at first, so I had to comment out the update book test initially before I got a complete build. I realised this was the problem through reading the console output.

![image](https://user-images.githubusercontent.com/108797859/183070262-f7968af8-bc4b-4b1a-aa59-c2de2a2c828a.png)

After initialising the build through a github pull via webhook, jenkins took some time to install all requirements and then proceeded to show the problems occured during testing.

![image](https://user-images.githubusercontent.com/108797859/183070607-254c1dea-6006-453a-9378-978e9862d1f1.png)

Next, I fixed the container problem and ran more builds that led me to finding out that there is a problem with updating a book.

![image](https://user-images.githubusercontent.com/108797859/183071041-e6f5beac-3294-49c8-86c6-efa0a53d3684.png)

I tested this out on the front end and found that updating the title of the book was not working, whilst the description and publication year changes were administered. Thus, since I was unable to fix the problem I looked for those changes in the tests, which proved successful.

![image](https://user-images.githubusercontent.com/108797859/183071358-07fe75d5-ddca-4282-a95c-ff28b959d990.png)

Upon the successful build, I connected it with a WSGI server by using gunicorn, which has allowed me to run the flask app on multiple threads. Furthermore, I added a deployment script that allows me the app to stop without continuously working. 

Lastly, I ensured that artefacts were archived so that I can access the reports.

![image](https://user-images.githubusercontent.com/108797859/183075090-111a7913-45b9-4406-9834-86a1e7dab9ce.png)

With the index report suggesting high coverage

![image](https://user-images.githubusercontent.com/108797859/183075214-9e0ddfff-cd16-4e55-919f-5e1e8878e176.png)

#### Reflection on the risk assessment

This framework has saved me some time as I had problems with GCP - mainly that the MySQL db did not work, despite taking the assumingly correct steps - thus to not waste more time I switched to SQLite. More minor problems were also present with the VMs which required to set up new ones with an older version of the Ubuntu OS. I also encountered a problem when setting versions of requirements - there must have been some inconsistency across the VMs and errors came up when I set their versions so I left them as they were (except for selenium).

#### Further versions of the app

Adding extra functionality and extending the abilities of the app are possible and achievable. One could link the app to a database of books and allow readers to update their reading wish list, with an ability to order those books through external stores and leaving their reviews on our app. 

#### Acknowledgments 

I would like to acknowledge and thank Adam Grey and Victoria Sacre for providing the neccessary training that has allowed me to complete this project.
Furthermore, credit and thanks go to the creators of the products used in the project, as well as countless people and their products that provide free guidence on how to solve problems.


