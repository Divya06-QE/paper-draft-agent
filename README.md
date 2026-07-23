# paper-draft-agent
# Paper Draft Multi-Agent System (Azure AI Foundry + LangGraph)

This project implements a multi-agent system in Azure AI Foundry using LangGraph/LangChain
to draft quarterly, half-yearly, and annual financial papers for multiple committees.

## Key features

- Multi-agent orchestration with LangGraph
- Azure AI Foundry + `langchain-azure-ai` integration
- Committee-specific templates (up to 10 committees)
- Data ingestion from:
  - SharePoint (previous papers, knowledge base)
  - Dataverse / Power Platform (metadata, meeting records)
- Notifications via Teams and Outlook
- Drafted papers stored in user-specific SharePoint locations

## High-level flow

1. **Committee router agent**  
   Routes request to the correct committee configuration and template.

2. **Data ingestion agent**  
   Pulls meeting agenda, notes, key points, action items, next steps, and historical papers.

3. **Drafting agent**  
   Uses LLM to pre-fill the committee-specific template.

4. **Review agent**  
   Applies basic checks, adds rationale, and prepares final draft.

5. **Notification agent**  
   Sends Teams/Outlook notifications with links to the stored draft in SharePoint.

## Setup

1. Create an Azure AI Foundry project and deploy a chat model (e.g. `gpt-4.1`).
2. Set environment variables:

   ```bash
   export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
   export FOUNDRY_MODEL_NAME="gpt-4.1"
   export TENANT_ID="<tenant-id>"
   export CLIENT_ID="<client-id>"
   export CLIENT_SECRET="<client-secret>"
   export SHAREPOINT_SITE_URL="https://<tenant>.sharepoint.com/sites/<site>"
   export SHAREPOINT_DOC_LIB="Documents"
   export DATAVERSE_ENV_URL="https://<org>.crm.dynamics.com"
   export POWER_PLATFORM_FLOW_URL="<flow-http-trigger-url>"
   export TEAMS_WEBHOOK_URL="<teams-incoming-webhook-url>"
   export OUTLOOK_SENDER_ADDRESS="<service-account@domain>"

