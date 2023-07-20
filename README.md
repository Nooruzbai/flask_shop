A simple shop application for demonstration.

Technologies utilized in the application:
1. Python3
2. Vanilla JavaScript/ajax
3. Flask
4. Flask-login
5. Flask-wtforms
6. SQLAalchemy
7. Postgresql
8. Bootstrap
9. Docker, DockerCompose

In order to install and launch the application, please follow the steps below:
1. If you do not have git, please install it.


2. Clone the repository from the GitHub using this command:
    git clone https://github.com/Nooruzbai/flask_shop_app.git  

5. After cloning the repository, please go to cloned folder and execute the commands in Linux or Windows command line bellow:

6. Create virtual environment:  
python3 -m venv venv.  
7. Activate the virtual environment:  
for Linux: source venv/bin/activate  
for Windows: python3 venv\Scripts\activate
8. Install the dependencies:  
pip install -r requirements.txt
4. In the main directory "flask_shop_app" create a ".env" file.


5. Fill the ".env" file with data:

SECRET_KEY=create a secret key  
POSTGRES_HOST=localhost


        Attention: If you want to run in docker services please change the DATABASE HOST part in "database_url"
        in source/__init__.py file such database_url = f'postgresql://{postgres_user}:{postgres_password}@db/{postgres_database}'

POSTGRES_DB=postgres  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=postgres  
UPLOAD_PATH=source/static/uploads  

6. In the main directory "flask_shop_app" create a ".flaskenv" file.

7. Fill the file with folowing data:  
FLASK_APP="source"  
FLASK_DEBUG=TRUE(In development mode, if not put FALSE)

8. If you are running "Docker" services please run: 
    sudo docker compose up --build


9. If you want to run locally please run:
    flask run


10. Please register and login with right credentials.


If you have encountered any issues, please write me to "nooruzbay@gmail.com".