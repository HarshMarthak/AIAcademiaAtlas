# AIAcademiaAtlas
Mapping all the research papers in a field and summarising

Define the Scope:

Each node (paper, institute, topic or author) can be represented as a point, with lines connecting related nodes called edges.

The size of each node can be determined by how many citations/papers/ it has

I think it should be a Citation Network

Nodes: Each paper is a node in the network.

Edges: Create an edge between two nodes if one paper cites another.

Node Size: The size of each node will be proportional to its citation count. Papers with more citations will have larger nodes.

We can set the depth of the network; for example, We give the script a paper and a depth of 1 will map all the papers that the paper we gave it cites. A depth of 2 will cite all of those papers and the papers they cite.

We can choose only to map papers with a threshold number of citations.

If a paper cites another paper more than once, it likely means the paper is more important to that research. This can affect the thickness of the edges.

Data Collection and Data Processing:

Collect data from IEEE Xplore API, arXiv API, springer
arXiv
Content: metadata and article abstracts for the e-prints hosted on arXiv.org
Permissions: no registration is required
Limitations: no more than 4 requests per second

IEEE Xplore
Content: metadata for articles included in IEEE Xplore
Permissions: must be affiliated with an institution that subscribes to IEEE Xplore. Temple is a subscriber.
Limitations: maximum 1,000 results per query

Springer
Content: full-text of SpringerOpen journal content and BioMed Central, as well as metadata from other Springer resources
Permissions: free to access. Request a key at https://dev.springer.com/signup
Limitations: noncommercial use

Elsevier
Content: multiple APIs for full-text books and journals from ScienceDirect and citation data from Engineering Village and Embase
Permissions: free to register; click 'Get API Key" to request a personal key: https://dev.elsevier.com/
Limitations: "Researchers at subscribing academic institutions can text mine subscribed full-text ScienceDirect content via the Elsevier APIs for non-commercial purposes."   
Usage policies depend on use cases; see the list at https://dev.elsevier.com/use_cases.html

https://guides.temple.edu/APIs#:~:text=API%20stands%20for%20application%20programming,in%20a%20machine%2Dreadable%20format. 

