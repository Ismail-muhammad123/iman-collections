#!/bin/bash
python e-commerce/manage.py collectstatic && gunicorn --workers 2 e-commerce/imanClothing.wsgi