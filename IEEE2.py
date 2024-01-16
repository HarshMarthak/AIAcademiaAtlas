from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import requests
import json
import pprint
import re


## Load configuration
conFile = open('C:/Users/Fin/OneDrive/Documents/GitHub/AIAcademiaAtlas/config.json')
config = json.load(conFile)
conFile.close()

## Initialize client
client = ElsClient(config['apikey'])

paper_doi = '10.1016/j.indmarman.2021.11.001'

doc = FullDoc(doi = paper_doi)

if doc.read(client):
    print("Document successfully retrieved")
        # Debug: Print a small part of the retrieved data
    print("Printing a snippet of the retrieved document data:")
   # pprint.pprint(doc.data['coredata'] if 'coredata' in doc.data else doc.data)
    #pprint.pprint(doc.data)

    text = json.dumps(doc.data)
    print("\nJSON Data (Snippet):")
    print(text[:500]) 

    # Access the references (if available)
    pattern = r'\w+,\s\w+\.\s\(\d{4}\)\.\s.*?\.\s\w+,\s\d+,\s\d+–\d+\.'
    references = re.findall(pattern, text)
    for i, ref in enumerate(references, start=1):
        print(f"Reference {i}:\n{ref}\n")
else:
    print("References not available in the retrieved document.")






















#     if 'reference' in doc.data:
#         references = doc.data['reference']
#         for ref in references:
#             # Process each reference (exact fields depend on the document's structure)
#             print(ref)
#     else:
#         print("References not available in the retrieved document.")











# if doc.read(client):
#     # The Scopus ID (scp_id) is typically part of the response, extract it here
#     print("Title:", doc.title)
#     ref=doc.data['item']['bibrecord']['tail']['bibliography']['reference']
#     print(ref)
# else:
#     print("Failed to read the document.")

# if doc.read(client):
#     # Extract references if available
#     try:
#         references = doc.data
#         return references
#     except KeyError:
#         return "Unable to find references in the document."
# else:
#     return "Failed to read the document."


# doc = AbsDoc(scp_id = 84872135457)



# if doc.read(client):
#     print("Title:", doc.title)
#     # Extract the EID from the document for the reference request
#     eid = doc.data['coredata']['eid']
#     # Construct the URL for the REF view
#     ref_url = f"https://api.elsevier.com/content/abstract/eid/{eid}?apiKey={config['apikey']}&view=REF"
#     # Make the request for
#     # Make the API request for references
#     response = requests.get(ref_url)
#     if response.status_code == 200:
#         references_data = response.json()

#         print(references_data) # Placeholder for actual reference processing
#     else:
#         print("Failed to fetch references")
# else:
#     print("Failed to read the document.")
