FROM d3fk/python_in_bottle
WORKDIR /usr/src/myapp
ADD dfens-app.py .
CMD python dfens-app.py