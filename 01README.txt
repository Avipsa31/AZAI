README
This repository provides a Python application that detects the language of a given text input using the Azure Text Analytics API.

The application runs interactively, prompting users to enter text, which it processes through Azure’s Text Analytics language detection service to determine the language.

Key features include:

Integration with Azure Text Analytics through the TextAnalyticsClient from the azure.ai.textanalytics package.
Secure handling of API credentials through environment variables. Sensitive information like the API endpoint and API key is securely loaded from a .env file using the dotenv package.
Usage:

The application operates in a loop, requesting text input from the user until they type "quit" to stop.
After each entry, the detected language is displayed on the console.
Error handling is included for issues like incorrect configurations or connection errors.
Requirements:

An Azure account with access to the Text Analytics API.
The API endpoint and API key for your Azure Text Analytics service.
Installed packages: dotenv and azure-ai-textanalytics.
Setup Instructions:

Clone the repository.
Install the required packages:
bash
Copy code
pip install python-dotenv azure-ai-textanalytics
Create a .env file with your Azure endpoint and key in the following format:
plaintext
Copy code
AI_SERVICE_ENDPOINT=your_azure_endpoint
AI_SERVICE_KEY=your_azure_key
Run the script with:
bash
Copy code
python <script_name>.py
Enter text to detect its language, and type "quit" to exit.
This setup allows easy configuration and straightforward usage, making it a convenient tool for language detection applications.






