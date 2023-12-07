# 🌎 Wikipedia Network - Similarity between pages of DevOps, Machine Learning, Blockchain, and Computer Security. 💻


In this project, the goal is to use the Wikipedia page network to analyze and construct graphs related to the pages mentioned in it. This process was done with four themes, namely the pages on DevOps, Machine Learning, Blockchain, and Information Security. Consequently, it was possible to analyze the similarity between the pages and thus create a graph that represented the connection between the common nodes of the networks found. For this entire process, I utilized the [NetworkX](https://networkx.org/) library in Python and [Gephi](https://gephi.org/) for graph manipulation and visualization.

That being said, the entire project and its analyses regarding the found results aim to fulfill the following requirements:

- **1st Requirement:** Generate a directed network (graph) from the links of Wikipedia pages considering the fusion of 4 SEEDs.

- **2nd Requirement:** From the constructed network, generate a figure using Gephi with the following information about the graph: Degree Centrality, Closeness Centrality, Betweenness Centrality, and finally, Eigenvector Centrality.

- **3rd Requirement:** From the constructed network, generate a figure showing the Cumulative Density Function (CDF) and the Probability Density Function (PDF) of the in-Degree of the network along with the histogram of this vertex property.

- **4th Requirement:** From the constructed network, generate a visualization of the graph highlighting the k-core and k-shell of the network.

- **5th Requirement:** Deploy the graph visualization so that the colors are related to the community criterion and the vertex size to the in-degree metric.

Thus, in the rest of this README, you will find the results of each requirement, except the first one. For the first requirement, if want to find the code used to generate the network, please refer to this Jupyter Notebook: [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Src/wiki_notebook.ipynb) 

Additionally, you can find the deployment for the 5th requirement in the following link. [![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)](https://migueleuripedes.github.io/Algorithms_And_Data_Structure_II/Implementations/projeto_WikiNetworkWithGephi/Upload/network/#Artificial%20Intelligence)

This deployment was made using the Sigma.js plugin for Gephi. The plugin can be found [here](https://www.sigmajs.org/).

  
<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/readme_mainpic.png?raw=true" width="1000" height="500">
</div>



This project was made by my ([Miguel](https://github.com/MiguelEuripedes)) as part of the course of Algorithms and Data Structures II, taught by [Prof. Ivanovitch Silva](https://github.com/ivanovitchm). Here the project is related to the weeks 12, aiming to take into practice the content of week 10, 11 and 12. The portuguese video explaning the project and implementation can be found 
[here ![Open in Loom](https://img.shields.io/badge/-Video-83DA77?style=flat-square&logo=loom)](https://www.loom.com/share/aefc1432d1734c1eae51efc7da1b8cb2?sid=79ee3483-c103-4a5d-a07c-32a3021f7538).



## 📌 Requirement 02 - Avaliation of the Network

I did not mentioned befora, but the result of the merging of the four networks was a graph with 826 nodes and 1,000 edges. This graph was then used to calculate the following metrics: Degree Centrality, Closeness Centrality, Betweenness Centrality, and Eigenvector Centrality. The following scale can resume how to understand the color scale for all these metrics.

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/scale.png?raw=true" >
</div>

To improve the visualization of the graph, I used the Force Atlas 2 algorithm to organize the nodes. This algorithm is a force-directed layout algorithm that simulates the attraction and repulsion forces between the nodes. The result of this algorithm can be seen in the following image.

For all the images I sellected some nodes randomly to give a little emphasis to the results. In some cases the nodes selected represent the higher values of the metric, in others not. This was done to show that difference and importance of each metric.


### 📊 2.1 - Degree Centrality

The degree centrality is a measure of the number of connections that a node has in a network. In this case, the degree centrality is the number of links that a page has to other pages. Thus, the higher the degree centrality, the more connections a page has to other pages.

To calculate the degree centrality, I used the following code:

```python
nx.set_node_attributes(common_subgraph, nx.degree_centrality(common_subgraph), 'degree_centrality')
```

The result of this code is a dictionary with the degree centrality of each node. This dictionary is then used to create a new attribute for each node in the graph. This attribute is the degree centrality of the node.

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/degree_centrality.png?raw=true" width="1000" height="500">
</div>

In this case the nodes Computer Security, Information Security and computer science where the ones with the highest degree centrality.

### 📊 2.2 - Closeness Centrality

The closeness centrality is a measure of the average distance of a node to all other nodes in the network. In this case, the closeness centrality is the average distance of a page to all other pages. Thus, the higher the closeness centrality, the closer a page is to all other pages. This metric is important because it can be used to identify the most important pages in a network.

In general terms, the closer a page is to others, the more central it is in the network. Therefore, pages with higher closeness centrality tend to be considered more important, as they are more accessible and connected to other parts of the network. This measure is particularly useful for evaluating communication efficiency and the speed at which a page can interact with others in the network.

Here is the code used to calculate this metric:
    
```python
nx.set_node_attributes(common_subgraph, nx.closeness_centrality(common_subgraph), 'closeness_centrality')
```

Here is the result image for this metric:

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/closeness_centrality.png?raw=true" width="1000" height="500">
</div>

Coincidentally, the nodes with the highest degree centrality are also the ones with the highest closeness centrality. This is because the more connections a node has, the closer it is to other nodes. However, this is not always the case, it all depends on the network. 


### 📊 2.3 - Betweenness Centrality

The betweenness centrality is a measure of the number of times a node acts as a bridge along the shortest path between two other nodes. In this case, the betweenness centrality is the number of times a page acts as a bridge along the shortest path between two other pages. Thus, the higher the betweenness centrality, the more a page acts as a bridge between other pages.

To calculate the betweenness centrality, I used the following code:

```python
nx.set_node_attributes(common_subgraph, nx.betweenness_centrality(common_subgraph), 'betweenness_centrality')
```

Check the image found for metric:
<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/betweeness_centrality.png?raw=true" width="1000" height="500">
</div>

From the image above we can see that the node 'Database' is the one with the highest betweenness centrality. Curiouly, the nodes 'Computer Security', 'Information Security' and 'computer science' also present a relatively high betweenness centrality. If you remember well these where nodes that connect the most to other nodes, and from the picture we can notice some of them really act as bridges between other nodes.


#### 📊 2.4 - Eigenvector Centrality

The eigenvector centrality is a measure of the influence of a node in a network. In this case, the eigenvector centrality is the influence of a page in a network. Thus, the higher the eigenvector centrality, the more influence a page has in a network.

To calculate the eigenvector centrality, I used the following code:

```python
nx.set_node_attributes(common_subgraph, nx.eigenvector_centrality(common_subgraph), 'eigenvector_centrality')
```

Below is the image found for this metric:

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/eigenvector_centrality.png?raw=true" width="1000" height="500">
</div>

The nodes with the highest eigenvector centrality are the ones with the highest degree centrality, what is somewhat expected. This is because the more connections a node has, the more influence it has in the network. However, this is not always the case, it all depends on the network.


## 📌 Requirement 03 - In-Degree Distribution

For this task the goal was to plot the Cumulative Density Function (CDF) and the Probability Density Function (PDF) of the in-Degree of the network along with the histogram of this vertex property. To do this, I used the seaborn library in Python that has the ```ecdfplot()``` function that provides de CDF plot, and the ```kdeplot()``` function that provides the PDF plot. The result can be seen below:

<div style="display: flex" align="center">
  <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/CDF_image.png?raw=true" width="500" />

  <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/PDF_image.png?raw=true" width="500" /> 
</div>

The Cumulative Distribution Function (CDF) plot illustrates the cumulative distribution of the in-degree within the network, showcasing how many nodes have an in-degree less than or equal to a given value. Simultaneously, the Probability Density Function (PDF) plot displays the probability distribution of in-degrees, providing insights into the likelihood of different in-degree values occurring. The accompanying histogram further visualizes the frequency distribution of in-degrees, revealing that a majority of nodes possess an in-degree between 0 and 30. Notably, the histogram highlights the presence of nodes with in-degrees exceeding 100, indicating potential outliers or nodes with significant connectivity.

## 📌 Requirement 04 - K-Core and K-Shell

For this task the first thing done by me was to calculate the core number of each node in the common_subgraph. The core number of a node is the largest value k of a k-core containing that node. A k-core is a maximal subgraph that contains nodes of degree k or more. The following code was used to calculate the core number of each node:

```python
set([v for k,v in nx.core_number(common_subgraph).items()])
```

The outcome is a set representing different k values for which the vertices are present in the k-core of the graph. 

If you wish to visualize the different k values for which vertices are present in the k-core of the graph, you can use this resulting set. For instance, if the resulting set is {2, 3, 4}, it signifies that the graph's vertices are present in the corresponding k-cores for k=2, k=3, and k=4. I my case I decided to use the highest k value, which was 143. In a simple way, doing this I can visualize the most dense and central subgraph of the network.

The highest-order k-core typically corresponds to the most densely connected portion of the graph, where nodes have significantly high degrees and are strongly interconnected with each other. Essentially, the highest-order k-core represents the backbone of the network.

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/comp_K_core_and_K_shell.png?raw=true" width="1000" height="500">
</div>

For the K-Shell, I used a differente value for k. For this case I used the value 4, which not necessarily is the highest value. The K-Shell is a subgraph of the network where all nodes have a degree of at least k. In this case, the K-Shell is a subgraph where all nodes have a degree of at least 4. 


## 💎Final look of the network

The image below shows the final look of the network. In this image, the nodes are colored according to the community criterion and the vertex size according to the in-degree metric.

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_WikiNetworkWithGephi/Images/final_graph.png?raw=true" width="1000" height="500">
</div>



## References

[Ivanovitch's repository for algorithms and data structures](https://github.com/ivanovitchm/datastructure)
