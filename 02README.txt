README
Overview:

The repository contains a Python script, 02Image analysis.py, that performs image analysis using Azure's AI Vision services.
The script connects to Azure’s Vision API to analyze images and extract visual insights (e.g., object detection, scene understanding).
Built with Python, this project uses libraries like:
dotenv for environment variable management.
Pillow (PIL) for image handling.
Azure’s imageanalysis SDK for Vision API interactions.
Setup and Requirements:

Azure Vision API Setup:

Create an Azure Vision API resource on Azure’s platform.
Obtain the API endpoint and key.
Environment Variables:

Set up environment variables for secure credential storage.
AI_SERVICE_ENDPOINT: The Azure Vision API endpoint.
AI_SERVICE_KEY: The API key for authentication.
These variables can be stored in a .env file for easy management.
Script Execution:

Run the script with a command-line argument for the image file path:
bash
Copy code
python 02Image\ analysis.py path/to/image.jpg
If no image is specified, the script defaults to analyzing a predefined image file.
Functionality:

The script loads credentials and connects to Azure’s Vision API.
It processes the specified image file, analyzes its visual features, and displays the insights.
Use Case:

This project is suitable for developers interested in integrating Azure's Vision AI into applications that require automated image analysis and visual recognition.
Additional Notes:

Ensure all dependencies are installed, and the Azure account is set up before running the script.
The project aims to offer accessible AI-driven image analysis for various applications.