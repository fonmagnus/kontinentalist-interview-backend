<!-- GETTING STARTED -->

## Introduction

This repository is created for Kontinentalist Interview Take Home Assignments. The purpose of this repository is to provide the backend server for the corresponding project.

The server is developed using Django REST framework as it is a server for API which can be consumed by client

The example of the client side repository can be found here
https://github.com/fonmagnus/kontinentalist-interview-frontend

<br/>

## Prerequisites

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

## Installation

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

<br/>

## API Documentation

### Directory Structure

The Django REST API structured in this directories :

- `accounts`

  responsible for account management (login, register, authorization of JWT Token). Account management is adopted using `djoser` library

- `env`

  Virtual environment for python

- `root`

  Our main directory. Consists of several directories and files :

  - `api/v1`

    responsible for managing API endpoints (such as methods, permission, and business logic)

  - `modules`

    parent directory for another directories. Each directory within this module is responsible for entity management

    - `modules/posts`

      Responsible for `post` entity. This includes the model manager (`models.py`), urls to API (`urls.py`), permissions classes (`permissions.py`), and JSON serializers (`serializers.py`) for the `post` entity

  - `repositories`

    this is the DB accessor. Means that all classes within this module are responsible for the CRUD operations in repository / DB level

  - `services`

    this is the service implementation. We wrap the business logic inside this service. So on the API level, they just need to use the instance(s) of this service

  - `settings.py`

    main configuration for django framework

<br/>

## API endpoints

Once you have your server is up and running, all these endpoints are available for the API's entry points. You just need to append a hostname prefix for the URL (e.g. `http://localhost:8000`). For some endpoints, it requires some credentials (JWT token) to be attached in the header request as `Authorization` parameters. These endpoints will be marked as `requires JWT Token`

---

### Account management

- **[POST]** `/api/auth/users/`

  - Purpose : Registering a new user

  - Body Request params :

    - `role` : The name of the role (either `Admin` or `Member`)
    - `email` : The email of the new user
    - `name` : The name of the user
    - `password` : The password of the user
    - `re-password` : Must be the same as password

  - Example request

    ```json
    {
      "role": "Admin",
      "email": "aranmu@example.com",
      "name": "Aranmu Haesulla",
      "password": "helloworldatikap",
      "re_password": "helloworldatikap"
    }
    ```

  - Response :

    - `name` : The name of the newly registered user
    - `email`: The email of the user
    - `role` : The role of ther user

<br/>

- **[POST]** `/api/auth/jwt/create`

  - Purpose : Provide access and refresh token to the user using the basic email-password credentials

  - Body Request params :

    - `email` : The email of the new user
    - `password` : The password of the user

  - Example request :

    ```json
    {
      "email": "admin@email.com",
      "password": "admin"
    }
    ```

  - Response :

    - `access` : the access token
    - `refresh` : the refresh token

  - Example response :

    ```json
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODU3NzI2MSwianRpIjoiNWNiZmJhZDBlY2Y4NGVjMmJhOGE4YzJiMDI0OWRjMWQiLCJ1c2VyX2lkIjo0fQ.EQiboeeceyON3NDsE52RUGIkHVuI4Mn5c2WjcveAcOs",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDk0NDYxLCJqdGkiOiI5NDk4OTk1MTg2ZWY0NmU4YWVhZDVmZGYwMzZmNTIzNiIsInVzZXJfaWQiOjR9.d1XicQjqXQzSqCK7w0tZ37mb3qXSzjounc0KYQnl4BQ"
    }
    ```

<br/>

- **[POST]** `/api/auth/jwt/refresh`

  - Purpose : Provide the new access token to the user

  - Body Request params :

    - `refresh` : The refresh token

  - Example request :

    ```json
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODUzNzA2OSwianRpIjoiZjI3NzFmMDc1M2Y0NDJlYzk1MjU3NDIwODBjZmI3Y2EiLCJ1c2VyX2lkIjo4fQ.HT4IKDE9Z_6KNUIDKF92pSEoioPdUy6y0d8v7ikke88"
    }
    ```

  - Response :

    - `access` : the new access token

  - Example response :

    ```json
    {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDk0NDYxLCJqdGkiOiI5NDk4OTk1MTg2ZWY0NmU4YWVhZDVmZGYwMzZmNTIzNiIsInVzZXJfaWQiOjR9.d1XicQjqXQzSqCK7w0tZ37mb3qXSzjounc0KYQnl4BQ"
    }
    ```

