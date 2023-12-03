FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
COPY ./FastAPI /app
RUN apt-get clean && apt-get update && apt-get install -y locales
# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "movie_app:movie_app", "--host", "0.0.0.0", "--port", "80"]