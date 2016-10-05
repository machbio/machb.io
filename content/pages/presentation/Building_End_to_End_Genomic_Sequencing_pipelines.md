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
        		<li>Building NGS Pipeline Framework</li>
        		<li>Automating FASTQ file generation</li>
        		<li>Developing application to visualize network data</li>
        		<li>Building Data pipeline for 3D imaging data</li>
        		<li>C Level Performance in Python</li>
        	</ul>
        </section>
    </section>
    <section>  
    	<section>
    	<h3>Building NGS Pipeline Framework</h3>
    	<strong>Software Infrastructure that can manage execution of NGS Pipelines</strong>
    	<ul align="left">
	    	<li>Pipelines - GATK Variant Calling Pipeline and STAR-RSEM Pipeline</li>
	    	<li>Multiple Genome Annotations across different species</li>
    	</ul>
      	</section>
    	
    	<section>
      	<h3>Challenges</h3>
    	<ul align="left">
      		<li>COTS did not provide API access to their platforms</li>
      		<li>Limited to RNA-Sequencing Pipelines, while DNA-Sequencing Pipeline data was too large</li>
      		<li>Pipeline Versioning</li>
      		<li>OpenSource Solutions has assumptions</li>
      	</ul>
      	</section>

      	<section>
      	<h3>Evaluation of Workflow Managers</h3>
    	<ul align="left">
	      	<li>large active community around the workflow manager</li>
	      	<li>can handle non-linear pipelines</li>
	      	<li>has comprehensive logging system</li>
	      	<li>completely configurable algorithm parameters</li>
	      	<li>re-run after failed runs,from the last successful step</li>
	    </ul>
	  	<u><strong>Snakemake and Nextflow</strong></u>
      	</section>

       	<section>
    		<h3>Pipex</h3>
	    	<ul align="left">
	    		<li>Asynchronous Web Server to handle NGS pipeline</li>
				<li>Supports Snakemake, Nextflow and ShadowFax(Internal), its a thin wrapper around the execution systems</li>
				<li>Works on Internal HPC Cluster, AWS CfnCluster and Super Computing Facilities</li>
				<li>Webapp and Command Line tool to run, stop or restart pipelines</li>
	    	</ul>
      	</section>
      	
      	<section>Pipex Overview Diagram</section>
      	<section>Pipex Simplified DataFlow</section>

      	<section>
      	<h2>Snakemake</h2>
       	<div align="left">
      	<h3>Pros</h3>
	       	<ul align="left">
	       	<li>Large Community of Bioinformaticians</li>
	       	<li>Suited for Large Pipelines</li>
	       	<li>Make based workflow</li>
	       	</ul>      	
      	<h3>Cons</h3>
	       	<ul align="left">
	       	<li>No Docker Support</li>
	       	<li>No Environment Modules</li>
	       	<li>Excellent Cleanup Process</li>
	       	</ul>      	      
       	</div>	
      	</section>
       	<section>
       	<h2>Nextflow</h2>
       	
       	<div align="left">
       	<h3>Pros</h3>
	       	<ul align="left">
	       	<li>Docker Support</li>
	       	<li>Slurm used in Supercomputing facilities</li>
	       	<li>Environment Variables Control</li>
	       	<li>Configuration profiles</li>
	       	<li>Built in Environment Modules Support</li>
	       	</ul>
       	<h3>Cons</h3>
	       	<ul align="left">
	       	<li>Groovy Language Syntax</li>
	       	<li>JVM based memory issues</li>
	       	</ul>       	
       	</div>
      	</section>

      	<section>
      	<h3>Benefits of NGS Pipeline Framework</h3>
      	<div align="left">
	      	<li>Effective Control over every aspect of Pipeline</li>
	      	<li>Large Community of Pipelines</li>
	      	<li>Customize Report generation</li>
	      	<li>Save Money</li>
      	</div>
      	</section>      	
    </section>
    
    <section>
    	<section>
    	<h3>Automating FastQ file Generation</h3>
    	<strong>Processing of sequencer outputs into FASTQ files</strong>
    	<ul align="left">
	    	<li>De-multiplexing of Sample files into specific FASTQ Files</li>
	    	<li>Quality Control metrics at multiple levels - Sample, Run and Device</li>
	    	<li>Support for HiSeq, MiSeq, NextSeq</li>
    	</ul>    	
      	</section>

      	<section>
      	<h3>Challenges</h3>
      	<ul align="left">
      		<li>Automation meant Standardization</li>
      		<li>Internal Project vs External Project</li>
      		<li>Important QC metrics for lab and computational biologists</li>
      		<li>Utilizing Grid Engine Support</li>
      	</ul>
      	</section>      	

       	<section>
    		<h3>BiNGS</h3>
	    	<ul align="left">
	    		<li>Command line application tool for automating primary processing</li>
				<li>Quality Control Tools as part of the steps required</li>
				<li>Adapter Trimming</li>
				<li>Demultiplex and trigger QC pipelines</li>
				<li>Trigger mechanism based on decision tree</li>
				<li>Integrates with the Project Management Tool</li>
	    	</ul>
      	</section>

      	<section>
      		FASTQ processing Overview Diagram
      	</section>

    	<section>
      	<h3>Benefits of Primary Processing Automation</h3>
      	<div align="left">
      		<li>QC metrics helpful and avoids unnecessary downstream processing</li>
      		<li>Metadata leads to end-to-end Pipeline Processing</li>
      		<li>Helping Lab folks to identify issues</li>
      	</div>
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
	    		<li>Ability to Filter, Search on different attributes. </li>
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