- **[GET]** `/api/account/me`

  - **`requires JWT token`**

  - Purpose : Provide the user account's detail
  - Response :

    - `email` : the email of the user
    - `name` : the name of the user
    - `role` : the role of the user

  - Example response :

    ```json
    {
      "email": "aranmu@example.com",
      "name": "Aranmu Haesulla",
      "role": "Admin"
    }
    ```

---

### Posts management

- **[GET]** `/api/posts/all`

  - **`requires JWT token`** and **`requires Admin role`**

  - Purpose : See all the posts (only accessible by admin role)
  - Response :
    Consists of the list of all posts

    - `id` : the id of the post
    - `posted_by` : a user object who posts this post (consists of the `email`, `id`, `name`, and `role` of user)
    - `title` : the title of the post
    - `content` : the content of the post

  - Example response :

    ```json
    [
      {
        "id": 3,
        "posted_by": {
          "name": "Aranmu Haesulla",
          "role": "Admin",
          "id": 13,
          "email": "aranmu@example.com"
        },
        "title": "New Post Update",
        "content": "This is a new post update"
      },
      {
        "id": 6,
        "posted_by": {
          "name": "admin",
          "role": "Admin",
          "id": 4,
          "email": "admin@email.com"
        },
        "title": "This is Post",
        "content": "This is Me"
      }
    ]
    ```

- **[GET]** `/api/posts/get`

  - **`requires JWT token`**

  - Purpose : See all the posts which is posted by the user who requests
  - Response :
    Consists of the list of all posts that is posted by corresponding user

    - `id` : the id of the post
    - `posted_by` : a user object who posts this post (consists of the `email`, `id`, `name`, and `role` of user)
    - `title` : the title of the post
    - `content` : the content of the post

  - Example response :

    ```json
    [
      {
        "id": 3,
        "posted_by": {
          "name": "Aranmu Haesulla",
          "role": "Admin",
          "id": 13,
          "email": "aranmu@example.com"
        },
        "title": "New Post Update",
        "content": "This is a new post update"
      }
    ]
    ```

- **[GET]** `/api/posts/get/{id}`

  - **`requires JWT token`**

  - Purpose : See a single post detail by its post ID (only accessible by admin OR a user who writes that post)
  - Response :
    Consists of a single post detail

    - `id` : the id of the post
    - `posted_by` : a user object who posts this post (consists of the `email`, `id`, `name`, and `role` of user)
    - `title` : the title of the post
    - `content` : the content of the post

  - Example response :

    ```json
    {
      "id": 8,
      "posted_by": {
        "name": "admin",
        "role": "Admin",
        "id": 4,
        "email": "admin@email.com"
      },
      "title": "Abuba",
      "content": "abfsaufbasufbasfa"
    }
    ```

- **[POST]** `/api/posts/create`

  - **`requires JWT token`**

  - Purpose : Create a new post

  - Body Request params :

    - `title` : The title of the post
    - `content` : the content of the post

  - Example request :

    ```json
    {
      "title": "This is Post",
      "content": "This is Me"
    }
    ```

  - Response :
    A 200 OK status code and the post object IF the post creation is succeeded, or error code if there's a problem

  - Example response :

    ```json
    {
      "id": 16,
      "posted_by": {
        "name": "admin",
        "role": "Admin",
        "id": 4,
        "email": "admin@email.com"
      },
      "title": "This is Post",
      "content": "This is Me"
    }
    ```

- **[PUT]** `/api/posts/update/{id}`

  - **`requires JWT token`**

  - Purpose : Update an existing post by its id (can only be updated by admin or the user who owns the post)

  - Body Request params :

    - `title` : The title of the post
    - `content` : the content of the post

  - Example request :

    ```json
    {
      "title": "New Post Update",
      "content": "This is a new post update"
    }
    ```

  - Response :
    A 200 OK status code and the post object IF the post update is succeeded, or error code if there's a problem

  - Example response :

    ```json
    {
      "id": 16,
      "posted_by": {
        "name": "admin",
        "role": "Admin",
        "id": 4,
        "email": "admin@email.com"
      },
      "title": "New Post Update",
      "content": "This is a new post update"
    }
    ```

- **[DELETE]** `/api/posts/delete/{id}`

  - **`requires JWT token`**

  - Purpose : Delete an existing post by its id (can only be deleted by admin or the user who owns the post)

  - Response :
    A 200 OK status code and the message IF the post deletion is succeeded, or error code if there's a problem

  - Example response :

    ```json
    {
      "message": "Successfully delete post"
    }
    ```
