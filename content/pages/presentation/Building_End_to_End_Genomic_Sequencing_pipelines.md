Title: Building End to End Genome Sequencing Pipelines
Slug: slides/build_genomic_sequencing_pipelines
Template: slide
Theme: moon

<div class="slides">
    <section>
    	<section>
	        <h1>Building Computational Workflows/Pipelines</h1>
	        <p>By Sandeep Shantharam</p>
        </section>
        <section>
	        	<p align="left"><strong>Bioinformatics Masters Student from Indiana University</strong></p>
	        	<p align="left">1+ year at Biogen</p>
	        	<p align="left">2+ years at Indiana University</p>
	        	<p align="left">3+ years at Tata Consultancy Services</p>
        </section>
        <section>
        	<h1>Overview</h1>
        	<ul>
        		<li>Building Next Generation Sequencing Pipelines</li>
        		<li>Automating FASTQ file generation</li>
        		<li>Developing application to visualize network data</li>
        		<li>Building Data pipeline for 3D imaging data</li>
        		<li>C Level Performance in Python</li>
        	</ul>
        </section>
    </section>


    <section>  
    	<section>
    	<h3>Building Next Generation Sequencing Pipelines</h3>
      	</section>

      	<section>
      	<h3>Challenges</h3>
      	</section>      	
    	
    	<section>
    		- Pipex is Biogen's answers to Seven Bridges' - it gives complete control of every aspect of running a pipeline.
			- Pipex supports three execution system - Snakemake, Nextflow and ShadowFax(Internal), its a thin wrapper around the execution systems.
			- Pipex has basic requirements from Execution systems to be able to Start, Stop and Log.
			- Pipex supports jobs to be run on Internal Grid Engine.
			- Pipex has been designed to work on Internal HPC Cluster, AWS Cfn Cluster and any Super Computing Facilities.
			- Pipex works by recieving request from SEQR to run jobs , stop jobs and restart jobs.
			- Pipex is Asynchronous tool meaning, you can simulatneously run many Pipelines.
			- Pipex has strict version control system at the Pipeline versioning level, so high regard for reproducing the results.
			- Future goal of Pipex to ease writing new Pipelines and provide flexibility to priortize the Pipeline runs.
			- Pipex though has a single client (SEQR), additional CLI tools could be built to run Pipelines from Command Line.
      	</section>

       	<section>
      	</section>
      	
      	<section>
      	<h2>Evaluation of Workflow Managers</h2>
      	<p>
      	<li>Ability to re-run after failed runs.</li>
      	<li></li>
      	</p>
      	</section>
      	
      	<section>
      	Snakemake
      	</section>
       	<section>
       	Nextflow
      	</section>

      	<section>
      	</section>      	
    </section>
    
    <section>
    	<section>
    	<h3>Automating FastQ file Generation</h3>
      	</section>

      	<section>
      	<h3>Challenges</h3>
      	</section>      	

    	<section>
			- Two Components of BiNGS - FASTQ Processing and Project ID generation.
			- Project ID generation is created based on Issues/Tasks rquested from Computational Biology Group or Sequencing Lab.
			- Project ID is created for data from both Internal and External Projects.
			- Project ID is used in the SampleSheets for Sequencing Machines
			- Project ID is used to Identify the location of FASTQ files and Post-Processed Data from Pipeline Runs
			- Project IDs are generated using a Scheduler at Regular Intervals

			- FASTQ Processing is supported for Hi-Seq Illumina Machines as of now, support both RNA and DNA Sequencing Samples.
			- Based on the completion of dump from the Sequencing Machine and Availablilty of SampleSheet
			- Utilizes the Grid Engine to process the BCL Files into FASTQ files.
			- De-Multiplexing of Samples into Projects and Post-Processing QC metrics are also run on Grid Engine as individual jobs.
			- Updates SEQR about the completion of processing of FASTQ Files - leading to Projects being available for running Pipelines.
			- Future Support for other Sequencing Machines (MiSeQ and NextSeQ).
			- Future Possibility of Integrating with Fulcrum Genomics folks for Run Folder Level QC metrics.
			- FASTQ Processing is triggered based on various conditions and there are manual steps involved.
      	</section>

    	<section>
      	</section>

       	<section>
      	</section>      	

    </section>    

    <section>
	    <section>
	    	<h3>Syllable Mouse Imaging Data</h3>
			<iframe width="853" height="480" src="https://www.youtube.com/embed/Yl6qLbiEA_U?start=49&end=85&rel=0" frameborder="0" allowfullscreen></iframe>
	    </section>
	    <section>
	    	<h3>Requirements</h3>
	    	<p>
	    	<li>Utilize AWS tools to enable ease of moving large amounts of data</li>
	    	<li>Build robust data workflow for an error free processing</li>
	    	<li>Generate multiple type of reports with the Imaging Data</li>
	    	<li>Designing for the Synchronous nature of the Web Application</li>
	    	</p>
	    </section>
	    <section>
	    	<img data-src="/extra/SyllableArc.png">	    	
	    </section>
    </section>    

    <section>
    	<section>
    		<h3>Network Navigator - Visualizing Network Data</h3>
    		<img data-src="/extra/netex.gif">
    	</section>
    	<section>
    		<h3>Requirements</h3>
    		<p>
	    		<li>Ability to Visualize Large Networks - scaling on Nodes, Attributes and Edges.</li>
	    		<li>Abilty to Filter, Search on different attributes. </li>
	    		<li>Perform Enrichment based on the different attributes.</li>
	    		<li>Loading Internal and External data with regular updates.</li>
    		</p>
    	</section>
    	<section>
    		<img data-src="/extra/NetExplo.png">
    	</section>
    </section>

    <section>
	    <section>
	    	<h3>C Level Performance in Python</h3>
	    	<li>Rules/Process in NGS Pipelines</li>
	    	<li>Enrichment Calculation in Network Navigator</li>
	    </section>
	    <section>
	    	<h3>Pairwise Distance Function</h3>
	    	<p>will take an array representing M points in N dimensions, and return the M x M matrix of pairwise distances</p>
	    	from <a href="https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/">Numba vs. Cython: Take 2</a>
	    	<pre>
	    		<code>
	    			import numpy as np
					X = np.random.random((10000, 3))
	    		</code>
	    	</pre>
	    </section>
	    <section>
	    	<h3>Pure Python Implementation</h3>
	    	<img src="/extra/Python.png" />
	    </section>
	   	<section>
	    	<h3>Cython Implementation</h3>
	    	<img src="/extra/Cython.png" />
	    	<li>Speedup of Approximately 637.2x over Pure Python Implementation</li>	
	    </section>
	    <section>
	    	<h3>Numba Implementation</h3>
	    	<img src="/extra/Numba.png" />	    	
	    	<li>Speedup of Approximately 900.2x over Pure Python Implementation</li>
	    	<li>Speedup of Approximately 1.4x over Cython Implementation</li>
	    </section>	    
    </section>

	<section>
    	<h1>Acknowledgement</h1>
    		<p>my amazing team at <h2>Biogen</h2> who shall not be named...</p>
    </section>
    <section>
    	<h2>Thank you.. Any Questions ???</h2>
    	<ul style="list-style: none;">
    	<li><i class="fa fa-twitter"> machbio</i></li>
    	<li><i class="fa fa-share-square-o"> <a href="https://machb.io">https://machb.io</a></i></li>
    	</ul>
    </section>
</div>