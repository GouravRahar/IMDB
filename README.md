# Project Setup and Configuration

This guide will help you set up the project and configure your PostgreSQL database. Follow the instructions below to get started.

---

## 1. Database Setup

### 1.1. Check if PostgreSQL is Installed
Make sure PostgreSQL is installed on your machine.  
If PostgreSQL is not installed, follow the official [PostgreSQL installation guide](https://www.postgresql.org/download/).

### 1.2. Create the Database and User

If the database is not already set up, follow these steps:

1. **Login to PostgreSQL:**

   ```bash
   psql postgres
   ```

2. **Create the Database:**

   ```sql
   CREATE DATABASE imdb;
   ```

3. **Create a User:**

   ```sql
   CREATE USER admin_user WITH PASSWORD '@$!@123[45]';
   ```

4. **Grant Permissions:**

   ```sql
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin_user;
   GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO admin_user;
   GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO admin_user;
   ALTER USER admin_user WITH SUPERUSER;
   ```

---

## 2. Environment Configuration

### 2.1. Create a `.env` File

In the root of your project (where `manage.py` is located), create a file named **.env** and add the following configuration:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=imdb
DB_USER=admin_user
DB_PASSWORD=@$!@123[45]
DB_HOST=localhost
DB_PORT=5432
```

These variables will be used in your Django settings to connect to your PostgreSQL database.

---

## 3. Project Dependencies

### 3.1. Install Packages & Libraries

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

---

## 4. Django Migrations

### 4.1. Make and Apply Migrations

Run the following commands to create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Running the Project

### 5.1. Start the Django Development Server

Run the following command to start the development server:

```bash
python manage.py runserver
```

You can now access your project at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 6. Postman Link for testing

  [POSTMAN](https://imdb-project.postman.co/workspace/New-Team-Workspace~ac1aae75-a97b-40db-8edb-51b52750fd42/collection/12167432-20ba75b0-7bc9-479e-a5bf-d0fba5491e5c?action=share&creator=12167432) link

---

Happy Coding! 🚀
