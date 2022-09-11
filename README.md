For run this project you need use following steps:

1.Open your terminal, go to Desktop or another folder by 'cd' command;

2.Paste in terminal:'https://github.com/SpaceIgor/Parse_data'

3.Creating and activate your virtualenv - for windows: python -m venv <name_of_virtualenv> => <name_of_virtualenv>/Script/activate

4.Back to previos folder wich includes manage.py and run: "pip install --upgrade pip" => "pip install -r requirements.txt";

5.Activate modules in XAMPP: Apache and MySQL You can see how to connect it in the next video, if something didn’t work out for you: https://www.youtube.com/watch?v=yWD0yDMouVY To see your databases you can view them at: http://localhost/phpmyadmin

6.Now in the config.py file you need to enter your details to communicate with your database

7.Еhen you need to run the mysql_shema.py file to create the database shema and then run the main.py file to parse the data

8.you can export the database dump directly in phpadmin or follow the instructions: 'http://www.electronick.org.ua/articles/mysql/kak-sdelat-damp-basy-dannyh-mysql/'
