import requests
import json

# Replace with your API key
api_key = "96566c203d6cee20bf9b6612305c2ed8"

# Example DOI
doi = '10.1016/j.indmarman.2021.11.001'  # Replace with the DOI of the paper

# Headers for the request
headers = {
    'X-ELS-APIKey': api_key,
    'Accept': 'application/json'
}

# Abstract Retrieval API URL using DOI
abstract_url = f'https://api.elsevier.com/content/abstract/doi/{doi}'

# Make the request for the abstract
abstract_response = requests.get(abstract_url, headers=headers)
abstract_data = abstract_response.json()

#print(json.dumps(abstract_data, indent=4))


# Extract title and Scopus ID (needed for citation overview)
title = abstract_data['abstracts-retrieval-response']['coredata']['dc:title']
scopus_id = abstract_data['abstracts-retrieval-response']['coredata']['dc:identifier'].split(':')[1]
eid = abstract_data['abstracts-retrieval-response']['coredata']['eid']

print(f"Title: {title}")
print(f"Scopus ID: {scopus_id}")
print(f"EID: {eid}")
print(scopus_id)
# Citation Overview API URL
# references_url = f'https://api.elsevier.com/content/abstract/scopus_id/{85118991788}?field=references'

references_url = f'https://api.elsevier.com/content/abstract/EID:{eid}?apiKey={api_key}&view=REF'

# Make the request for the abstract and references
abstract_response = requests.get(references_url, headers=headers)

# Check if the request was successful
if abstract_response.status_code == 200:
    abstract_data = abstract_response.json()

    # Extract references
    references = abstract_data.get('abstracts-retrieval-response', {}).get('references', {}).get('reference', [])

    # Print each reference
    print("\nReferences:")
    for ref in references:
        # Reference details can vary, so you might need to adjust the fields you access
        ref_info = ref.get('ref-info', {})
        ref_title = ref_info.get('ref-title', {}).get('ref-titletext', '')
else:
    print(f"Error with status code: {abstract_response.status_code}")

