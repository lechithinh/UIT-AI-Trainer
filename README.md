<div id="top"></div>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Last Commit][last-commit-shield]][last-commit-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- GETTING STARTED -->

# Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Prerequisites

This is an example of how to list things you need to use the software and how to install them.

-   Python 3 - [Download instructions here](https://www.python.org/downloads/)
-   Pip 3 (usually gets installed automatically with Python)
-   MySQL Server - If you haven't already, [download the package from here](https://dev.mysql.com/downloads/installer/), then create a user account and note the username and password

If all the above are satisfied, you may proceed to the next section.

## Installation 

Follow these insturctions to setup your own instance of the app:

(**<u>PS</u>**: The instructions may look lenghty, but they;re simple and just explained in detail, so please don't click away. I would highly recommend you having a look at the codebase and trying the app for yourself.)

### 1: Clone the repo

Find instructions for [cloning/downloading this repo here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository), then unzip the repository

Or if you have git command line installed, clone using this command:

```sh
git clone https://github.com/Just-Moh-it/HotinGo.git
```

### 2: Cd to the folder

Open terminal/cmd/powershell and change directory/folder to the cloned folder. [Here are the instructions](https://www.howtogeek.com/659411/how-to-change-directories-in-command-prompt-on-windows-10/)

The command for the same would be

```sh
cd Location\ To/Hotingo
```

### 3: Install the PIP packages/dependencies

After you cd into the repo folder, ensure you see the following cmd/terminal prompt

```sh
Something.../HotinGo $
```

If not, repeat the previous step.

After this, run the following command in cmd/terminal:

```sh
pip install -r requirements.txt
```

### 4: Setup the database

To create the database from the MySQL schema, either:

1: Copy-paste the contents of [sql/hms.sql](sql/hms.sql) directly into the MySQL command line, or

2: Use the command to do it automatically (from cmd)

```sh
mysql -u <mysql-username> -p<mysql-password> < hms.sql
```

This will create and setup the database.

(**<u>Note</u>**: Don't **include the "<>" angular brackets** in the command, and replace the `<mysql-username>` and `<mysql-password>` with the credentials created, as discussed in the [Prerequisites Section](#Prerequisites))

### 5: Add database credentials to the app

Start by renaming the `.example.env` file just `.env`, and then replacing the `Your-Username` and `Your-Password` values with the MySQL credentials.

### 6: Installing Fonts

In order to make the app's gui look good, you will have to install the Montserrat font. From the `assets` folder, install all three fonts (with `.ttf` format) by double clicking them.

### 7: It's done 🎉 | Run the app

Run `main.py` file with python 3 and you should see the login window, if you have followed each step correctly.

The default username and password are `username` and `password` respectively.


<p align="right">(<a href="#top">back to top</a>)</p>

## Extras

Here are some things you may try with the app

### Adding new users

To add new login credentials, you will have to create new users by directly adding records to the database in the `login` table. Run the command to insert new login credentials:

```sql
INSERT INTO login (username, password) values ("your-username", "your-password");
```

(**<u>PS</u>**: This is the only part of the app that requires direct database interactions, since you can't add a signup page to an admin-based application without compromising on security, though our previous app versions had the feature, along with reset and forget password.)

<p align="right">(<a href="#top">back to top</a>)</p>





