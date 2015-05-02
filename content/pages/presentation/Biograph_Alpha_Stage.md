Title: BioGraph in Alpha Stage
Slug: slides/biograph_alpha_stage
Template: slide
Theme: beige

<div class="slides">
    <section>
        <h1>Biograph</h1>
        <p>Drug Repositioning Application</p>
        <p>By Sandeep Shantharam</p>
    </section>
    <section>
        <h2>Introduction</h2>
        <p>Biograph is an application being built for Drug-Repositioning:</p>
        <ul>
            <li>Frontend Interface for MURI team <strong>"curation"</strong>.</li>
            <li>Backend application with ElasticSearch for searching <strong>"entities"</strong>
            </li>
            <li>Backend application with Graph Database (Neo4j) for mapping the <strong>"relationship"</strong>
            </li>
            <li>
                <strong>Data analytics</strong> platform for performing analysis on the datastore of Biograph.</li>
            <li>Backend Application is a REST API endpoints and the Frontend Applicaiton will be an Angular Framework.</li>
        </ul>
    </section>
    <section>
        <section>
            <h2>Problem - Data Integration </h2>
            <ul>
                <li>Entities in the application meaning - "gene", "protein", "chemical", "pathway" and "diseases".</li>
                <li>The problem with most of the biological databases, is the lack of quality or quantity of these entities.</li>
                <li>The Biograph application plans to solve this by integrating these databases.</li>
                <li>In the Data integration, the inclusion and exclusion of the entities will result in quality of the final datastore.</li>
            </ul>
        </section>
        <section>
            <h2>Solution - ElasticSearch</h2>
            <ul>
                <li>ElasticSearch is a database that can be used to unify the entities and further streamline our process in eliminating the duplication of entities.</li>
                <li>The ElasticSearch is important for curation purposes.</li>
                <li>ElasticSearch will increase the rate at which the curation is done and also eliminate duplication in relationships.</li>
                <li>The backend could be further used for text-analysis and automatic curation in the future.</li>
            </ul>
        </section>
        <section>
            <h1><span style="font-size:48px">Schema - ElasticSearch</span></h1>
            <pre><code>
{"index": {"_index": "ctdbio", "_type": "string"}} 
## ["chemical","gene","protein","pathway","disease"]
        </code></pre>
            <pre><code>{
  "bid": bid,       ## Primary Unique Number that will represent the type
  "type": "string", ## ["chemical","gene","protein","pathway","disease"]
  "name": name,
  "primary": {dictionary},
  "secondary": synonymns, ## List of Synonymns
  "tag": [list],              ## Tag for the entity
  "text": "string"        ## Text that is relevant to the Entity
}</code></pre>
        </section>
        <section>
            <span style="font-size:48px">Schema - Chemical</span>
            <pre><code>sc_line = {
   "bid": bid,
   "type": "chemical",
   "name": name,
   "primary": {"drugbank": drugbank, "cas": cas},
   "secondary": synonymns,
   "tag": [],
   "text": chemtext
   }</code></pre>
            <span style="font-size:48px">Schema - Gene</span>
            <pre><code>sc_line = {
    "bid": bid,
    "type": "gene",
    "name": name,
    "primary": {"biogrid": biogrid, "pharmagkb": pharmagkb, 
    "uniprotid": uniprotid, "gene_symbol": gen_sym, "alt_gene_ids": alt_gene},
    "secondary": synonymns,
    "tag": [],
    "text":  ""       
  }</code></pre>
        </section>
        <section>
            <span style="font-size:48px">Schema - Disease</span>
            <pre><code>sc_line = {
   "bid": bid,
   "type": "disease",
   "name": name,
   "primary": {"alt_dis": alt_dis, "medic_terms": medic},
   "secondary": synonymns,
   "tag": [],
   "text": distext
 }</code></pre>
            <span style="font-size:48px">Schema - Pathway</span>
            <pre><code>sc_line = {
   "bid": bid,
   "type": "pathway",
   "name": name,
   "primary": {},
   "secondary": [],
   "tag": [],
   "text": ""
}</code></pre>
        </section>
    </section>
    <section>
        <section>
            <h2>Problem - Graph Datastore</h2>
            <ul>
                <li>Entities in the graph datastore are the same - "gene", "protein", "chemical", "pathway" and "diseases".</li>
                <li>The biological databases just try to map a single relationship between entities.</li>
                <li>The Biograph application plans to solve this by able to map relation across different entities with path information.</li>
                <li>In building the datastore, the quality of the database will depend on the expressiveness of the queries and the usefulness of the query to the biologists.</li>
            </ul>
        </section>
        <section>
            <h2>Solution - Neo4j</h2>
            <ul>
                <li>Neo4j is a database that will be used to store the data in a network format or graph format.</li>
                <li>The Neo4j will be important as it can do some of the data analytic's like node degree and path identification easy for the application.</li>
                <li>Neo4j will help in storing the relationship created by the curators.</li>
            </ul>
        </section>
        <section>
            <h2>Schema - Ne04j</h2>
            <pre><code>{  
  "table":{  
    "_response":{  
      "columns":[  
        "r"
      ],
      "data":[  
        {  
          "row":[  
            {  
              "name":"DNA segment, 03B03F (Research Genetics)",
              "bid":"27777"
            }
          ],
          "graph":{  
            "nodes":[  
              {  
                "id":"155926",
                "labels":[  
                  "gene"
                ],
                "properties":{  
                  "name":"DNA segment, 03B03F (Research Genetics)",
                  "bid":"27777"
                }
              }
            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            {  
              "name":"DNA segment, 03B03R (Research Genetics)",
              "bid":"27778"
            }
          ],
          "graph":{  
            "nodes":[  
              {  
                "id":"155927",
                "labels":[  
                  "gene"
                ],
                "properties":{  
                  "name":"DNA segment, 03B03R (Research Genetics)",
                  "bid":"27778"
                }
              }
            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            {  
              "name":"DNA segment, 03.MMHAP34FRA.seq",
              "bid":"53288"
            }
          ],
          "graph":{  
            "nodes":[  
              {  
                "id":"155928",
                "labels":[  
                  "gene"
                ],
                "properties":{  
                  "name":"DNA segment, 03.MMHAP34FRA.seq",
                  "bid":"53288"
                }
              }
            ],
            "relationships":[  

            ]
          }
        }
      ],
      "stats":{  
        "contains_updates":false,
        "nodes_created":0,
        "nodes_deleted":0,
        "properties_set":0,
        "relationships_created":0,
        "relationship_deleted":0,
        "labels_added":0,
        "labels_removed":0,
        "indexes_added":0,
        "indexes_removed":0,
        "constraints_added":0,
        "constraints_removed":0
      }
    },
    "nodes":[  
      {  
        "id":"155926",
        "labels":[  
          "gene"
        ],
        "properties":{  
          "name":"DNA segment, 03B03F (Research Genetics)",
          "bid":"27777"
        }
      },
      {  
        "id":"155927",
        "labels":[  
          "gene"
        ],
        "properties":{  
          "name":"DNA segment, 03B03R (Research Genetics)",
          "bid":"27778"
        }
      },
      {  
        "id":"155928",
        "labels":[  
          "gene"
        ],
        "properties":{  
          "name":"DNA segment, 03.MMHAP34FRA.seq",
          "bid":"53288"
        }
      }
    ],
    "other":[  

    ],
    "relationships":[  

    ],
    "size":3,
    "stats":{  
      "contains_updates":false,
      "nodes_created":0,
      "nodes_deleted":0,
      "properties_set":0,
      "relationships_created":0,
      "relationship_deleted":0,
      "labels_added":0,
      "labels_removed":0,
      "indexes_added":0,
      "indexes_removed":0,
      "constraints_added":0,
      "constraints_removed":0
    }
  },
  "graph":{  
    "nodeMap":{  
      "155926":{  
        "name":"DNA segment, 03B03F (Research Genetics)",
        "bid":"27777"
      },
      "155927":{  
        "name":"DNA segment, 03B03R (Research Genetics)",
        "bid":"27778"
      },
      "155928":{  
        "name":"DNA segment, 03.MMHAP34FRA.seq",
        "bid":"53288"
      }
    },
    "relationshipMap":{  

    }
  }
}</code></pre>
        </section>
        <section>
            <h2>Schema - labels</h2>
            <pre><code>{  
  "table":{  
    "_response":{  
      "columns":[  
        "labels(n)",
        "type(r)"
      ],
      "data":[  
        {  
          "row":[  
            [  
              "disease"
            ],
            "chemical_disease"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "gene"
            ],
            "chemical_gene"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "pathway"
            ],
            "chemical_pathway"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "chemical"
            ],
            "chemical_gene"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "disease"
            ],
            "gene_disease"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "pathway"
            ],
            "gene_pathway"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "chemical"
            ],
            "chemical_disease"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "pathway"
            ],
            "disease_pathway"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "gene"
            ],
            "gene_disease"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "chemical"
            ],
            "chemical_pathway"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "disease"
            ],
            "disease_pathway"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        },
        {  
          "row":[  
            [  
              "gene"
            ],
            "gene_pathway"
          ],
          "graph":{  
            "nodes":[  

            ],
            "relationships":[  

            ]
          }
        }
      ],
      "stats":{  
        "contains_updates":false,
        "nodes_created":0,
        "nodes_deleted":0,
        "properties_set":0,
        "relationships_created":0,
        "relationship_deleted":0,
        "labels_added":0,
        "labels_removed":0,
        "indexes_added":0,
        "indexes_removed":0,
        "constraints_added":0,
        "constraints_removed":0
      }
    },
    "nodes":[  

    ],
    "other":[  

    ],
    "relationships":[  

    ],
    "size":12,
    "stats":{  
      "contains_updates":false,
      "nodes_created":0,
      "nodes_deleted":0,
      "properties_set":0,
      "relationships_created":0,
      "relationship_deleted":0,
      "labels_added":0,
      "labels_removed":0,
      "indexes_added":0,
      "indexes_removed":0,
      "constraints_added":0,
      "constraints_removed":0
    }
  },
  "graph":{  
    "nodeMap":{  

    },
    "relationshipMap":{  

    }
  }
}</code></pre>
        </section>
    </section>
    <section>
        <img src="https://s3.amazonaws.com/media-p.slid.es/uploads/machbio/images/1021452/Biograph.png" style="visibility: visible;" data-natural-width="692" data-natural-height="594">
    </section>
    <section>
        <h2>Challenges</h2>
        <ul>
            <li>Data Integration - need database parsing in the format the schema entails.</li>
            <li>Graph Datastore - the quality of the relation and the scoring the relationship edges.</li>
            <li>Frontend - the intuitiveness of the interface will enable the curators to contribute towards building the database.</li>
            <li>Quality evaluation - Quality parameters for the curators.</li>
        </ul>
    </section>
    <section>
        <h2>Thank you.. Any Questions ???</h2>
    </section>
</div>

