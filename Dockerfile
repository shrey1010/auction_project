FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

# Define environment variable(s) if needed
# ENV VARIABLE_NAME=value

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "auction_project.wsgi:application"]
