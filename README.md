## Project Overview

This project is a RESTful API built with Python and Flask, designed to manage personal blog posts. It demonstrates core software engineering principles including object-oriented programming (inheritance), robust error handling, and persistent data storage using a MySQL database.

Features
Full CRUD Operations: Create, Read, Update, and Delete blog articles.

Database Persistence: All data is stored in a structured MySQL schema.

Robustness: Implements inheritance for database management and global exception handling.

Unit Tested: Core logic is validated through Python unit tests.

🛠 Tech Stack
Language: Python 3.x

Framework: Flask

Database: MySQL

Libraries: mysql-connector-python, pytest (for testing)

🚀 Getting Started

1. Prerequisites

Install MySQL Server

Install Python

2. Database Setup
   Run the following commands in your MySQL terminal:

CREATE DATABASE blogging_api;
USE blogging_api;

CREATE TABLE posts (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL,
content TEXT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3. Installation
   Bash

# Clone the repository

git clone <your-repo-link>

# Install dependencies

pip install flask mysql-connector-python

4. Running the App
   Bash
   python personal_blog.py
   The API will be available at http://127.0.0.1:5000

🛣 API Endpoints (Documentation)
MethodEndpointDescriptionGET/postsRetrieve all blog
postsGET/posts/<id>Retrieve a single post by IDPOST/posts
Create a new blog postPUT/posts/<id>
Update an existing postDELETE/posts/<id>Remove a post from the database
