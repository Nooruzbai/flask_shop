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

In order to install and launch the application, please follow the steps below:
1. If you do not have git, please install it.

2. Clone the repository from the GitHub using this command:
    git clone https://github.com/Nooruzbai/flask_shop_app.git

3. In the main directory "flask_shop_app" create a ".env" file.

4. Fill the ".env" file with data:
##SECRET_KEY=create a secret key
##POSTGRES_HOST=localhost
        Attention: If you want to run in docker services please change the DATABASE HOST part in "database_url"
        in source/__init__.py file such database_url = f'postgresql://{postgres_user}:{postgres_password}@db/{postgres_database}'
##POSTGRES_DB=postgres
##POSTGRES_USER=postgres
##POSTGRES_PASSWORD=postgres
##UPLOAD_PATH=source/static/uploads

5. In the main directory "flask_shop_app" create a ".flaskenv" file.
6. Fill the file with folowing data:
FLASK_APP="source"
FLASK_DEBUG=TRUE(In development mode, if not put FALSE)

7. If you are running "Docker" services please run: 
    sudo docker compose up --build

8. If you want to run locally please run:
    flask run

9. Please register and login with right credentials.

If you have encountered any issues, please write me to "nooruzbay@gmail.com".