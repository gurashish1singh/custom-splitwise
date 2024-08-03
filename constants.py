from __future__ import annotations

# Splitwise related constants
SPLITWISE_SITE = "https://secure.splitwise.com"
SPLITWISE_API_VERSION = "/api/v3.0"
SPLITWISE_BASE_URL = f"{SPLITWISE_SITE}{SPLITWISE_API_VERSION}"
SPLITWISE_AUTHORIZE_URL = f"{SPLITWISE_SITE}/oauth/authorize"
SPLITWISE_TOKEN_URL = f"{SPLITWISE_SITE}/oauth/token"

# User Endpoints
SPLITWISE_GET_USER = f"{SPLITWISE_BASE_URL}/get_user"
SPLITWISE_GET_CURRENT_USER = f"{SPLITWISE_BASE_URL}/get_current_user"

# Expenses Endpoints
SPLITWISE_GET_EXPENSE = f"{SPLITWISE_BASE_URL}/get_expense"
SPLITWISE_GET_EXPENSES = f"{SPLITWISE_BASE_URL}/get_expenses"

# Group Endpoints
SPLITWISE_GET_CURRENT_USER_GROUPS = f"{SPLITWISE_BASE_URL}/get_groups"
SPLITWISE_GET_GROUP = f"{SPLITWISE_BASE_URL}/get_group"

# Friend Endpoints
SPLITWISE_GET_CURRENT_USER_FRIENDS = f"{SPLITWISE_BASE_URL}/get_friends"
SPLITWISE_GET_FRIEND = f"{SPLITWISE_BASE_URL}/get_friend"
