# Fast-HTMX

## Description
Fast-HTMX is a demo project of [FastAPI](https://fastapi.tiangolo.com) and [HTMX](https://htmx.org).  The purpose of this project
is to illustrate how to create a website with no JavaScript, using only HTML, CSS, and
Python.  HTMX is a plugin that allows this to be possible.

## HTMX Attributes
The following HTMX attributes are used in this project:

- hx-get
- hx-post
- hx-trigger
- hx-target
- hx-push-url
- hx-indicator
- hx-swap

## Structure
db - Database setup

models - Data models

schema - Pydantic models

services - Database services

static - Static files

templates - Contains files for each page and partials for all partial pages that are related to the main page of the directory which it is under.

viewmodels - View models for gathering data for pages and partials.

main.py - Main operational file for running FastAPI.

## How to run
- Create virtual environment
- Activate virtual environment
- Install requirements `pip3 install -r requirements.txt`
- Run project `python3 -m uvicorn main:app --reload`
    ### Using Docker
    - Build image `docker build -t fast-htmx .`
    - Create Database `touch sql_app.db`
    - Run container `docker run -v $(pwd)/sql_app.db:/code/sql_app.db -d --name fast-htmx -p 8000:8000 fast-htmx`