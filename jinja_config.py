from jinja2 import FileSystemLoader, Environment

# Create a FileSystemLoader with multiple search paths
loader: FileSystemLoader = FileSystemLoader(['blueprints/main/templates/privacy_policy.html', 'models/messages.py'])

# Create a Jinja environment with the custom loader
env: Environment = Environment(loader=loader)
