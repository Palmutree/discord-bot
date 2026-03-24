import os
from pathlib import Path

# Read the token from environment or env file
def _load_token():
    # First check if token is in environment (Replit Secrets)
    token = os.environ.get('DISCORD_TOKEN')
    if token:
        return token
    
    # Fall back to reading from local env file (for local development)
    env_file = Path(__file__).parent / 'env'
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if key == 'DISCORD_TOKEN':
                        return value.strip('"\'')
    return None

DISCORD_TOKEN = _load_token()

def load_env():
    """Load environment variables from the 'env' file or environment."""
    # Check environment variables first (Replit Secrets)
    if os.environ.get('DISCORD_TOKEN'):
        return
    
    # Fall back to env file
    env_file = Path(__file__).parent / 'env'
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        value = value.strip('"\'')
                        os.environ[key] = value
