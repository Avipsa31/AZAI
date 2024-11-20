AI_SERVICE_ENDPOINT="https://xxxxxxxxxxxxxxxxxxx.azure.com/"
AI_SERVICE_KEY="6ZMyOQRnxxxxxxxxxxxxxxQQJ99AKACYeBjFXJ3w3AAAaACOGfoVK"
QA_PROJECT_NAME=LearnFAQ
QA_DEPLOYMENT_NAME=production







from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:
        # Load configuration settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Validate environment variables
        if not all([ai_endpoint, ai_key, ai_project_name, ai_deployment_name]):
            raise ValueError("One or more environment variables are missing.")

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

        # Submit questions in a loop
        user_question = ''
        print("Type 'quit' to exit.")
        while user_question.lower() != 'quit':
            user_question = input('\nQuestion:\n')
            if user_question.lower() == 'quit':
                print("Exiting the application.")
                break

            # Get answers from the QnA service
            response = ai_client.get_answers(
                question=user_question,
                project_name=ai_project_name,
                deployment_name=ai_deployment_name
            )
            
            # Display answers
            for candidate in response.answers:
                print(f"Answer: {candidate.answer}")
                print(f"Confidence: {candidate.confidence}")
                print(f"Source: {candidate.source}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()