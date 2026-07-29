# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API in Python using FastAPI so you can practice routing, request handling, and JSON responses for a simple resource.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a basic FastAPI application and verify that it runs locally.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create an app with a root endpoint that returns a welcome message
- Start the server and confirm the endpoint responds correctly

### 🛠️ Build CRUD Endpoints

#### Description
Add endpoints for creating, reading, updating, and deleting items in your API.

#### Requirements
Completed program should:

- Define a simple resource such as tasks or books
- Add endpoints to list all items and retrieve one item by ID
- Add endpoints to create, update, and delete an item
- Return JSON data and use appropriate status codes

### 🛠️ Add Validation and Documentation

#### Description
Improve the API so it is easier to use and understand.

#### Requirements
Completed program should:

- Use Pydantic models for request and response data
- Validate required fields and correct data types
- Explore the automatic documentation available at /docs
