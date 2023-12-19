# 🚘 Route Optimization - Using OSMnx, NetworkX and Simulated Annealing in street nerworks. 🚩


In this project, my goal is to use the [OSMnx](https://github.com/icemagno/osmnx/tree/main) to analyze street networks and construct the best route given a number of locations to consider. To do this, I will use the [NetworkX](https://networkx.org/) library to create a graph from the street network and then use the [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing) algorithm to find the best route.

For this project, the source code was based on the following work done by Ossi Myllymäki: ["Conquering Seven Hills: Route Optimization With SA"](https://omyllymaki.medium.com/conquering-seven-hills-route-optimization-with-sa-d96ace682e2c)

That being said, this project seeks to work the following topics:

- Selection of the City and Tourist Spots.

- Implementation of the *Simulated Annealing* Algorithm

- User interface based on Folium and OSMnx

- Simulation e Test of itineraries

- Itinerary visualization

With that the results expected are:

- An optimized tourist itinerary that offers a efficient and pleasant experience for visitors
- Practical application and in-depth understanding of graphs with optimization algorithms.

Thus, in the rest of this README, you will find the results. If want to find the code used to generate the network, please refer to this Jupyter Notebook: [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)]([https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Notebook/Projeto_Roteiro.ipynb](https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Notebook/Projeto_Roteiro.ipynb)

This project was made by my ([Miguel](https://github.com/MiguelEuripedes)) as part of the course of Algorithms and Data Structures II, taught by [Prof. Ivanovitch Silva](https://github.com/ivanovitchm). Here the project is related to the final weeks of the course.

The portuguese video explaning the project and implementation can be found 
[here ![Open in YouTube](https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/OUEWqdlNFA4).



## Calculating the best route

The Traveling Salesman Problem (TSP) is a classic challenge in combinatorial optimization, specifically in route planning and transportation networks. It involves finding the most efficient route through a set of cities, visiting each once and returning to the starting point.

Graphs naturally represent the TSP, with cities as vertices and connections as edges. Python, with libraries like OSMnx and NetworkX, facilitates the practical implementation. OSMnx retrieves spatial data from OpenStreetMap, creating a graph of walkable roads. NetworkX then analyzes this graph, efficiently calculating the shortest distances between cities. This distance matrix serves as the foundation for TSP optimization.

### Simulated Annealing

Due to the problem's complexity, heuristic approaches like Simulated Annealing are valuable. It is a powerful algorithm for finding optimal routes, well-suited for problems like the traveling salesman. Unlike greedy algorithms prone to local minima, simulated annealing mimics the physical annealing process. It uses a temperature-driven concept, allowing random changes in the system. During each iteration, a mutated solution is generated, and with a probability determined by temperature, it may replace the current solution—even if worse. This randomness helps escape local minima. The algorithm's core involves temperature, mutation, probability, and termination conditions, all customizable based on the specific use case.

## The routes

For this project I explored the city of Natal, Brazil. Although not as large or internationally renowned as São Paulo, Rio de Janeiro, or Salvador, Natal is a city filled with numerous tourist attractions. For the tests, I chose to use three different tourist routes. These are:

### Gastronomic Route

This route is based on an article from the [TripAdvisor](https://www.tripadvisor.com.br/Restaurants-g303518-Natal_State_of_Rio_Grande_do_Norte.html) website. From there, I selected the first 6 restaurants on the list and created a route with them. This route is as follows:

```python
"Camarões" -> "La Brasserie de La Mer" -> "Marechal" -> "Manary Gastronomia & Arte" -> "Lotus" -> "Nau Frutos do Mar"
```

### Sea Route

This route is based on an article from this [website](https://visit.natal.br/roteiros/). From there, I selected one of the tourist itinerary. Specifically for this route, I selected the following points:

```python

```python
"Morro do Careca" -> "Via Costeira / Centro de convenções" -> "Relógio do Sol" -> "Letreiro - AMO NATAL" -> "Escadaria Mãe Luiza" -> "Centro Municipal de Artesanato da Praia do Meio" -> "Forte dos Reis Magos"
```

### Historical Center Itinerary.

This route is also based on an article from this [website](https://visit.natal.br/roteiros/). I decided to pick this route because it is the one that could be done by walking and had a lot more tourist spots than the others. 

```python
"Beco da Lama" -> "Espaço Cultural Ruy Pereira" -> "Igreja do Rosário dos Pretos - Mirante" -> "Praça André de Albuquerque" -> "Igreja Matriz Nossa Senhora da Apresentação" -> "Memorial Câmara Cascudo" -> "Igreja Bom Jesus das Dores" -> "Igreja Nossa Senhora de Lourdes" -> "Solar Bela Vista" -> "Instituto Histórico Geográfico do Rio Grande do Norte" -> "Rua da Conceição" -> "Museu Café Filho" -> "Bar de Nazaré" -> "Capitania das Artes" -> "Museu de Cultura Popular Djalma Maranhão" -> "Teatro Alberto Maranhão" -> "Instituto Câmara Cascudo"
```

## Results

The diagram presented below captures a standard execution of the algorithm. Initially, there's an exploration phase characterized by a high temperature, allowing the algorithm to accept solutions that might be worse than the current one. The accompanying figure on the right illustrates the calculated probability values influencing these decisions. As the iteration progresses, the temperature gradually decreases, leading to a reduced probability of accepting inferior solutions. Even at this stage, it's plausible for a solution with a low Δcost to be accepted as the current solution. Towards the end, as the temperature approaches zero, the algorithm shifts into a more deterministic, greedy behavior, accepting only solutions that unequivocally improve upon the current one (Δcost < 0). This dynamic evolution is reflected in the visualized outcomes of the Simulated Annealing process.


Here is the result for each route:

#### Gastronomic Route

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Imgs/GraphResult_GastronomicRoute.png?raw=true" width="600" height="400">
</div>

In this case, we have a network designed for cars, with 18,617 nodes and 48,453 edges. We observed that the algorithm quickly reduced the temperature. Before reaching 200 iterations, it was possible to identify a stabilization at a low temperature, indicating that the algorithm may have reached an acceptable point. However, towards the end, there was a slight variation with a slight increase in temperature, but it did not significantly alter the result. Therefore, the distance found was 24.13. This route explores a small part of one neighborhood and then moves to another, resulting in a higher cost.


#### Sea Route

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Imgs/GraphResult_SeaRoute.png?raw=true" width="600" height="400">
</div>

For this case, we have the same network as in the previous scenario (specifically designed for cars). We observed that the algorithm quickly found an acceptable solution. Before reaching 200 iterations, it was possible to identify a decrease in temperature, indicating a low probability of accepting impractical solutions (when compared to the current one). Therefore, the distance found was 32.07. It's worth noting that this route explores a significant portion of the city, making it a long route that consequently increases its cost.


#### Historical Center Itinerary

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Imgs/GraphResult_HistoricalCenter.png?raw=true" width="600" height="400">
</div>

In this case, if we have a longer route in a larger network (26,407 nodes and 77,414 edges), I opted to use more iterations of the Simulated Annealing (SA) to optimize the route. We observed a tumultuous start for the algorithm, but over time, it managed to cool down, eventually reaching a good solution for the problem. Nevertheless, the total distance obtained was 8.86, significantly shorter than the others. Since it's a feasible route to be done on foot, it is a quite reasonable consideration for a tourist itinerary.


### Visualization of the routes

The images below provide a visualization of the routes found by the algorithm, enhancing the understanding of both the problem and the solution obtained.

#### Gastronomic Route
<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Imgs/Map_GastronomicRoute.png?raw=true" width="600" height="400">
</div>

#### Sea Route

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Imgs/Map_SeaRoute.png?raw=true" width="600" height="400">
</div>

#### Historical Center Itinerary

<div align="center">
    <img src="https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_RouteOptimization/Imgs/Map_HistoricalCenter.png?raw=true" width="600" height="400">
</div>


## References

[Ivanovitch's repository for algorithms and data structures](https://github.com/ivanovitchm/datastructure)
