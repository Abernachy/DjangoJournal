# DjangoJournal
A basic journaling app I built in Django that I can deploy to my home server and I can use it to reflect on life and talk about things I've learned.  I spent a week going through a Django Tutorial and I wanted to build something I would use.

## Installation and Configuration
There are a few approaches you can do to this.  In production the app runs in its own container and connects to a PostgresDB running in another container.  In order to order to make this easier to set up and run, a docker file and a docker-compose file are provided.  Be aware that this was my first real jump into setting up docker with a project.  In my own homelab I have Portainer running on a Pi4 and for small applications like this one, I prefer to run it on that (I haven't regretted this decision yet, hopefully wont).

Trying to add the stack via Portainer's GUI kept giving me a lot of problems.  I would try and upload the .env file and it would read the environment variables, but then error out telling me there is no .env file provided -_-.  Then manually inputting the environment variables would work, but then it would error out in the App container saying the manage.py file doesnt exist.  Then you would run the docker command for entry override and you'd see the files in there and you'd have to tell yourself you aren't crazy, its the machine thats crazy.

So yea save yourself some headaches and do the following:
1) Clone this repo
2) set up your .env file with your 9 environment variables
3) Build the stack via '$ docker-compose up --build'
4) App will be at your localhost:8080


At some point I'll put this on a host outside of my homelab so I can get some experience deploying outside of my own network.


### Setting up via docker 
You must smash your face against the keyboard.  Smarter people will have a better idea but since I have


### Environment Variables
Whether you are using a .env file or adding the stack manually, you'll have to provide environment variables for both the database and the app.

```

DB_HOST=(can be the database ip or the name you set up in the compose, for me it was just 'db' since thats what I used in the docker-compose)
DB_PORT=(port of preference, I used "5432")
DB_USER=(name of the postgres user it'll set up on first run)
DB_PASSWORD=(password associated with the user account)
DB_NAME=(name of the database)
DJANGO_SECRET_KEY=(This must be provided, if the key is lost, look below for instructions)
DJANGO_ADMIN_USER=(admin user account it creates, it looks for 'admin' or what you use here)
DJANGO_ADMIN_EMAIL=(email for the admin account)
DJANGO_ADMIN_PASSWORD=(password for the admin account)

```
Admin account is mandatory as thats the account that can access url/admin panel.

### Retrieving lost DJANGO_SECRET_KEY
Without the secret key provided as an environment variable it absolutely doesn't work.  

What you will have to do is generate a new Secret Key via the DJango python shell.
```
$ python manage.py shell
> from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())

```
Then add that new secret key as an environment variable.

# Libraries
This app was built using Bootstrap 5, Django 5.3 and Djhtml

## Screenshots
![Journal List](images/Screenshot%20from%202025-03-15%2013-26-34.png)

![Looking at entries](images/Screenshot%20from%202025-03-15%2013-26-49.png)

![Journal Entry Page](images/Screenshot%20from%202025-03-15%2013-27-05.png)

