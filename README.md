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


<p align="center">
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Tech](#tech)
- [Installation](#installation)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

LOPA is a Graphical User Interface (GUI) used to evaluate high-consequence scenarios determining if the combination of probability of occurrence and severity of consequences meets a company’s risk tolerance.

## Tech <a name = "tech"></a>

LOPA is written in Python 3  
  
## Installation  <a name = "installation"></a>
  
#### Windows 10 Users

Please install and set up the following packages first. Ugrade if you find the package already installed:  
* Download [Python 3](https://www.python.org/downloads/). It is advisable to install the package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.  
  ```sh
  python -V
  ```  
* Download [pip](https://pip.pypa.io/en/latest/installing) and follow the instructions in the link as an installation guide.  
* [SQLite3](https://sqlitebrowser.org/) (Ensure it is installed).
* It is advisable to use Tkinter in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this virtual environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:
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

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Imaging Library
- [SQLite](https://sqlite.org/index.html) - Database
- [PyInstaller](https://www.pyinstaller.org/) - Package Bundler

## ✍️ Authors <a name = "authors"></a>

- [@seun-beta](https://github.com/seun-beta) - Software Development
- [@seun-beta](https://github.com/seun-beta) - Software Development
- [@seun-beta](https://github.com/seun-beta) - Software Development



## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
