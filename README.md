# Server Dashboard Web Application

Multi-tier Web App Deployment

## Project Overview

This project is a Flask-based multi-tier web application deployed on AWS. It displays live server information including CPU usage, memory usage, disk usage, hostname, operating system details, and stores the collected metrics in an Amazon RDS MySQL database.

The application follows a three-tier architecture:

* Frontend: HTML, CSS, JavaScript
* Backend: Python Flask
* Database: Amazon RDS MySQL

The application is deployed on an Amazon EC2 instance and connects to Amazon RDS for data storage.

---

## Features

* Displays live CPU usage
* Displays memory usage
* Displays disk usage
* Displays server hostname
* Displays operating system information
* Displays current server time
* Stores server metrics in Amazon RDS
* Displays previously stored metrics on the History page
* Responsive web interface

---

## AWS Services Used

* Amazon EC2
* Amazon RDS (MySQL)
* Security Groups
* Amazon VPC

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* PyMySQL
* psutil
* Git
* GitHub

---

## Project Architecture

Browser

↓

Amazon EC2

↓

Flask Application

↓

Amazon RDS MySQL

---

## Project Structure

Multi-tier-Web-App-Deployment

app.py

database.py

requirements.txt

README.md

templates/

static/

---

## Application Workflow

1. User opens the application in a web browser.
2. Flask receives the request.
3. The application collects server information using the psutil library.
4. The collected metrics are stored in Amazon RDS.
5. Flask returns the dashboard page to the browser.
6. The History page retrieves stored records from Amazon RDS and displays them.

---

## Installation

Clone the repository

git clone https://github.com/bsudarshan7/Multi-tier-Web-App-Deployment.git

Move into the project directory

cd Multi-tier-Web-App-Deployment

Create a virtual environment

python -m venv .venv

Activate the virtual environment

Windows

.venv\Scripts\activate

Linux

source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open the application

http://localhost:5000

---

## Database

Database Name

server_dashboard

Table Name

server_metrics

The database stores:

* Hostname
* CPU Usage
* Memory Usage
* Disk Usage
* Timestamp

---

## Use Cases

This application can be used for:

* Server monitoring
* Infrastructure monitoring
* Learning Flask with AWS
* Learning Amazon RDS integration
* Monitoring EC2 instance health
* Cloud computing practice
* Python backend development practice

---

## Future Improvements

* Application Load Balancer
* Nginx Reverse Proxy
* Gunicorn
* Auto Scaling Group
* CloudWatch Monitoring
* User Authentication

---

## Application Screenshots

Dashboard

(Add dashboard screenshot here)

History Page

(Add history page screenshot here)

Amazon EC2

(Add EC2 screenshot here)

Amazon RDS

(Add RDS screenshot here)

---

## Author

Sudarshan Birajdar
