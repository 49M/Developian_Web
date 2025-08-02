# Developian

[![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)

**Developian** is a comprehensive personal development web application built with Django that empowers users to set, track, and achieve their goals through structured reflection and habit management.

## 🎯 Overview

Developian serves as your personal development companion, offering tools for:
- **Goal Setting & Tracking**: Create and monitor progress toward your personal and professional goals
- **Habit Management**: Build and maintain positive habits through structured tracking
- **Reflection Logging**: Document your journey with detailed reflections and notes
- **Scheduling**: Organize your time with daily and long-term planning tools
- **Progress Visualization**: Track your development over time

## ✨ Key Features

### 🎯 Goal Management
- Create, edit, and delete personal goals
- Track progress with detailed reflections
- Goal ownership and privacy (each user sees only their goals)
- Time-stamped goal creation and reflection entries

### 📝 Reflection System
- Add detailed reflections for each goal
- Edit existing reflections
- Chronological organization of thoughts and progress
- Rich text logging capabilities

### 👤 User Management
- Custom user authentication system
- Secure registration and login
- Email-based user accounts
- Password reset functionality

### 📅 Scheduling (Planned Features)
- Daily scheduling with drag-and-drop interface
- Long-term planning for recurring events
- Time management tools

### 🎨 User Interface
- Clean, responsive design with Bootstrap 5
- Mobile-friendly interface
- Intuitive navigation
- Inspirational quotes on the homepage

## 🚀 Getting Started

### Prerequisites

Before running Developian, ensure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Developian_Web.git
   cd Developian_Web
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv dev_env
   
   # Activate virtual environment
   # On macOS/Linux:
   source dev_env/bin/activate
   
   # On Windows:
   dev_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your web browser and navigate to `http://127.0.0.1:8000/`
   - Create a new account or log in to start using Developian

### Quick Start Guide

1. **Register an Account**: Visit the registration page to create your account
2. **Log In**: Use your credentials to access your personal dashboard
3. **Create Your First Goal**: Navigate to the Goals section and add a new goal
4. **Add Reflections**: Click on a goal to add reflections and track your progress
5. **Explore Features**: Check out the scheduling tools and other features as they become available

## 🏗️ Project Structure

```
Developian_Web/
├── dev_project/          # Main Django project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── developian/          # Core application
│   ├── models.py        # Goal and Reflection models
│   ├── views.py         # Application views
│   ├── forms.py         # Django forms
│   ├── urls.py          # App URL patterns
│   └── templates/       # HTML templates
├── accounts/            # User authentication app
│   ├── models.py        # Custom user model
│   ├── views.py         # Authentication views
│   └── forms.py         # User forms
├── dev_env/             # Virtual environment
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 🛠️ Technology Stack

- **Backend**: Django 5.0.6
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Custom Django authentication
- **Deployment**: Platform.sh ready

## 🔧 Configuration

### Environment Variables

For production deployment, consider setting these environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` in production
- `DATABASE_URL`: Database connection string
- `EMAIL_HOST_USER`: SMTP email username
- `EMAIL_HOST_PASSWORD`: SMTP email password

### Database Configuration

The application is configured to use:
- SQLite for local development
- PostgreSQL for Platform.sh deployment

## 📱 Usage Examples

### Creating a Goal
1. Log into your account
2. Navigate to "Goals" in the navigation menu
3. Click "Add New Goal"
4. Enter your goal description
5. Save to create your goal

### Adding Reflections
1. From your Goals page, click on any goal
2. Click "Add Reflection"
3. Write your reflection in the text area
4. Save to log your progress

### Managing Your Progress
- View all goals on the Goals page
- Click individual goals to see reflection history
- Edit or delete reflections as needed
- Track your development over time

## 🤝 Contributing

We welcome contributions to Developian! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Issues and Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Include steps to reproduce any bugs
4. Specify your environment (OS, Python version, etc.)

## 🚢 Deployment

### Platform.sh Deployment

The application is configured for Platform.sh deployment with:
- Automatic PostgreSQL database setup
- Static file handling
- Environment-based configuration

### Local Production Testing

```bash
# Set production-like settings
export DEBUG=False
export SECRET_KEY="your-secret-key"

# Collect static files
python manage.py collectstatic

# Run with production settings
python manage.py runserver
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Built with Django framework
- UI powered by Bootstrap 5
- Inspirational quotes feature for daily motivation
- Community feedback and contributions

## 🗺️ Roadmap

### Upcoming Features
- [ ] Habit tracking system
- [ ] Progress visualization charts
- [ ] Drag-and-drop daily scheduling
- [ ] Long-term recurring event planning
- [ ] Email notifications and reminders
- [ ] Goal sharing and collaboration
- [ ] Mobile app companion
- [ ] Data export functionality

### Version History
- **v1.0.0**: Core goal setting and reflection system
- **Future**: Enhanced scheduling and habit tracking

---

**Start your personal development journey today with Developian!** 🌟

For more information, visit our [documentation](docs/) or [contact us](mailto:support@developian.app).
