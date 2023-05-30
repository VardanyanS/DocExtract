## Base image
#FROM python:3.8
#
## Set working directory
#WORKDIR /DocExtract
#
## Copy project files to the working directory
#COPY . /DocExtract
#
## Install project dependencies
#RUN pip install -r requirements.txt
#
## Specify the command to run your application
#CMD ["python", "app.py"]

FROM python:3.8
WORKDIR /app

COPY app.py invoice_df.py dataframe_conversion.ipynb IMG_6473.jpg README.md requirements.txt /app/
#COPY data ./data
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
