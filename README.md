# 🥢 Good Chef Chinese Takeaway

A modern, responsive Chinese takeaway restaurant website built with Django, featuring a clean white and red theme inspired by Canton Chinese Takeaway.

## 🌟 Features

- **Modern Design**: Clean white and red theme with professional styling
- **Full Menu System**: Complete menu with categories and items
- **Shopping Cart**: Add items to cart with real-time updates
- **Checkout System**: Complete checkout process with delivery form
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Multiple Pages**: Home, Menu, About Us, Contact, Delivery, and Checkout
- **Database**: SQLite database with 74 menu items across 9 categories

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Good Chef"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Visit the website**
   - Open your browser and go to `http://127.0.0.1:8000/menu/`

## 📱 Website Pages

- **Home**: `http://127.0.0.1:8000/`
- **Menu**: `http://127.0.0.1:8000/menu/`
- **About Us**: `http://127.0.0.1:8000/menu/about/`
- **Contact**: `http://127.0.0.1:8000/menu/contact/`
- **Delivery**: `http://127.0.0.1:8000/menu/delivery/`
- **Checkout**: `http://127.0.0.1:8000/menu/checkout/`

## 🍽️ Menu Categories

1. **Starters** 🥟 - Spring rolls, prawn crackers, etc.
2. **Soups** 🍲 - Hot and sour soup, sweet corn soup, etc.
3. **Chicken Dishes** 🍗 - Sweet and sour chicken, kung pao chicken, etc.
4. **Beef Dishes** 🥩 - Beef in black bean sauce, beef curry, etc.
5. **Pork Dishes** 🐷 - Sweet and sour pork, char siu pork, etc.
6. **Seafood Dishes** 🐟 - Sweet and sour fish, prawn curry, etc.
7. **Vegetable Dishes** 🥬 - Stir-fried vegetables, tofu dishes, etc.
8. **Rice & Noodles** 🍚 - Fried rice, chow mein, etc.
9. **Desserts** 🍮 - Ice cream, fruit salad, etc.

## 🛒 Shopping Cart Features

- Add items to cart with quantity tracking
- Real-time cart updates
- Remove items from cart
- Cart persistence using localStorage
- Order summary with subtotal and delivery costs
- Free delivery on orders over £15

## 💳 Checkout Process

- Customer information form
- Delivery address and instructions
- Payment method selection
- Order summary with total calculation
- Order confirmation

## 🎨 Design Features

- **Color Scheme**: White background with red (#d32f2f) accents
- **Typography**: Clean, readable fonts
- **Icons**: Emoji icons for visual appeal
- **Responsive**: Mobile-first design approach
- **Animations**: Smooth hover effects and transitions
- **Professional Layout**: Clean navigation and footer

## 🛠️ Technical Stack

- **Backend**: Django 4.2+
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: Emoji icons for simplicity

## 📁 Project Structure

```
Good Chef/
├── goodchef/
│   ├── goodchef/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── menu/
│   │   ├── migrations/
│   │   ├── templates/menu/
│   │   │   ├── base.html
│   │   │   ├── menu_list.html
│   │   │   ├── checkout.html
│   │   │   ├── about.html
│   │   │   ├── contact.html
│   │   │   └── delivery.html
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   └── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## 🔧 Configuration

The project uses Django's default settings with the following key configurations:

- **Database**: SQLite (db.sqlite3)
- **Static Files**: Served by Django development server
- **Templates**: Django template engine
- **URLs**: Clean URL structure with namespacing

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure environment variables
5. Use a production WSGI server (Gunicorn, uWSGI)

## 📞 Contact Information

- **Phone**: 01234 567890
- **Email**: info@goodchef.co.uk
- **Address**: 123 High Street, Bedford
- **Hours**: Daily 5pm - 11pm

## 📄 License

This project is created for educational and demonstration purposes.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Good Chef Chinese Takeaway** - Authentic Chinese cuisine since 1995 🥢
