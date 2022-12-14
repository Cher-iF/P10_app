#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""
    
    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "930e7336-3faf-428e-afd4-8bf6381edc30")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "U7-8Q~EnUmbE8_mP2enUdjoeRB5ivpz4wwJFfcqr")
    LUIS_APP_ID = os.environ.get("LuisAppId", "45c98dc5-6ad6-4693-a51f-89d28ffc032a")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "315164affd6148cb9530f673610b291e")
    #LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://p10luisapps-authoring.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "f3a09437-aa25-4288-b17f-82f8318e4471"
    )
