# dZENcode Initiate Tech Task
## Description
This project uses Python, Django, psycopg2 (PostgreSQL) and Docker Compose.

## How to set up the project

### Requirments
1. Download and install an executable of the latest version of Python - https://www.python.org/downloads/
2. Download and install an executable of the latest version of Git - https://git-scm.com/downloads
3. Download and install an executable of the correct version of Docker - https://www.docker.com/products/docker-desktop/

In order to verify that you installed everything correctly, try to execute in your Terminal or Command Prompt these commands:
* <code>python --version</code>
* <code>git -v</code>
* <code>docker -v</code>
* <code>docker-compose -v</code>

If no error were occuring it means that everything is ready for the next stage.

### Installment
1. Create a folder on your machine on which this project should be installed.
2. On GitHub.com, navigate to the main page of the repository.
3. Above the list of files, click 'Code' and copy the URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type this command: <code>git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY</code>

### Running
1. Open the Terminal, type this command <code>docker-compose up --build</code>, then wait until all containers are creating.
2. In your browser, open a new tab and type in a URL input field <code>127.0.0.1:8000</code>. You should see this: ![first page](https://pylessons.com/media/Tutorials/django-website/django-first-app/blobid0.png)
3. Open the Terminal again and type this commands:
* <code>docker-compose exec web python manage.py makemigrations polls</code>
* <code>docker-compose exec web python manage.py migrate</code>
* <code>docker-compose exec web python manage.py createsuperuser</code>. Note that when you type this command you would need to type your own credentials (name, email, password).
4. In your browser, open a new tab and type in a URL input field <code>127.0.0.1:8000/admin</code>, log in with the credentials you created on a previous step. After that you would be able to create, view, edit and delete any users and comments from this admin panel.

<p align="center">
    <img src="https://media3.giphy.com/media/7yojoQtevjOCI/200w.webp?cid=dda24d506chtinc24mmurycy0ftxktpxor1y4ln0crqp5jfd&ep=v1_gifs_gifId&rid=200w.webp&ct=g" />
</html>