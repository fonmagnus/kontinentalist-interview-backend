<!-- GETTING STARTED -->

## Getting Started

This repository is created for Kontinentalist Interview Take Home Assignments. The purpose of this repository is to provide the backend server for the corresponding project.

The server is developed using Django REST framework as it is a server for API which can be consumed by client

The example of the client side repository can be found here
https://github.com/fonmagnus/kontinentalist-interview-frontend

<br/>

### Prerequisites

Make sure you have python installed in your local machine and you're good to go. To install python, you can download the package here
https://www.python.org/downloads/

or if you are using Mac OS X, you can install it via homebrew

- brew
  ```sh
  brew install python
  ```

or in Linux, you can use this command

- apt-get
  ```sh
  sudo apt-get install python3.8
  ```

<br/>

### Installation

To run this project in your local machine, just follow this simple steps

1. Create Python virtual environment
   ```sh
   python -m venv env
   ```
2. Activate the virtual environment
   ```sh
   source env/bin/activate
   ```
3. Install all required dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Django server
   ```sh
   python manage.py runserver
   ```

Your API server is now live and can be accessed at port 8000 (default port)
