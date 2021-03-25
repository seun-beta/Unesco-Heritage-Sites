# Unesco World Heritage Sites

## Table of Contents

- [About](#about)
- [Data Model Diagram](#schema)
- [Getting Started](#getting_started)
- [Concepts I have learnt so far](#concepts_learnt)

## About <a name = "about"></a>

Unesco World Heritage Sites is a Django project that showcases my knowledge of creating good data models using One-To-Many Relationships and running scripts that load data into databases using Django's ORM.  

## Data Model Diagram <a name="schema"></a>
<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/seun-beta/Unesco-World-Heritage-Sites/blob/main/db.JPG" alt="Data Model Diagram for Unesco World Heritage Sites" border="0"></a>
</p>

<h3 align="center">Data Model Diagram</h3>

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  

### Prerequisites

- Python3 
 
- SQLite
- Django3

### Installing

A step by step series of examples that tell you how to get a development env running.

### Windows 10 Users

Please install and set up the following packages first. Ugrade if you find the package already installed:  
* Download [Python 3](https://www.python.org/downloads/). It is advisable to install the package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed. 
   
    Python 3 and above is needed to sucessfully run these programs.

  ```sh
  python -V
  ```  
  
* Download [pip](https://pip.pypa.io/en/latest/installing) and follow the instructions in the link as an installation guide. [Pip](https://pip.pypa.io/en/latest/installing) is the package manager for Python.

* [SQLite3](https://sqlitebrowser.org/) (Ensure it is installed).

* It is advisable to install Django in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this virtual environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  py -m pip install virtualenvwrapper-win 
  ```
  
- Create a new virtual environment.  

   **N/B**: The angle brackets **< >** should be ignored when typing your environment name.

  ```sh
  mkvirtualenv <envname>
  ```
    

* Change your directory to the directory of the virtual environment.

- Activate the virtual environment with:

  ```sh
  <envname>\Scripts\activate
  ```
  
- Install requirements in the virtual environment created:
  
  ```sh
  pip install django 
  ```

  ```sh
  pip install -r requirements.txt
  ```

- Run server to ensure everything is running properly.

  ```sh
  python manage.py runserver
  ```

- Deactivate the virtual environment with:

  ```sh
  deactivate
  ```

## Concepts I applied  <a name="concepts_learnt" ></a>  
These are a list of concepts I applied while building this project:

- Data modelling.  
- One-To-Many Relationships.
- Database normalization.
- Running automated scripts in Django using [Django Extensions](https://django-extensions.readthedocs.io/#:~:text=Django%20Extensions%20is%20a%20collection,admin%20extensions%20and%20much%20more.).
