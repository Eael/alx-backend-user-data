#!/usr/bin/env python3
""" Authentication Module
"""
import re
from typing import List, Typevar
from flask import request

class Auth:
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Gets authorization header from request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the Current user from the request
        """
        return None
