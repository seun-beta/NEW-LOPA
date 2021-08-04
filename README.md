<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Layer of Protection Analysis (LOPA)</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> LOPA is a Graphical User Interface (GUI) used to evaluate high-consequence scenarios determining if the combination of probability of occurrence and severity of consequences meets a company’s risk tolerance.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Tech](#tech)
- [Installation](#installation)

- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

### Tech <a name = "tech"></a>

ToDo List is written in Python3 and Bottle 0.13.  
  
## Installation  <a name = "installation"></a>
  
#### Windows 10 Users

Please install and set up the following packages first. Ugrade if you find the package already installed:  
* Download [Python3](https://www.python.org/downloads/). It is advisable to install the package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.  
  ```sh
  python -V
  ```  
* Download [pip](https://pip.pypa.io/en/latest/installing) and follow the instructions in the link as an installation guide.  
* [SQLite3](https://sqlitebrowser.org/) (Ensure it is installed).
* It is advisable to use bottle in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this virtual environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:
  ```sh 
  py -m pip install virtualenvwrapper-win 
  ```
  
* Create a new virtual environment:
  ```sh
  mkvirtualenv <envname>
  ```
* Change your directory to the directory of the virtual environment

* Activate the virtual environment with:
  ```sh
  <envname>\Scripts\activate
  ```
* Install requirements in the virtual environment created:

  ```sh
  pip install -r requirements.txt
  ```
* Run server to ensure everything is running properly.
  ```sh
  python lopa.py
  ```
* Deactivate the virtual environment with:
  ```sh
  deactivate
  ```

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
