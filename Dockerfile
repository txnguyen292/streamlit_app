# FROM continuumio/miniconda:latest
FROM python:3.7

WORKDIR /home/streamlit_app

COPY . .

RUN pip install -r requirements.txt

# RUN echo "Make sure streamlit is installed"
# RUN python -c "import streamlit"
EXPOSE 8501
CMD streamlit run app.py


/mnt/c/Users/tnguy/personal_projects/EnhanceIT/cat_vs_dog