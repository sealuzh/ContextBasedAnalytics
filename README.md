# Context Based Analytics

Context-Based Analytics (CBA) is a research project between University of Zurich and IBM T.J. Watson Research Center in New York. 

## Problem
Diagnosing problems in large-scale, distributed applications running in cloud environments requires investigating different sources of information to reason about application state at any given time. Typical sources of information available to de- velopers and operators include log statements and other runtime information collected by monitors such as application and system metrics. Just as importantly, developers rely on information related to changes to the source code and configuration files (program code) when troubleshooting. This information is generally scattered, and it is up to the troubleshooter to inspect multiple implicitly-connected fragments thereof. Currently, different tools need to be used in conjunction, e.g., log aggregation tools, source-code management tools, and runtime-metric dashboards, each requiring different data sources and workflows. Not surprisingly, diagnosing problems is a difficult proposition. 
## Proposed Approach
We propose Context-Based Analytics (CBA), an approach that makes the links between runtime information and program-code fragments explicit by constructing a graph based on an application-context model. Implicit connections between information fragments are explicitly represented as edges in the graph. 

### Framework 

We designed a framework for expressing application-context models and implemented a prototype. 
To model entities to incorporate in the context graph, you need to provide


  - Data Extractor: Basically a formal description of the data source (e.g., HTTP API, database connector)
  - Model: The unique attributes that make up an entity and how to form it from the data extractor
  - Nodes: Definition of how models are represented in the graph and how it can expand
  - Visualization: Mapping from Node/Model to a Visualization (Time Series, KeyValue List, Code Fragment are available). There is a possibility to extend visualizations.
  - Entry Point: Definition of starting nodes that can be extended upon


### Disclaimer
Beware that this implementation only serves as a proof-of-concept. You should not use any of this code in production, seriously. For more informaton on code that sometimes comes out of a research enviornment, read this: http://matt.might.net/articles/crapl/
