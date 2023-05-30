# DocExtract

To run the web app, you need to build a Docker image using the following command in the terminal:

Copy code
docker build -t app .
Once the Docker image is built, you can run the app using the following command:

arduino
Copy code
docker run -p 8501:8501 --name docextract app
To access your Streamlit app from a browser, you can use either of the following URLs:

Local URL: http://localhost:8501 or http://127.0.0.1:8501
Simply open any web browser and enter one of the above URLs to access the Streamlit app running on your local machine.
