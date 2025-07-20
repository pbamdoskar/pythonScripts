#!/usr/bin/env python3

import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def main():
    try:
        # Authenticate using the default Azure credential (Managed Identity)
        credential = DefaultAzureCredential()

        # Set your Azure subscription ID as an environment variable or hard-code it
        subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", "255b7234-0c59-4300-a866-2c563ecd5edc")

        # Initialize ResourceManagementClient
        resource_client = ResourceManagementClient(credential, subscription_id)

        # List all resource groups
        print("Listing resource groups in subscription:")
        for rg in resource_client.resource_groups.list():
            print(f"- {rg.name}")
    
    except Exception as e:
        print(f"Runbook failed with error: {str(e)}")

# This entry point is required in Azure Automation
main()
