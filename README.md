# FacebookPoster
## what does this code do?
Hola soy reinoso
https://www.facebook.com/groups/2466772883410452/requests/?hoist_pending_member_ids_suggested_order=100041843405619&notif_id=1569537917676612&notif_t=group_r2j

This code creates a message on a Facebook group of your choosing which you have authority to write on.


## Installation
Simply clone the GitHub repository:

`git clone https://github.com/SubZKiller/FacebookPoster.git`

Install requirements:

Before we do anything we first need to install the libraries, to do so we open a command window (ctrl + alt + t) and copy each of the following lines pressing enter between them and accepting the installation 

`sudo apt-get install python-requests`

`sudo apt-get install python-pyquery`


## Usage

You must add your Facebook groupID where you want topost (Line Number 23)

```python
grupoID = "Your_GroupID" #(Fijo)

```
You must sign in to the Facebook account you wish to publish the message on by entering the username and password as well as inserting the group link you wish to publish on (Line Number 149)

```python
main(usernane='insert_username', password='insert_password', page='insert_URL')

```

After inserting all the information needed all you have to do is save changes and run the code

`python FacebookPoster.py`

Type your menssage and press Intro
