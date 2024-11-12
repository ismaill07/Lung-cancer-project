# Lung cancer

## Description
A Regression type prediction model using *Random Forest Regressor* algorithm. It uses R², MAE (Mean Absolute Error) and MSE (Mean Squared Error) as the metric for prediction. This model is used to predict lung cancer patient.

## Steps

### Building Files
1) app.py: which has regression model code
2) requirements.txt: which has the required library names
3) Liver Patient Dataset (LPD)_train.csv: .csv dataset which includes the data regarding counsumer forcast prediction
4) Dockerfile: which contains the commands to be run in docker
5) selenium_test.py: which contains the selenium code for automated testing
6) templates/index.html: in contains html (computer language) which is used to display the contents from app.py

### Git & Other Commands used in Command Prompt
1) `mkdir <file_name>` to create the folder
2) `cd <file_name>` to go inside the folder
3) `git init`, initializing folder as git repository
4) manually add all the files
5) `git add .` to add all the files into git track
6) `git commit -m "<message>"`, it commits whatever is there in the track
7) `git remote add origin <GitHub repository link>`, builds connection between git and github
8) `git push --set-upstream origin master`, sends all the files from git to github.


### Jenkins
1) created a new item with item name as **<item_name>**
2) selected *Freestyle project* as the item type
3) selected *Git* in **Source Code Management**
4) added *Execute Windows batch command* step in **Build Steps**
5) Saved the Configurations
6) Clicked build now

#### Output
  ![image](https://github.com/user-attachments/assets/ac461993-14b8-4cb4-b0ec-03e8800dd037)

### Dockers
1) used `cd` to go forward and `cd..` to do backward, to get to the correct path in command prompt (i.e. the folder where all the files including docerfile is located.
2) executed the command `docker build -t <docker_image_name> .` to build the docker image.
3) executed the command `docker run <docker_image_name>` to run the docker image.

#### Output
  ##### Command Prompt
  ![image](https://github.com/user-attachments/assets/809243a0-7abb-4784-8908-ef837ad15747)
  ![test 1 1 1](https://github.com/user-attachments/assets/8f8338be-1aca-4d59-a55a-a3879ecd0466)
  ![test 1 1 2](https://github.com/user-attachments/assets/dcce3b90-9774-407e-9826-a4a4de76f876)
  ![test 1 1 3](https://github.com/user-attachments/assets/d3615a52-0f2d-459b-846f-19a4ba21cc85)

  
  ##### Docker Hub
  ![image](https://github.com/user-attachments/assets/e318fd40-71ec-4f34-9585-506911d3aa04)


### Selenium
1) integrated flask into app.py. And build an html file called index.html inside templates folder.
2) created selenium_test.py file which contains the selenium code for autotesting app.py

#### Output
  ![image](https://github.com/user-attachments/assets/2e3f17a9-8313-4ce3-acb3-c53c3ff610bb)
