
# PDF Question Generator

## Abstract
The PDF Question Generator is an automated tool that processes PDF documents to generate relevant interview and exam preparation questions. Utilizing advanced machine learning models, this system efficiently analyzes PDF content and formulates meaningful questions, aiding users in their study and preparation efforts.

## Introduction
The PDF Question Generator project aims to simplify the process of creating study and interview questions from PDF documents. By leveraging AWS Lambda, API Gateway, and Streamlit, this tool provides an easy-to-use interface for users to upload PDF files and receive generated questions. This project combines modern cloud services and machine learning to deliver a practical solution for students, educators, and professionals preparing for exams or interviews.

## Prerequisites
Before you start, ensure you have the following:

- **AWS Account:** To create Lambda functions and API Gateway.
- **Python Environment:** To work with the provided code.
- **Streamlit:** For building the user interface.
- **Necessary API Keys:** GROQ API Key and OpenAI API Key.


## Step-by-Step Guide

### Step 1: Setting Up the Lambda Function

#### a. Create a Lambda Function
- Log in to your AWS Management Console.
- Navigate to the **AWS Lambda** service.
- Click **Create function**.
- Select **Author from scratch**.
- Enter a function name (e.g., `PDFQuestionGenerator`).
- Choose **Python 3.8** (or later) as the runtime.
- Click **Create function**.

#### b. Add Environment Variables

- In the Lambda function configuration, find the **Environment variables** section.

- Add the following variables:
   - `GROQ_API_KEY`: Your GROQ API key.
   - `OPENAI_API_KEY`: Your OpenAI API key.

- The env variables can be access in the code as `groq_api_key=os.environ['GROQ_API_KEY']`

#### c. Upload the Code
- In the Lambda function configuration, go to the **Code** tab
- There will an exsisting `lambda_function.py` file paste the related code in it. And then add the related files `llm_model.py`, `llm_pipeline.py`, `preprocessing.py`, and `prompt.py`.

#### d. Add External Libraries
- AWS Lambda requires external libraries to be added as layers. - Follow the guide in my medium article abouthow to add external libraries as a layer in AWS Lambda
- [https://komalsai234.medium.com/how-to-add-external-libraries-as-a-layer-in-aws-lambda-function-8350280b665a](https://komalsai234.medium.com/how-to-add-external-libraries-as-a-layer-in-aws-lambda-function-8350280b665a)


### Step 2: Setting Up API Gateway

- Go to the **API Gateway** service in AWS.
- Click **Create API** and select **HTTP API**.
- Click **Build**.
- Add a new route:
   - Method: `POST`
   - Resource Path: `/generate-questions`
- Select **Add Integration** and choose your Lambda function.
-  Click **Next** and then **Create**.
- Create a Stage and Deploy the API
    - After creating the API and defining the route, follow these steps to deploy it:
        - In the API Gateway console, select your API.
        - In the left navigation pane, click on Stages.
        - Click Create to create a new stage.
        - Enter a name for the stage (e.g., dev, prod).
        - Click Create to deploy the API to the stage.
    - Note the endpoint URL provided for your deployed API stage. This is the URL you will use in your applications to access the API (https://your-api-id.execute-api.region.amazonaws.com/stage-name).

### Step 3: Setting Up Streamlit Interface

Open your terminal and run the streamlit file  `main.py`:

```bash
streamlit run main.py
```
### Step 4: Testing
- Open the Streamlit application in your web browser (the terminal will show the local URL).

- Upload a PDF file.
- The application will send the PDF to the Lambda function via the API Gateway.
- The generated questions will be displayed.
- Optionally, download the questions as a text file.


## Streamlit App Demo

https://github.com/Komalsai234/PDF-Question-Generator/assets/99163734/8741f837-f0c9-4efe-96d9-58b4ac2792ca


