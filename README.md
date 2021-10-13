# Fast-HTMX

## Description
Fast-HTMX is a demo project of FastAPI an HTMX.  The purpose of this project
is to illustrate how to create a website with no JavaScript, using only HTML, CSS, and
Python.  HTMX is a plugin that allows this to be possible.

## Structure
db - Database setup

models - Data models

schema - Pydantic models

services - Database services

static - Static files

templates - Contains files for each page and partials for all partial pages that are related to the main page of the directory which it is under.

viewmodels - View models for gatering data for pages and partials.

main.py - Main operational file for running FastAPI.

## How to run
- Create virtual environment
- Activate virtual environment
- Install requirements `pip3 install -r requirements.txt`
- Run project `python3 -m uvicorn main:app --reload`