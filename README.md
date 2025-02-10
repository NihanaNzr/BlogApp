# BlogApp
A full-featured Django-based blogging application.
## &nbsp;Overview
BlogApp is a Django-based blog application where users can create, edit, and delete blog posts. It supports user authentication, rich text formatting, and an intuitive UI for seamless blogging.
## &nbsp;Features

- Create, Read, Update, and Delete (CRUD) operations for blog posts.
- User Authentication (Register, Login, Logout).
- Rich Text Editor for blog content.
- List &amp; Detail View of blog posts.
- Author-based post management (Only authors can edit/delete their own posts).
- Mobile-Responsive UI with Bootstrap 5.


## &nbsp;Installation Guide
### 1. Clone the Repository
``` bash
git clone https://github.com/NihanaNzr/BlogApp.git
cd BlogApp
```
### 2. Create a Virtual Environment
``` bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py migrate
```
### 5. Run the Development Server
``` bash
python manage.py runserver
```
Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Register/Login: Create an account or log in.
- Create a Blog: Use the rich text editor to write a blog post.
- Edit/Delete Posts: Authors can modify or remove their own posts.
- Browse Blogs: View published blogs in a user-friendly interface.
## 🛠 Built With

- Django - Backend Framework
- Bootstrap 5 - Frontend Styling
- SQLite/PostgreSQL - Database


## &nbsp;Contact
- For any issues or feature requests, feel free to open an issue or reach out:
- Email: [nihananizar17@gmail.com](nihananizar17@gmail.com)
- GitHub: [NihanaNzr](https://github.com/NihanaNzr)
