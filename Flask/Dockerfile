FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
COPY ./app /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "movie_app_html:app", "--host", "0.0.0.0", "--port", "8080"]