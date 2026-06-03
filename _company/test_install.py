import googleapiclient.discovery
import requests
import sys

print(f"--- Installation Check ---")
print(f"google-api-python-client imported successfully: {hasattr(sys.modules['googleapiclient'], 'discovery')}")
print(f"requests imported successfully: {hasattr(sys.modules['requests'], 'get')}")
print("--------------------------")