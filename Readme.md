## Project: Data Pipeline
### 1. Project Overview
The project consists of the following components:

Application: Generates and sends fake data to a PostgreSQL database.
PostgreSQL Database: Stores the data sent by the application.
pgAdmin: Provides an interface for managing the PostgreSQL database.
### 2. Project Structure
Dockerfile: Defines how to build the Docker image for the application.
docker-compose.yml: Configures and manages the Docker containers.
Servers.json: Configuration file for pgAdmin.
main.py: The main script for generating and inserting data into PostgreSQL.
### 3. Running the Project
3.1 Installing Docker and Docker Compose
Install Docker and Docker Compose by following the instructions on the official Docker website and Docker Compose website.
https://docs.docker.com/desktop/install/windows-install/
https://docs.docker.com/compose/install/

#### 3.2 Cloning the Repository
Clone the repository or download the files as a ZIP archive and extract them.

`cd <repository_folder>`
#### 3.3 Starting the Containers
Navigate to the directory containing docker-compose.yml.

`cd path_to_directory`
Build and start the containers.

`docker-compose up --build`
The --build flag ensures that Docker rebuilds the images if there are any changes.

#### 3.4 Checking the Setup
Containers: Verify that all containers are running.

`docker ps`

pgAdmin: Open your browser and go to http://localhost:8080. Use the connection settings from Servers.json to connect to the PostgreSQL database.

### 4. Code Description
#### 4.1 main.py

__create_db_if_not_exists:__ Creates the database if it does not already exist.  
__create_table_if_not_exists:__ Creates the user_metrics table if it does not already exist.    
__db_connection:__ Establishes a connection to the PostgreSQL database.  
__generate_user_metrics:__ Generates fake user metrics data.  
__insert_metrics:__ Inserts generated metrics data into the user_metrics table.  
__stream_user_metrics:__ Continuously generates and inserts data into the database.  
__main:__ Runs the stream_user_metrics function.
#### 4.2 Dockerfile
__FROM python:3.9:__ Uses Python 3.9 as the base image.  
__WORKDIR /app:__ Sets the working directory inside the container.  
__COPY . /app:__ Copies project files into the working directory of the container.  
__RUN pip install -r requirements.txt:__ Installs project dependencies.  
__CMD ["python", "main.py"]:__ Runs the main script.
#### 4.3 docker-compose.yml
__app:__ Defines the service for the application.  
__db:__ Defines the service for PostgreSQL.  
__pgadmin:__ Defines the service for pgAdmin.  
__networks:__ Configures network communication between containers.  
__volumes:__ Defines volumes for data persistence.
#### 4.4 Servers.json
Configuration file used by pgAdmin to connect to the PostgreSQL database. It includes:

__Name:__ The name of the server.  
__Host:__ The hostname or IP address of the PostgreSQL container.  
__Port:__ The port PostgreSQL is running on (default is 5432).  
__MaintenanceDB:__ The default database to connect to.  
__Username:__ The username for connecting to PostgreSQL.  
__Password:__ The password for the username.  
__SSLMode:__ The SSL mode for the connection.