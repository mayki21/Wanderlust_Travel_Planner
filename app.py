from flask import jsonify
import os
import psycopg2
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from models import Destination, Itinerary, Expense
from flask_migrate import Migrate
from models import db

# Load environment variables from a .env file
load_dotenv()


app = Flask(_name_)
url = os.getenv("url")


# Connect to the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = url
db.init_app(app)
migrate = Migrate(app, db)





@app.route('/')
def hello():
    return "Welcome"
# Define a route for adding destinations


@app.route('/destinations', methods=['POST'])
def create_destination():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    location = data.get('location')

    new_destination = Destination(
        name=name, description=description, location=location)

    db.session.add(new_destination)
    db.session.commit()

    return jsonify({'message': 'Destination added successfully', 'id': new_destination.id}), 201
# Define a route for getting all destinations


@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()

    destination_list = []
    for destination in destinations:
        dest_dict = {
            'id': destination.id,
            'name': destination.name,
            'description': destination.description,
            'location': destination.location
        }
        destination_list.append(dest_dict)

    return jsonify(destination_list)


@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)

    if not destination:
        return jsonify({'message': 'Destination not found'}), 404

    dest_dict = {
        'id': destination.id,
        'name': destination.name,
        'description': destination.description,
        'location': destination.location
    }
    return jsonify(dest_dict)


@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.get_json()
    destination = Destination.query.get(destination_id)

    if not destination:
        return jsonify({'message': 'Destination not found'}), 404

    destination.name = data.get('name', destination.name)
    destination.description = data.get('description', destination.description)
    destination.location = data.get('location', destination.location)

    db.session.commit()

    return jsonify({'message': 'Destination updated successfully'})


@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)

    if not destination:
        return jsonify({'message': 'Destination not found'}), 404

    db.session.delete(destination)
    db.session.commit()

    return jsonify({'message': 'Destination deleted successfully'})


# Create an itinerary (POST `/itineraries`)


@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    destination_id = data.get('destination_id')
    activity = data.get('activity')

    # Check if the destination_id exists in the destinations table
    existing_destination = Destination.query.get(destination_id)

    if not existing_destination:
        return jsonify({'error': 'Destination not found'}), 404

    # If the destination exists, proceed to create the itinerary
    new_itinerary = Itinerary(destination_id=destination_id, activity=activity)
    db.session.add(new_itinerary)
    db.session.commit()

    return jsonify({'message': 'Itinerary added successfully', 'id': new_itinerary.id}), 201


# Get all itineraries for a specific destination (GET `/itineraries/destination/<int:destination_id>`)
@app.route('/itineraries/destination/<int:destination_id>', methods=['GET'])
def get_itineraries(destination_id):
    itineraries = Itinerary.query.filter_by(
        destination_id=destination_id).all()

    itinerary_list = [{
        'id': itinerary.id,
        'destination_id': itinerary.destination_id,
        'activity': itinerary.activity
    } for itinerary in itineraries]

    return jsonify(itinerary_list)


# Get a specific itinerary (GET `/itineraries/<int:itinerary_id>`)


@app.route('/itineraries/<int:itinerary_id>', methods=['GET'])
def get_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)

    if not itinerary:
        return jsonify({'message': 'Itinerary not found'}), 404

    itinerary_dict = {
        'id': itinerary.id,
        'destination_id': itinerary.destination_id,
        'activity': itinerary.activity
    }

    return jsonify(itinerary_dict)


# Update a specific itinerary (PUT `/itineraries/<int:itinerary_id>`)


@app.route('/itineraries/<int:itinerary_id>', methods=['PUT'])
def update_itinerary(itinerary_id):
    data = request.get_json()

    itinerary = Itinerary.query.get(itinerary_id)

    if not itinerary:
        return jsonify({'message': 'Itinerary not found'}), 404

    itinerary.destination_id = data.get('destination_id')
    itinerary.activity = data.get('activity')

    db.session.commit()

    return jsonify({'message': 'Itinerary updated successfully'})


# Delete a specific itinerary (DELETE `/itineraries/<int:itinerary_id>`)


@app.route('/itineraries/<int:itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)

    if not itinerary:
        return jsonify({'message': 'Itinerary not found'}), 404

    db.session.delete(itinerary)
    db.session.commit()

    return jsonify({'message': 'Itinerary deleted successfully'})


@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    destination_id = data.get('destination_id')
    expense_category = data.get('expense_category')
    amount = data.get('amount')

    destination = Destination.query.get(destination_id)
    if not destination:
        return jsonify({'error': 'Destination not found'}), 404

    expense = Expense(destination_id=destination_id,
                      expense_category=expense_category, amount=amount)
    db.session.add(expense)
    db.session.commit()

    return jsonify({'message': 'Expense added successfully', 'id': expense.id}), 201

# Get all expenses for a specific destination (GET `/expenses/<int:destination_id>`)
# Get all expenses for a specific destination (GET `/expenses/destination/<int:destination_id>`)


@app.route('/expenses/destination/<int:destination_id>', methods=['GET'])
def get_expenses_by_destination(destination_id):
    expenses = Expense.query.filter_by(destination_id=destination_id).all()

    if not expenses:
        return jsonify({'message': 'No expenses found for the destination'}), 404

    expense_list = [{'id': expense.id,
                     'destination_id': expense.destination_id,
                     'expense_category': expense.expense_category,
                     'amount': expense.amount} for expense in expenses]

    return jsonify(expense_list)

# Get a specific expense (GET `/expenses/<int:expense_id>`)


@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense_by_id(expense_id):
    with db:
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM expenses WHERE id = %s;", (expense_id,))
            expense = cursor.fetchone()

    if not expense:
        return jsonify({'error': 'Expense not found'}), 404

    expense_obj = Expense(expense[0], expense[1], expense[2], expense[3])
    return jsonify(expense_obj._dict_)


# Update a specific expense (PUT `/expenses/<int:expense_id>`)
@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense_by_id_update(expense_id):
    expense = Expense.query.get(expense_id)

    if not expense:
        return jsonify({'error': 'Expense not found'}), 404

    expense_data = {
        'id': expense.id,
        'destination_id': expense.destination_id,
        'expense_category': expense.expense_category,
        'amount': expense.amount
    }

    return jsonify(expense_data)

# Delete a specific expense (DELETE `/expenses/<int:expense_id>`)


@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)

    if not expense:
        return jsonify({'error': 'Expense not found'}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({'message': 'Expense deleted successfully'})



# Define the route to get weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')  # Get the location from the request

# Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
    api_key = os.getenv('api_key')

# Define the OpenWeatherMap API URL with the location and API key
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
    # Make the API request to get weather data
        response = requests.get(weather_url)
        data = response.json()

    # Check if the request was successful
        if response.status_code == 200:
        # Extract relevant weather information from the response
            weather_data = {
                'location': location,
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }

            return jsonify(weather_data), 200
        else:
            return jsonify({'error': 'Weather data not found'}), 404

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching weather data'}), 500


if _name_ == '_main_':
    app.run(debug=True)