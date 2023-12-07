from fastapi import FastAPI
from routers import health

#create an instance of FastAPI and customize metadata configurations
app = FastAPI(
        docs_url='/api/docs', #set the URL for the API documentation
        openapi_url='/api/openapi', #set the URL for the OpenAPI schema
        redoc_url=None, #disable the ReDoc documentation
        title='URL Shortener', #set the title of the API
        description='**URL Shortener** a *RESTful API* to provide a service for shortening long URLs into more manageable and shareable links.', #set the description of the API
        summary='Open-source project that aims at providing a short URLs.', #set a summary for the API
        version='0.0.1', #set the version of the API
        contact={'name': 'URL Shortener', 'url': 'https://github.com/antenehbedilu/urlshortener', 'email': 'hello@antenehbedilu.com'}, #set the contact information for the API
        license_info={'name': 'MIT License', 'url': 'https://raw.githubusercontent.com/antenehbedilu/urlshortener/main/LICENSE'}) #set the license information for the API

#include the health router in the FastAPI application
app.include_router(health.router)
