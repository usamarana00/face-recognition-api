# Face Verification API

## Overview
This Face Verification API provides a robust solution for verifying the authenticity of images using face recognition and anti-spoofing technology. It is designed to help integrate face verification features into various applications, ensuring security and authenticity in user interactions.

## Features
- **Upload Image**: Save a verified image after passing anti-spoofing checks.
- **Verify Image**: Compare a new image against a saved image to confirm identity and check for spoofing.

## Getting Started

### Prerequisites
- Python 3.8.8 
- Flask
- DeepFace
- Any other dependencies listed in `requirements.txt`

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/face-verification-api.git
2. Installing libraries:
   ```bash
   cd face-verification-api
   pip install -e .
3. running the script:
    ```bash
   python face-recognition-api


# Postman Setup
## Using the API with Postman

To simplify the interaction with the Face Verification API, a Postman collection has been prepared and exported as `face-recognition-api.postman_collection.json`. This collection includes pre-configured requests for both uploading and verifying images.

### Importing the Collection into Postman
1. **Download and Install Postman**: If you haven't already, download Postman from [Postman's official website](https://www.postman.com/downloads/) and install it.
2. **Import the Collection**:
   - Open Postman.
   - Click on the "Import" button at the top left corner of the application.
   - Drag and drop the `face-recognition-api.postman_collection.json` file into the import window, or use the file picker to locate and select the JSON file.
   - Confirm the import to load the collection into your Postman workspace.

### Using the Collection
Once imported, the collection will contain two primary requests configured for your convenience:

#### 1. Upload Image
- **Method**: POST
- **Endpoint**: `/upload`
- **Description**: This request allows you to upload an image along with an associated email address. The image will be checked for authenticity and saved if it passes anti-spoofing checks.
- **Body**:
  - `image`: (File) The image file you want to upload.
  - `email`: (Text) The email address associated with the image.

#### 2. Verify Image
- **Method**: POST
- **Endpoint**: `/verify`
- **Description**: This request allows you to submit a new image for verification against a previously uploaded image associated with an email address.
- **Body**:
  - `image`: (File) The new image file you want to verify.
  - `email`: (Text) The email address used for the reference image.

### Running Requests
- Select the request you wish to use from the left sidebar under the imported collection.
- Fill in the required parameters, such as the image file and email.
- Hit "Send" to execute the request. The response will appear in the lower section of the Postman interface.
