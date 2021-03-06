Title: Big Data & Graph Databases
Slug: slides/big_data_and_graph_databases
Template: slide
Theme: night

<div class="slides">
    <section class="" data-id="baf03da378387d4c3aeefe9a4f736179">
        <h1>Big Data, Pathway analysis &amp; Graph Databases</h1>
        <div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;by Sandeep Shantharam</div>
    </section>
    <section class="" data-id="c6e65839dc0f5c8b56931896ee5b7aa7">
        <h3>What is BigData ? How Big is Big ?</h3>
        <hr>
        <div>“Big data is a term describing the storage and analysis of large and or complex data sets using a series of techniques including, but not limited to: NoSQL, MapReduce and machine learning.” [1]
        </div>
        <div>According to&nbsp;Michael Stonebraker (MIT, Works on VoltDB);</div>
        <div>
            <ol>
                <li>Big Volume</li>
                <li>Big Velocity</li>
                <li>Big Variety</li>
            </ol>
        </div>
        <br/>
        <div> According to Google BigQuery, Big Data Means 500 Million Rows.</div>
        <hr>
        <div>[1]Undefined By Data: A Survey of Big Data Definitions -&nbsp;
            <a href="http://arxiv.org/pdf/1309.5821v1.pdf">http://arxiv.org/pdf/1309.5821v1.pdf</a>
        </div>
    </section>
    <section class="" data-id="460ae81959d21ef33ad24771ffe8e9a2">
        <h2>BigData and Bioinformatics;</h2>
        <div>
            <img height="500" src="http://www.genome.gov/images/content/cost_per_megabase.jpg" />
            <br/>
        </div>
        <p>
            <font style="font-size: 24px;">Bigdata in Bioinformatics is not the same as other fields</font>.
        </p>
        <div style="text-align: center;">
            <font style="font-size: 18px;">[2] Cost Per Raw MegaBase of DNA Sequence Graph -&nbsp;</font>
            <a href="http://www.genome.gov/sequencingcosts/">
                <font style="font-size: 18px;">http://www.genome.gov/sequencingcosts/</font>
                <br/>
            </a>
        </div>
    </section>
    <section class="" data-id="f431a6229076b53a876355225a1213e4">
        <h3>Is Bioinformatics really BigData ?</h3>
        <font style="font-size: 98px;">Yes</font>
        <div>
            <ul>
                <li>
                    <font style="font-size: 16px;">
                        <font>
                            <span style="font-size: 16.329307556152344px; font-style: normal; font-variant: normal;">[ June 2013]&nbsp;</span>Major grant funds UCSC researchers using big data to predict cancer outcomes -&nbsp;
                            <a href="http://news.ucsc.edu/2013/06/cancer-big-data.html">http://news.ucsc.edu/2013/06/cancer-big-data.html</a>&nbsp;
                        </font>
                    </font>
                </li>
                <li>
                    <font style="font-size: 16px;">
                        <font>
                            <span style="font-size: 16.329307556152344px; font-style: normal; font-variant: normal;">&nbsp;[March 2013]&nbsp;</span>With $6.25M In Tow, Bina Technologies Wants To Bring Big Data Insight To Genomic Sequencing -&nbsp;
                            <a href="http://techcrunch.com/2013/03/25/with-6-5m-in-tow-bina-technologies-wants-to-bring-big-data-insight-to-genomic-sequencing/">http://techcrunch.com/2013/03/25/with-6-5m-in-tow-bina-technologies-wants-to-bring-big-data-insight-to-genomic-sequencing/</a>
                            <br/>
                        </font>
                    </font>
                </li>
                <li>
                    <font style="font-size: 16px;">
                        <font>
                            <span style="font-size: 16.329307556152344px; font-style: normal; font-variant: normal;">[March 2013]&nbsp;</span>Big data bioinformatics startup Spiral Genetics raises $3M -&nbsp;
                            <a href="http://techcrunch.com/2013/03/25/with-6-5m-in-tow-bina-technologies-wants-to-bring-big-data-insight-to-genomic-sequencing/">http://techcrunch.com/2013/03/25/with-6-5m-in-tow-bina-technologies-wants-to-bring-big-data-insight-to-genomic-sequencing/</a>&nbsp;
                            <br/>
                        </font>
                    </font>
                </li>
                <li>
                    <font style="font-size: 16px;">
                        <span style="font-size: 16.329307556152344px; font-style: normal; font-variant: normal;">[July 2012]&nbsp;</span>Cloudera Chief Scientist Teams With Mount Sinai School of Medicine to Solve Medical Challenges Using Big Data -&nbsp;
                        <a href="http://www.cloudera.com/content/cloudera/en/about/press-center/press-releases/release.html?ReleaseID=1747809">http://www.cloudera.com/content/cloudera/en/about/press-center/press-releases/release.html?ReleaseID=1747809</a>&nbsp;
                    </font>
                </li>
            </ul>
        </div>
    </section>
    <section class="" data-id="23c9427b000424bd4942c21d6951f1b5">
        <h2>Big Data + Bio-Informatics</h2>
        <div>Big Data will not be about Sequencing Genomes and Proteins.</div>
        <div>
            <ul>
                <li>
                    <span>Software tools adapted to biological needs.</span>
                    <br/>
                </li>
                <li>Databases that suit biological data.</li>
                <li>Collaboration between various groups.</li>
            </ul>
        </div>
        <hr>
        <div>
            Advantages at IUPUI -&nbsp;</div>
        <div>
            <ol>
                <li>BigData processing Computation.</li>
                <li>File Storage systems scaling to Petabytes.</li>
                <li>Biological Patient Data.*</li>
                <li>Semantic Approach to Data.</li>
            </ol>
            <div style="text-align: left;">
                <span style="font-size: 18px;">[3]&nbsp;Gene-analysis firms reach for the cloud -&nbsp;</span>
                <a href="http://www.nature.com/news/gene-analysis-firms-reach-for-the-cloud-1.12634" style="font-size: 18px; text-align: center;">http://www.nature.com/news/gene-analysis-firms-reach-for-the-cloud-1.12634</a>
                <br/>
            </div>
        </div>
    </section>
    <section class="" data-id="cee8a58e87e8f1ab5c2c4e00f5dcd312">
        <h2>Pathway Analysis</h2>
        <div>
            <img height="300" src="https://s3.amazonaws.com/media-p.slid.es/uploads/machbio/images/111756/pathway_analysis.png" />
        </div>
        <div>
            <font style="font-size: 18px;">
                [4] Introduction to Pathway Analysis &nbsp;
                <a href="http://bioinformatics.mdanderson.org/MicroarrayCourse/Lectures09/Pathway%20Analysis.pdf">http://bioinformatics.mdanderson.org/MicroarrayCourse/Lectures09/Pathway%20Analysis.pdf
