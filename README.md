# Background Removal Web App

A simple and modern web application to **remove the background from images** using Python, Flask, and `rembg`. The app allows users to upload an image, removes its background, displays the result on the page, and provides a download option.  

This project also supports **Docker**, so you can run it anywhere without installing dependencies manually.

---

## Features

- Upload JPG/PNG images and remove the background.
- Preview the processed image instantly in the browser.
- Download the resulting transparent PNG image.
- Clean and responsive UI with modern design.
- Docker-ready for easy deployment.

---

## Tech Stack

- **Backend**: Python 3.10+, Flask
- **Image Processing**: `rembg`, Pillow
- **Machine Learning Model**: U²-Net (`u2net.onnx`)
- **Frontend**: HTML, CSS (responsive design)
- **Containerization**: Docker

---

## Project Structure

background-remove/
│
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build instructions
├── u2net.onnx # Pre-trained U²-Net model (optional)
└── templates/
└── index.html # HTML template for the web page



---

## Installation (Without Docker)

1. Clone the repository:


git clone <repo-url>
cd background-remove
Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows (CMD): venv\Scripts\activate

Windows (PowerShell): venv\Scripts\Activate.ps1

Linux/macOS (bash/fish): source venv/bin/activate

Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open your browser at: http://localhost:5100

Using Docker

Make sure you have Docker installed.

Build the Docker image:

docker build -t background-remove .


Note: If you want to copy the u2net.onnx model manually, place it in the project root. Otherwise, rembg will download it automatically at runtime.

Run the Docker container:

docker run -p 5100:5100 background-remove


Open your browser at: http://localhost:5100
