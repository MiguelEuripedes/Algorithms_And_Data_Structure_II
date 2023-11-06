# Requirement 03 - Table of Graph Properties

## Overview

The table below presents a set of metrics designed for graph networks, in this case representing different systems with their respective complexities. Each row in the table represents a specific network, and the columns provide information about the characteristics and properties of each one. Here, I seek to analyze the main conclusions drawn from the results presented in the table.

First, I highlight the description for each column and what it represents:
- The *first column* is simple and lists the names of the analyzed graph networks (all of them available on [SNAP](https://snap.stanford.edu/index.html)), primarily for identifying each observed system. 
- The *second column* represents the number of vertices (or nodes) in each network, indicating the size of the population or entities involved in the interaction.
- The *third column* refers to the number of edges (or connections) that link the vertices in the network, showing the extent of interactions or relationships between elements. 
- Now, for more complex features, the *fourth column* highlights the Degree assortativity coefficient. This coefficient measures the degree of assortativity in the network, indicating whether vertices with similar degrees tend to connect to each other. A positive value indicates assortativity, while a negative value indicates disassortativity. 
- The *fifth column* indicates how many distinct connected components exist in the network, which may reflect the presence of isolated subgroups. 
- The *penultimate column* deals with the Giant Connected Component Size, showing the size of the largest connected component in the network, highlighting the dominant or most densely connected part of the network. 
- Finally, the *last column* presents the clustering coefficient, measuring the tendency of vertices to form groups or clusters in the network, indicating the network's cohesion.

## Table

| Network          | Num. of Vertices | Num. of Edges | Degree assortativity coefficient | Num. of connected components | Giant Connected Component Size | Clustering coef. |
|---------------|-----------------|-------------|----------------------------------|----------------------------|-------------------------------------|---------------------|
| roadNet-PA  | 1088092           | 1541898      | 0.122749                        | 206                          | 1087562                               | 0.046477            |
| Amazon0601     | 403394           | 2443408      | -0.017647                        | 7                        | 403364                               | 0.417681            |
| Wiki-Vote | 7115            | 100762       | -0.083052                        | 24                         | 7066                                 | 0.140898            |
| facebook_combined | 4039           | 88234      | 0.063577                        | 1                          | 4039                               | 0.605547            |
| web-Google     | 875713            | 4322051      | -0.055089                        | 2746                         | 855802                                | 0.514296            |

---
## Description

Now, let's analyze the individual networks represented in the table:

1. **roadNet-PA**: With over a million vertices and more than a million edges, the roadNet-PA network is extensive and densely connected. Its assortativity coefficient of 0.1227 indicates a slight tendency for vertices with similar degrees to connect, although this value is relatively low. Furthermore, the network has 206 distinct connected components, suggesting a complex structure with multiple isolated groups. The size of the giant connected component (GCC) is impressive, with over a million vertices, and almost the entire network is part of it, highlighting the dominant part of the network. As for the clustering coefficient, it is relatively low, indicating moderate cohesion among the vertices. On average, approximately 4.65% of a vertex's neighbors are interconnected, which is interesting because in a transportation network, some road intersections may be interconnected in small areas, forming small clusters of traffic routes.

2. **Amazon0601**: This network consists of over 400,000 vertices and more than 2 million edges, indicating a complex network. With a negative degree assortativity coefficient of -0.0176, there is a suggestive tendency for disassortativity, where vertices with different degrees tend to connect. There are seven connected components in the network, indicating the presence of isolated subgroups. The size of the giant connected component is considerable, with once again, most of the vertices being a part of it. To conclude, the clustering coefficient is relatively high, suggesting that, on average, vertices in the network have a strong tendency to form densely connected groups or clusters. This is expected since this network is related to Amazon co-purchasing products.

3. **Wiki-Vote**: With over 7,000 vertices and more than 100,000 edges, the Wiki-Vote network is smaller than the previous ones. It has a negative degree assortativity coefficient, suggesting disassortativity. The network has 24 connected components, indicating a structure with several isolated groups. Its giant connected component (GCC) is smaller compared to other networks in the table, but the value indicates that the majority of the network is connected in a single giant component, allowing for high connectivity. Finally, the clustering coefficient is moderate, indicating reasonable cohesion in the network.

4. **facebook_combined**: With only 4,000 vertices and over 80,000 edges, this is the smallest network representing a real social network. Similar to the first network, the degree assortativity coefficient is positive, suggesting assortativity. Unlike the others, this network has only one connected component, indicating a single cohesive structure. The size of the giant connected component is equal to the total number of vertices, showing that the network is strongly connected. For this network, this means that it would be easy to disseminate information. The clustering coefficient is relatively high, reflecting the formation of groups. In the context of a social network, this may suggest that a user's friends tend to be friends with each other, forming well-defined communities.

5. **web-Google**: The last network is one of the largest in the table, with over 875,000 vertices and more than 4 million edges. In this network, the assortativity coefficient suggests disassortativity. There are 2,746 connected components, indicating a highly fragmented structure. This shows that the network consists of multiple isolated groups or sub-networks that are not connected to each other. It's important to note that each connected component is a collection of vertices (nodes) that are interconnected with each other but do not have connections to vertices outside that component. Moving on, once again, we have a network in which the giant connected component (GCC) is close to the total number of vertices, but there are many connected components, so one of them is responsible for a significant portion of the network. Finally, the clustering coefficient is similar to the previous one, indicating the presence of relatively well-defined groups in the network.

In summary, the table provides a comprehensive view of the properties of different graph networks. It demonstrates the diversity of structures and behaviors found in complex systems, from road networks to social networks and the web.