</a>
            </font>
        </div>
    </section>
    <section class="" data-id="8d45ee80520480c9242a06d97899d006">
        <h2>Tools in Pathway Analysis</h2>
        <div>Pathway tools with Functional discovery[6] -&nbsp;</div>
        <div>
            <ol>
                <li>First Generation: Over-Representation Analysis (ORA) tools
                    <br/>
                </li>
                <li>Second Generation: Functional Class Scoring (FCS) tools
                    <br/>
                </li>
                <li>Third Generation: Pathway Topology (PT) tools
                    <br/>
                </li>
            </ol>
        </div>
        <hr />
        <div>Pathway tools with Data Integration -</div>
        <div>
            <ol>
                <li>WikiPathways (www. wikipathways.org)</li>
                <li>MetaCore (www.genego.com)</li>
                <li>Pathview (http://pathview.r-forge.r-project.org/)
                    <br/>
                </li>
            </ol>
        </div>

        <div>
            <font style="font-size: 18px;"> [6]Khatri P, Sirota M, Butte AJ (2012) Ten Years of Pathway Analysis: Current Approaches and Outstanding Challenges. PLoS Comput Biol 8(2): e1002375. doi:10.1371/journal.pcbi.1002375</font>
        </div>
    </section>
    <section class="" data-id="ef1d81693bf481de17511f3600d75d33">
        <h2>Biological Pathway Building Process</h2>
        <div>
            <img height="300" src="https://s3.amazonaws.com/media-p.slid.es/uploads/machbio/images/111789/pathway_building_process.png" />
        </div>
        <div>
            <font style="font-size: 18px;">[7] Viswanathan GA, Seto J, Patil S, Nudelman G, Sealfon SC (2008) Getting started in biological pathway construction and analysis. PLoS Comput Biol 4(2): e16. doi:10.1371/journal.pcbi.0040016
                <br/>
            </font>
        </div>
        <div>
            <br/>
        </div>
    </section>
    <section class="" data-id="7e80797408fb769c5e74583514e015bb">
        <h2>Challenges in Pathway Analysis</h2>
        <h3>Annotation Challenges -</h3>
        <div>Low resolution knowledge bases
            <br/>
        </div>
        <div>Incomplete and inaccurate annotations
            <br/>
        </div>
        <div>Missing condition- and cell-specific information.
            <br/>
        </div>
        <br/>
        <h3>Methodological Challenges -&nbsp;</h3>
        <div>Benchmark data sets for comparing different methods
            <br/>
        </div>
        <div>Inability to model and analyze dynamic response
            <br/>
        </div>
        <div>Inability to model effects of an external stimuli
            <br/>
        </div>
    </section>
    <section class="" data-id="a598546bc31b86e63364e622dc962bb4">
        <h3>Computing Issues in Bioinformatics</h3>
        <div>
            <ul>
                <li style="text-align: left;">
                    <span>
                                    <b>Computation</b>
                                </span>
                    <br/>
                </li>
                <ul>
                    <li style="text-align: left;">
                        <span>algorithms, analysis, simulation, etc.
                                        <br/>
                                    </span>
                    </li>
                </ul>
                <li style="text-align: left;">
                    <span>
                                    <b>Visualization</b>
                                </span>
                    <br/>
                </li>
                <ul>
                    <li style="text-align: left;">
                        <span>seeing all of the data
                                        <br/>
                                    </span>
                    </li>
                </ul>
                <li style="text-align: left;">
                    <span>
                                    <b>Data management</b>
                                </span>
                    <br/>
                </li>
                <ul>
                    <li style="text-align: left;">
                        <span>storing and manipulating all of the data
                                        <br/>
                                    </span>
                    </li>
                </ul>
            </ul>
        </div>
    </section>
    <section class="" data-id="26d7021b90a80d49b90c8397ca8c25e5">
        <h3>Databases Tools in BioInformatics</h3>
        <div>Databases Publications in Bioinformatics [8]</div>
            <img src="http://nar.oxfordjournals.org/content/early/2011/12/01/nar.gkr1099/F1.large.jpg" />
        <div>Database Categories in Bioinformatics;</div>
        <div>
            <ol>
                <li>SQL Databases like MySQL, Oracle</li>
                <li>NoSQL Databases like MongoDb, RDF Datastore and Neo4J</li>
            </ol>
        </div>
        <div style="text-align: left;">
            <font style="font-size: 18px;">[8]&nbsp;MetaBase—the wiki-database of biological databases -
                <a href="http://nar.oxfordjournals.org/content/40/D1/D1250">http://nar.oxfordjournals.org/content/40/D1/D1250</a>
            </font>
        </div>
        <div></div>
    </section>
    <section class="" data-id="cb544b7031dcd843139d94f9427acc11">
        <h3>Graph Databases</h3>
        <div style="text-align: center;">NoSQL Databases that&nbsp;uses graph structures with nodes, edges, and properties to represent and store data.</div>
        <div style="text-align: center;">
            <b>
                            <u>No Index Lookups, Scale Free, &nbsp;No Schema</u>
                        </b>
        </div>
        <div style="text-align: center;">
            <img height="300" src="http://upload.wikimedia.org/wikipedia/commons/3/3a/GraphDatabase_PropertyGraph.png" />
        </div>
        <div style="text-align: center;">
            <font style="font-size: 18px;">
                [9] Graph Databases Book -&nbsp;
                <a href="http://graphdatabases.com/">http://graphdatabases.com/</a>
            </font>
        </div>
    </section>
    <section class="" data-transition="zoom" data-id="a9ce453b3339d844a59ca1e03b9a4ba6">
        <h2>Neo4J</h2>
        <div>True Graph Database that does not limit the number to triples like Triplestore.</div>
        <div class="absolute-element" style="position: absolute; width: 290px; height: 400px; z-index: 4; left: 593px; top: 205px;">
            <img src="http://assets.neo4j.org/img/neo4j/visually_refcard.gif" />
        </div>
        <div class="absolute-element" style="position: absolute; width: 489px; height: 467.41450706156587px; z-index: 4; left: 4px; top: 205px; max-height: none; max-width: none;">Neo4j stores data in nodes connected by directed, typed relationships with properties on both, also known as a Property Graph.</div>
        <div class="absolute-element" style="position: absolute; width: 487px; height: 279.42287124640063px; z-index: 4; left: 14px; top: 404px; max-height: none; max-width: none;">NEO4J is opensource and contains lot of tool interfaces to program in due to the community</div>
        <div class="absolute-element" style="position: absolute; width: 487px; height: 279.42287124640063px; z-index: 4; left: 5px; top: 612px; max-height: none; max-width: none;">
            <a href="http://www.neo4j.org/learn/neo4j">http://www.neo4j.org/learn/neo4j</a>
        </div>
    </section>
    <section class="" data-id="a273d44f29ed619598cb8e9325db1dc5">
        <h2>Neo4J - Hype or Real;</h2>
        <div>
            <b>
                            <font style="font-size: 24px;">Dump Now, Connect Later.</font>
                        </b>
        </div>
        <div>
            <b>
                            <font style="font-size: 24px;">Multiple Node Clusters.</font>
                        </b>
        </div>
        <div>
            <b>
                            <font style="font-size: 24px;">Billions of Nodes (90% of Cases).</font>
                        </b>
        </div>
        <div>
            <b>
                            <font style="font-size: 24px;">Nodes and Relationships have Properties.</font>
                        </b>
        </div>
        <div>
            <b>
                            <font style="font-size: 24px;">REST Api Interface with tools in all programming languages.</font>
                        </b>
        </div>
        <div>
            <font style="font-size: 24px;">
                <b>Natural language Processing Style Query language.</b>
            </font>
        </div>
        <div>
            <div>
                <ul>
                    <li>
                        <font style="font-size: 18px;">
                            <span style="text-align: center;">Topple the stacks of records in a Relational Database while keeping all the relationships, and you’ll see a graph. Where an RDBMS is optimized for aggregated data, Neo4j is optimized for highly connected data.</span>
                            <br/>
                        </font>
                    </li>
                    <li>
                        <font style="font-size: 18px;">
                            <span style="text-align: center;">A Key-Value model is great for lookups of simple or even complex values. When the values are themselves interconnected, you’ve got a graph. Neo4j lets you traverse quickly among all the connected values</span>
                            <br/>
                        </font>
                    </li>
                    <li>
                        <span style="text-align: center;">
                                        <font style="font-size: 18px;">The container hierarchy of a Document Database accommodates nice, schema-free data that can easily be represented as a tree. Which is of course a graph. Refer to other documents (or document elements) within that tree and you have a more expressive representation of the same data that you can easily navigate with Neo4j.[10]</font>
                                    </span>
                        <br/>
                    </li>
                </ul>
                <div>
                    <span style="font-size: 17.551074981689453px;">[10] Neo4J Data Models -&nbsp;</span>
                    <font style="font-size: 14px;">
                        <a href="http://www.neo4j.org/learn/nosql">http://www.neo4j.org/learn/nosql</a>
                    </font>
                    <br/>
                </div>
            </div>
        </div>
        <div>
            <font style="font-size: 12px;">**Markov Chain in Neo4j -
                <a href="http://nicolemargaretwhite.blogspot.com/2013/10/markov-chains-in-neo4j.html">http://nicolemargaretwhite.blogspot.com/2013/10/markov-chains-in-neo4j.html</a>
            </font>
        </div>
    </section>
    <section class="" data-id="a2850b350d1de0db31cec8fa262bf588">
        <h2>Cypher v/s SQL</h2>
        <div>
            <u>Joins in Sql and Cypher</u>
        </div>
        <div>
            <div>
                <pre><code>SELECT bar.*
FROM foo&nbsp;
JOIN bar ON foo.id = bar.foo_id
WHERE foo.id = 101 </code></pre>
            </div>
            <div>
                <pre><code>START foo=node(101)
MATCH foo--&gt;bar
RETURN bar </code></pre>
            </div>
            <div>
                <pre><code>SELECT bar.*, foo_bar.*
FROM foo&nbsp;
&nbsp; JOIN foo_bar ON foo.id = foo_bar.foo_id&nbsp;
&nbsp; JOIN bar ON foo_bar.bar_id = bar.id
WHERE foo.id = 1 </code></pre>
            </div>
            <div>
                <pre><code>START foo=node(1)
MATCH foo-[foo_bar]-&gt;bar
RETURN bar, foo_bar </code></pre>
            </div>
        </div>
        <div>
            <font style="font-size: 18px;">[11]
                <a href="http://systay.github.io/blog/2011/11/06/cypher---a-view-from-a-recovering-sql-dba/">http://systay.github.io/blog/2011/11/06/cypher---a-view-from-a-recovering-sql-dba/</a>
            </font>
        </div>
        <div>
            <font style="font-size: 18px;">[12]
                <a href="http://stackoverflow.com/questions/6873772/sql-postgres-shortest-path-in-graph-recursion/6900257#6900257">http://stackoverflow.com/questions/6873772/sql-postgres-shortest-path-in-graph-recursion/6900257#6900257</a>
            </font>
        </div>
        <div>
            <pre><code> yfiyfit</code></pre>
        </div>
    </section>
    <section class="" data-id="9dd078388f9b56f32945f47d5ed4fa3b">
        <h2>Cypher v/s SPARQL</h2>
        <div>Sparql is designed for data models with Namespace Identifiers and each property are treated as nodes.</div>
        <div>Sparql Queries are built for triplestores, like&nbsp;for triples being a data entity composed of subject-predicate-object, like "Protein A activates Gene X" or "Compound L inhibits Gene Z".</div>
        <div>
            <br/>
        </div>
        <h3>
                        <b>
                            <u>Cypher is just different.</u>
                        </b>
                    </h3>
        <div>
            <br/>
        </div>
        <div>SPARQL example in Chem2Bio2RDF -&nbsp;
            <a href="http://cheminfov.informatics.indiana.edu:8080/bindingdb/snorql/">http://cheminfov.informatics.indiana.edu:8080/bindingdb/snorql/</a>
        </div>
        <div>
            <font style="font-size: 18px;">
                <br/>
            </font>
        </div>
        <div>
            <font style="font-size: 18px;">[13] Learn More about Cypher -&nbsp;
                <a href="http://www.slideshare.net/maxdemarzi/cypher-12154713">http://www.slideshare.net/maxdemarzi/cypher-12154713</a>
            </font>
        </div>
    </section>
   
    <section class="" data-id="55fa2b1cbe1c8c3e490f91f50160f86f">
        <h2>Current Research in Graph</h2>
        <div>
            <br/>
        </div>
        <div>
            Bio4j is a bioinformatics graph based DB including most data available in UniProt KB (SwissProt + Trembl), Gene Ontology (GO), UniRef (50,90,100), RefSeq, NCBI taxonomy, and Expasy Enzyme DB -&nbsp;
            <a href="http://www.slideshare.net/pablo_pareja/graph-db-bioinformatics-bio4j-recent-applications-and-future-directions">http://www.slideshare.net/pablo_pareja/graph-db-bioinformatics-bio4j-recent-applications-and-future-directions</a>
        </div>
        <div>
            <br/>
        </div>
        <div>CS team in University of California - Santa Barbara -&nbsp;
            <a href="http://www.cs.ucsb.edu/~dbl/index.php">http://www.cs.ucsb.edu/~dbl/index.php</a>
        </div>
        <div>
            <br/>
        </div>
        <div>Stanford Statistics team worked on Graph theory for Immunology -&nbsp;
            <a href="http://www-stat.stanford.edu/~susan/papers/path3.pdf">http://www-stat.stanford.edu/~susan/papers/path3.pdf</a>&nbsp;/&nbsp;
            <a href="http://www2.research.att.com/~volinsky/Graphs/slides/holmes.pdf">http://www2.research.att.com/~volinsky/Graphs/slides/holmes.pdf</a>
        </div>
    </section>
    <section class="" data-id="378d1dca65070708d15695649bc70cac">
        <h2>Disadvantages of Neo4J;</h2>
        <div>
            <br/>
        </div>
        <div>
            <ul>
                <li style="text-align: justify; ">
                    <font style="font-size: 42px;">Not much standard tools available compared to SQL based Databases.
                        <br/>
                    </font>
                </li>
                <li style="text-align: justify; ">
                    <font style="font-size: 42px;">
                        <span>Limit of Nodes, Relationships and Relationship types at 34 Billion.</span>
                        <br/>
                    </font>
                </li>
                <li style="text-align: justify; ">
                    <font style="font-size: 42px;">
                        <span>Data Cluster replication cannot be done.</span>
                        <br/>
                    </font>
                </li>
                <li style="text-align: justify; ">
                    <span>
                                    <font style="font-size: 42px;">Data reliability needs to be tested as its a new database.</font>
                                </span>
                    <br/>
                </li>
            </ul>
            <div style="text-align: left;">
                <br/>
            </div>
        </div>
    </section>
    <section class="" data-id="b3c3cbbcd1896b3856214f8a2c6f322f">
        <h2>Bigdata + Pathways + Graphs = ?</h2>
        <div>
            <br/>
        </div>
        <div>
            <br/>
        </div>
    </section>
    <section class="" data-id="b11fa2659411237a1fddc5d8ad223aa0">
        <h2>Integration into Lab</h2>
        <div>
            <br/>
        </div>
        <div>Substituting Neo4J for RDF Triplestore in Integrative Biology -&nbsp;
            <a href="http://bib.oxfordjournals.org/content/14/1/109.full">http://bib.oxfordjournals.org/content/14/1/109.full</a>
        </div>
        <div>
            <br/>
        </div>
        <div>Import Data from various databases of Lab like PAGED, HAPPI into Neo4j.</div>
        <div>
            <br/>
        </div>
        <div>Build Visualization tools for data in Neo4j and form meaningful discoveries by Pathway analysis.</div>
    </section>
    <section class="" data-id="d4319842c58a42f81b9b5bf5e2ec5104">&nbsp;
        <h1>Questions ???</h1>
    </section>
    <section class="" data-id="1734be10314de367529684ae0fafc602">
        <h2>Thank you...and Links</h2>
        <div>
            <br/>
        </div>
        <div>
            <p></p>
            <ul>
                <li>Neo4J Database -&nbsp;
                    <a href="http://www.neo4j.org/">http://www.neo4j.org/</a>
                </li>
                <li>Bio2RDF -&nbsp;
                    <a href="http://bio2rdf.org/">http://bio2rdf.org/</a>
                </li>
                <li>Chem2Bio2RDf -&nbsp;
                    <a href="http://cheminfov.informatics.indiana.edu:8080/">http://cheminfov.informatics.indiana.edu:8080/</a>
                </li>
                <li>Bio4j -&nbsp;
                    <a href="http://bio4j.com/">http://bio4j.com/</a>
                </li>
            </ul>
            <p></p>
        </div>
        <div></div>
    </section>
</div>
