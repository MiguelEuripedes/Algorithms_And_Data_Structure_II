# 🏁 Project: Small Worlds 🚩


The purpose of this study is to explore the contents related to small-world networks and graphs. To achieve this, concepts such as assortativity, connected components, and clustering coefficient, among others, need to be applied. This work has been divided into three requirements:

- 1st Requirement: Select five networks from the [SNAP](https://snap.stanford.edu/index.html) website to analyze.

- 2nd Requirement: Create and interpret bipartite graphs concerning the assortativity with respect to the degree of nodes in each of these networks.

- 3rd Requirement: Compile and interpret a table where the columns represent properties specific to each of these networks, such as the number of vertices, the number of edges, degree assortativity coefficient, size of the Giant Connected Component (GCC), and the average clustering coefficient.
  
<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/assets/56210040/bbd0b466-3d26-4fcc-9bf5-73162891d84c" width="800" height="600">
</div>

This project was made by my ([Miguel](https://github.com/MiguelEuripedes)) as part of the course of Algorithms and Data Structures II, taught by [Prof. Ivanovitch Silva](https://github.com/ivanovitchm). Here the project is related to the weeks 9 aiming to take into practice the content of week 7 and 8. The portuguese video explaning the project and implementation can be found [here](https://www.loom.com/share/38d280626fbb47ee8c07078a712298ab?sid=3fa5d478-0032-4463-af2d-5243dd679d1e).

## 📌 Requirement 01 - Selecting Networks

Here you find the selected networks:

- [roadNet-PA](https://snap.stanford.edu/data/roadNet-PA.html): This netword represents the road network of Pennsylvania. Intersections and endpoints are represented by nodes, and the roads connecting these intersections or endpoints are represented by undirected edges.
- [Amazon co-purchasing product Network](https://snap.stanford.edu/data/com-Amazon.html): This network is derived from crawling the Amazon website, using the "Customers Who Bought This Item Also Bought" feature. It represents co-purchasing relationships between products. Each Amazon-defined product category forms a ground-truth community, with smaller communities of fewer than 3 nodes removed. The network focuses on the largest connected component, and the top 5,000 high-quality communities are detailed in the associated paper.
- [Wikipedia who-votes-on-whom Network](https://snap.stanford.edu/data/wiki-Vote.html): This network pertains to the voting processes within Wikipedia, specifically focusing on the election of administrators (or "admins"). Administrators are users with access to additional technical features to aid in Wikipedia maintenance. To become an administrator, a user must undergo a "Request for adminship" (RfA) process, during which the Wikipedia community decides, through public discussions or votes, who will be promoted to adminship.
- [Social circles from Facebook](https://snap.stanford.edu/data/ego-Facebook.html): This netword emphasizes Facebook 'circles' or friends lists, featuring node profiles, circles, and ego networks. Notably for the dataset, the Facebook data is anonymized, with user IDs replaced and feature meanings obscured.
- [Google web pages Network](https://snap.stanford.edu/data/web-Google.html): This network depicts web pages as nodes and their hyperlinks as directed edges, with data released in 2002 by Google for the Google Programming Contest.


## 🗃️ Rest of requirements

- 📁 [Requirement 02 - Assortativity with respect to the degree of network nodes](requirement_02/README.md)

- 📁 [Requirement 03 - Table of Graph Properties](requirement_03/README.md)


## References

[Ivanovitch's repository for algorithms and data structures](https://github.com/ivanovitchm/datastructure)
