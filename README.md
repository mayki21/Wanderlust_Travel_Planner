

# Wanderlust Travel Planner



Wanderlust Travel Planner is your go-to Flask-based backend application designed to take your trip planning to the next level. With seamless database integration, this application empowers you to manage your travel destinations, create itineraries, and effortlessly track your expenses. Whether you're a seasoned traveler or just embarking on your journey, Wanderlust Travel Planner is here to make your adventures memorable and organized.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Database Integration](#database-integration)
- [Destination Management](#destination-management)
- [Itinerary Planning](#itinerary-planning)
- [Expense Tracking](#expense-tracking)
-[API Documentation](#API-documentation)

## Features

### 1. Database Integration
- Ihave choose render free tier Postgresql data base  and configure it to seamlessly support destination management, itinerary planning, and expense tracking.

### 2. Destination Management
- Create, update, delete, and view travel destinations with attributes like name, description, and location.

### 3. Itinerary Planning
- Plan your itinerary with ease. Add, update, and delete activities for selected destinations to make your trip unforgettable.

### 4. Expense Tracking
- Record and track your trip expenses effortlessly. Add expenses, categorize them, and stay on top of your budget.

## Getting Started

These instructions will help you set up the Wanderlust Travel Planner on your local machine for development and testing purposes.

1. Clone the repository:
   ```bash
   git clone https://github.com/mayki21/Wanderlust_Travel_Planner.git



## API Routes Documentation

### Destination Management

#### Create a Destination
- **Route:** `POST /destinations`
- **Description:** Add a new travel destination.
- **Request Body:** `name` (string), `description` (string), `location` (string).
- **Response:** `201 Created`, `{ "message": "Destination added successfully", "id": <destination_id> }`

#### Get All Destinations
- **Route:** `GET /destinations`
- **Description:** Retrieve a list of all travel destinations.
- **Response:** `200 OK`, Array of destination objects.

#### Get a Specific Destination
- **Route:** `GET /destinations/<destination_id>`
- **Description:** Retrieve details of a specific travel destination.
- **Response:** `200 OK`, Destination object. `404 Not Found` if not found.

#### Update a Destination
- **Route:** `PUT /destinations/<destination_id>`
- **Description:** Update the details of a specific travel destination.
- **Request Body:** `name` (string), `description` (string), `location` (string).
- **Response:** `200 OK`, `{ "message": "Destination updated successfully" }`. `404 Not Found` if not found.

#### Delete a Destination
- **Route:** `DELETE /destinations/<destination_id>`
- **Description:** Delete a specific travel destination.
- **Response:** `200 OK`, `{ "message": "Destination deleted successfully" }`. `404 Not Found` if not found.

### Itinerary Planning

#### Create an Itinerary
- **Route:** `POST /itineraries`
- **Description:** Plan activities for a destination.
- **Request Body:** `destination_id` (integer), `activity` (string).
- **Response:** `201 Created`, `{ "message": "Itinerary added successfully", "id": <itinerary_id> }`. `404 Not Found` if destination not found.

#### Get Itineraries for a Destination
- **Route:** `GET /itineraries/destination/<destination_id>`
- **Description:** Retrieve planned activities for a destination.
- **Response:** `200 OK`, Array of itinerary objects. `404 Not Found` if destination not found.

#### Get a Specific Itinerary
- **Route:** `GET /itineraries/<itinerary_id>`
- **Description:** Retrieve details of a specific activity in your itinerary.
- **Response:** `200 OK`, Itinerary object. `404 Not Found` if not found.

#### Update an Itinerary
- **Route:** `PUT /itineraries/<itinerary_id>`
- **Description:** Update details of a specific activity in your itinerary.
- **Request Body:** `destination_id` (integer), `activity` (string).
- **Response:** `200 OK`, `{ "message": "Itinerary updated successfully" }`. `404 Not Found` if not found.

#### Delete an Itinerary
- **Route:** `DELETE /itineraries/<itinerary_id>`
- **Description:** Delete a specific activity from your itinerary.
- **Response:** `200 OK`, `{ "message": "Itinerary deleted successfully" }`. `404 Not Found` if not found.

### Expense Tracking

#### Record an Expense
- **Route:** `POST /expenses`
- **Description:** Track trip expenses.
- **Request Body:** `destination_id` (integer), `expense_category` (string), `amount` (float).
- **Response:** `201 Created`, `{ "message": "Expense added successfully", "id": <expense_id> }`. `404 Not Found` if destination not found.

#### Get Expenses for a Destination
- **Route:** `GET /expenses/destination/<destination_id>`
- **Description:** Retrieve expenses for a destination.
- **Response:** `200 OK`, Array of expense objects. `404 Not Found` if destination not found.

#### Get a Specific Expense
- **Route:** `GET /expenses/<expense_id>`
- **Description:** Retrieve details of a specific expense.
- **Response:** `200 OK`, Expense object. `404 Not Found` if not found.

#### Update an Expense
- **Route:** `PUT /expenses/<expense_id>`
- **Description:** Update details of a specific expense.
- **Request Body:** `destination_id` (integer), `expense_category` (string), `amount` (float).
- **Response:** `200 OK`, `{ "message": "Expense updated successfully" }`. `404 Not Found` if not found.

#### Delete an Expense
- **Route:** `DELETE /expenses/<expense_id>`
- **Description:** Delete a specific expense.
- **Response:** `200 OK`, `{ "message": "Expense deleted successfully" }`. `404 Not Found` if not found.

### Weather Data

#### Get Weather Data
- **Route:** `GET /weather`
- **Description:** Retrieve current weather data for a location.
- **Query Parameter:** `location` (string).
- **Response:** `200 OK`, Weather data. `404 Not Found` if not available. `500 Internal Server Error` in case of issues.



