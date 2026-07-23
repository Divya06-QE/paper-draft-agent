from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from azure.identity import DefaultAzureCredential
from .config import FOUNDRY_PROJECT_ENDPOINT, FOUNDRY_MODEL_NAME


def get_llm():
    return AzureAIChatCompletionsModel(
        endpoint=FOUNDRY_PROJECT_ENDPOINT,
        model=FOUNDRY_MODEL_NAME,
        credential=DefaultAzureCredential(),
    )
