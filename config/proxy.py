"""Proxy configuration."""
import os

# Proxy settings
HTTP_PROXY = os.getenv('HTTP_PROXY', 'http://127.0.0.1:8118')
HTTPS_PROXY = os.getenv('HTTPS_PROXY', 'http://127.0.0.1:8118')

# Whether to use proxy
USE_PROXY = os.getenv('USE_PROXY', 'true').lower() == 'true'

def get_proxy_config():
    """Get proxy configuration dictionary."""
    if not USE_PROXY:
        return None
        
    return {
        'http': HTTP_PROXY,
        'https': HTTPS_PROXY
    }
