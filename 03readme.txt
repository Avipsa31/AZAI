Image Text Analysis Tool - Documentation

This Python application is designed to perform text analysis on images using Azure AI Vision services. The tool is capable of processing both printed and handwritten text, making it versatile for various text extraction needs. The application leverages Azure's advanced AI capabilities to provide accurate text detection and analysis results.

To use this tool, users need to have an active Azure AI Vision Service subscription, which provides the necessary endpoint and authentication key. These credentials should be stored securely in an environment file. The application requires several Python dependencies including python-dotenv for environment variable management, Pillow for image processing, matplotlib for visualization, and the Azure AI Vision client library.

The application features a simple command-line interface that offers two main functions: analyzing printed text using a sample image (Lincoln.jpg) and reading handwritten text (Note.jpg). When processing an image, the tool performs comprehensive text analysis, detecting individual words and lines while providing detailed information about their location within the image.

For each analysis, the tool generates multiple outputs. It displays the detected text in the console, showing the exact text content along with precise bounding polygon coordinates for each line of text. At the word level, it provides additional details including the specific text, its position in the image, and a confidence score indicating the reliability of the detection. The tool also creates a visual output by saving an annotated version of the original image with cyan-colored bounding boxes highlighting the detected text.

The application is structured to handle errors gracefully, including issues related to file operations, API calls, and configuration problems. Users should ensure their images are stored in a designated 'images' folder within the project directory, and the output will be saved as 'text.jpg' in the root directory.

For proper setup, users need to configure their Python environment with the required dependencies and create an environment file containing their Azure credentials. The tool is designed to be user-friendly while providing professional-grade text analysis capabilities, making it suitable for both basic text extraction needs and more complex document analysis tasks.

This tool serves as an excellent solution for automating text extraction from images, whether for document digitization, data extraction, or content analysis purposes. Its ability to handle both printed and handwritten text makes it particularly valuable for diverse use cases in document processing and analysis.