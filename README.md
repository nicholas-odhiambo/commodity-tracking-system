# commodity-tracking-system

A backend application for tracking agricultural commodities as they move througha warehouse. The system records commodity receipts, inventory levels, inspections and stock movements, providing an accurate and auditable view of warehouse operations.

# Current Status
This project is currently under active development

# Project Goals

The primary objective of this project are to:
- Learn and apply FastAPI in a real-world project.
- Practice designing and building RESTful APIs.
- Improve SQL and databse design skills using PostgreSQL.
- Apply software engineering principles such as separation of concerns, dependancy injection and layered architecture.
- Build a maintainalbe and scalable backend application.


# Features

- Current and planned feature include:

- Commodity management
- Warehouse management
- Inventory tracking 
- Stock movement (receiving and issuing)
- Commodity inspections
- Receipt management
- Transaction history 
- Reporting support 


# Technology stack:
- **Languange:** Python 3 
- **Framwork:** FastAPI
- **Database:** PostgreSQl 
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **API Testing:** Postman 
- **Database Migratioons:** Alembic (Planned - am new to this)


# Architecture

The project follows a layered architecture:

Client
   │
Routes (API)
   │
Services (Business Logic)
   │
Repositories (Database Access)
   │
PostgreSQL

Each layer has a single responsibility, making the application easier to maintain and extend.


# Learning Objectives

This project is being developed as a learning exercise to gain practical experience with:

- FastAPI
- SQLAlchemy
- PostgreSQL
- REST API design
- Database modeling
- Clean Architecture principles
- Dependency Injection
- Git and GitHub workflows

# Future Improvements

Planned enhancements include:

- User authentication and authorization
- Role-based access control
- Inventory reports and analytics
- Barcode/QR code support
- File attachments
- Docker deployment
- Automated testing
- CI/CD pipeline

