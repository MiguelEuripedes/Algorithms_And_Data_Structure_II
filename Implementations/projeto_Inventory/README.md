
# 📨 Building Fast Queries on a CSV - Extended 📦

This is the second project of the first unit of the course, and here I (Miguel Euripedes) present my results and implementations. The main objective of this project is to adapt the guided project "Building Fast Queries on a CSV" from the *Introduction to Algorithms* course of the Data Engineer path, made by [Dataquest](https://app.dataquest.io/).

The initial idea of this project is to create a class that allows you to view and manage basic functions of a store inventory.📦 
For this solution, I tried to create the class in such a way that it was possible to use it for different datasets, a little different from the project on the website, which focused on creating a class to manager an specific dataset. 
Here are some of the secondary objectives that guided design attempts to achieve:
 - How to analyze the time and space complexity of an algorithm.
 - How preprocessing the data can significantly speed-up an algorithm.
 - How to sort data and efficiently search sorted data.

It is worth remembering that despite trying to create a more general Python Class, the tests performed for this project used the same data as Dataquest, an dataset with minor adaptations. The original dataset can be found here: [Kaggle](https://www.kaggle.com/datasets/muhammetvarl/laptop-price). It is a database containing an inventory of laptops, with various information about the products, including Company, Screen Resolution, Memory, Ram and 8 other characteristics.

<p align="center">
<img src="./Images/inventory_pic.jpg" width="600" height="600"/>


📎Speaking a little about the main objectives of this project, I highlight that it must:

1. Implement additional features as suggested by Dataquest. That are:
    - Write a query that finds all laptops whose price is in the given range. Using `min_price` and `max_price`.
    - Write a query that find the cheapest laptop given some characteristics such as, for instance, 32GB of RAM and 512 GB of SDD. 

2. Analyze the complexity of the implemented algorithms, considering the Big O, Big θ (Theta), and Big Ω (Omega) notations.

Finally, here I aim to display the main informations about these new implementations and what complexity was found for each function. 

📽️*The portuguese video where I explain a little about this project can be found here [![Open in Loom](https://img.shields.io/badge/-Video-83DA77?style=flat-square&logo=loom)](https://www.loom.com/share/69d7d7aec7114280ae784cc230802eba?sid=b8a60342-d507-4c22-808e-fd1fdde0de60).*

📋You can also check the jupyter notebook containing the final `Inventory` class implementation here: [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_Inventory/Inventory_Additions.ipynb)

If you want to check the notebook made by me during the process of the guided project check this one:[![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](https://github.com/MiguelEuripedes/Algorithms_And_Data_Structure_II/blob/main/Implementations/projeto_Inventory/Inventory_Project.ipynb)



---


## 🚀 Initialize the Inventory:

To initialize the inventory in which you want to query for products, you must first create an instance of the class `InventoryExplorer`, passing the name of the **CSV** file as a parameter.
```
laptop_inventory = InventoryExplorer("laptops.csv")
```

With this, it is possible to use its internal parameter to view its size:
```
print("Number of rows in the inventory: ", len(laptop_inventory.rows))
```
*Output:*
> Number of rows in the inventory:  1303

---

It is also possible to have an initial view of it using the class method `show_inventory_basics`.

```
laptop_inventory.show_inventory_basics(rows = 3)
```
*Output:*
> Inventory header: 
>
> ['Id', 'Company', 'Product', 'TypeName', 'Inches', 'ScreenResolution', 'Cpu', 'Ram', 'Memory', 'Gpu', 'OpSys', 'Weight', 'Price'] 
>
> Row #1 of inventory: ['6571244', 'Apple', 'MacBook Pro', 'Ultrabook', '13.3', 'IPS Panel Retina Display 2560x1600', 'Intel Core i5 2.3GHz', '8GB', '128GB SSD', 'Intel Iris Plus Graphics 640', 'macOS', '1.37kg', '1339'] 
>
> Row #2 of inventory: ['7287764', 'Apple', 'Macbook Air', 'Ultrabook', '13.3', '1440x900', 'Intel Core i5 1.8GHz', '8GB', '128GB Flash Storage', 'Intel HD Graphics 6000', 'macOS', '1.34kg', '898'] 
>
> Row #3 of inventory: ['3362737', 'HP', '250 G6', 'Notebook', '15.6', 'Full HD 1920x1080', 'Intel Core i5 7200U 2.5GHz', '8GB', '256GB SSD', 'Intel HD Graphics 620', 'No OS', '1.86kg', '575'] 


## 📃Overview of the new Functions

### 🔎 1. `find_product_with_price_range`:

This is the first of the required functions, as already presented before, its functionality is expected to perform a search for products that fit into a lower and upper price limit. For its implementation, I used another function implemented through the activities carried out during the guided project.

```
def find_product_with_price_range(self, min_price, max_price):
        '''
        Find all the products with a price between min_price and max_price using the help of the find_first_product_more_expensive() method.

        Parameters:
            - min_price [int]: the minimum price to search for;
            - max_price [int]: the maximum price to search for;

        Output:
            - [list]: a list of all the products with a price between min_price and max_price;

        '''
        
        start_index = self.find_first_product_more_expensive(min_price)    
        if start_index == -1:
            return []
        end_index = self.find_first_product_more_expensive(max_price)    
        return self.rows_by_price[start_index:end_index]
```

As you can see, I used the function`find_first_product_more_expensive` to carry out this search, here I basically aimed to reuse code and it was also possible to obtain a function that, through a binary search, returned what was requested. 
Below is an example of how to use it:

```
print(laptop_inventory.find_product_with_price_range(200, 230))
```

*Output example:*
> [['7260172', 'Vero', 'K146 (N3350/4GB/32GB/W10)', 'Notebook', '14', '1920x1080', 'Intel Celeron Dual Core N3350 1.1GHz', '4GB', '32GB Flash Storage', 'Intel HD Graphics 500', 'Windows 10', '1.22kg', 202], ['2981902', 'Acer', 'Chromebook 15', 'Notebook', '15.6', '1366x768', 'Intel Celeron Dual Core 3205U 1.5GHz', '4GB', '16GB SSD', 'Intel HD Graphics', 'Chrome OS', '2.20kg', 209], ['8653550', 'HP', 'Stream 11-Y000na', 'Netbook', '11.6', '1366x768', 'Intel Celeron Dual Core N3060 1.6GHz', '2GB', '32GB Flash Storage', 'Intel HD Graphics 400', 'Windows 10', '1.17kg', 209], ['4141479', 'HP', 'Stream 11-Y000na', 'Netbook', '11.6', '1366x768', 'Intel Celeron Dual Core N3060 1.6GHz', '2GB', '32GB Flash Storage', 'Intel HD Graphics 400', 'Windows 10', '1.17kg', 209], ['9962421', 'HP', 'Stream 11-Y000na', 'Netbook', '11.6', '1366x768', 'Intel Celeron Dual Core N3060 1.6GHz', '2GB', '32GB Flash Storage', 'Intel HD Graphics 400', 'Windows 10', '1.17kg', 209], ['7673693', 'Vero', 'V142 (X5-Z8350/2GB/32GB/W10)', 'Notebook', '14', '1366x768', 'Intel Atom X5-Z8350 1.44GHz', '2GB', '32GB Flash Storage', 'Intel HD Graphics 400', 'Windows 10', '1.45kg', 210], ['7356172', 'Asus', 'A541NA-GO342 (N3350/4GB/500GB/Linux)', 'Notebook', '15.6', '1366x768', 'Intel Celeron Dual Core N3350 1.1GHz', '4GB', '500GB HDD', 'Intel HD Graphics 500', 'Linux', '2kg', 224], ['9775124', 'HP', 'Stream 14-AX040wm', 'Notebook', '14', '1366x768', 'Intel Celeron Dual Core N3060 1.6GHz', '4GB', '32GB SSD', 'Intel HD Graphics 400', 'Windows 10', '1.44kg', 229], ['6539218', 'Lenovo', 'IdeaPad 100S-14IBR', 'Notebook', '14', '1366x768', 'Intel Celeron Dual Core N3050 1.6GHz', '2GB', '64GB Flash Storage', 'Intel HD Graphics', 'Windows 10', '1.5kg', 229], ['2456795', 'Lenovo', 'IdeaPad 100S-14IBR', 'Notebook', '14', '1366x768', 'Intel Celeron Dual Core N3050 1.6GHz', '2GB', '64GB Flash Storage', 'Intel HD Graphics', 'Windows 10', '1.5kg', 229], ['9789209', 'Lenovo', 'IdeaPad 100S-14IBR', 'Notebook', '14', '1366x768', 'Intel Celeron Dual Core N3050 1.6GHz', '2GB', '64GB Flash Storage', 'Intel HD Graphics', 'Windows 10', '1.5kg', 229]]


### 🎯 2. `find_optimal_product_with`:

This is the second additional function requested. With it, the user is expected to find a product in the inventory that meets their requirements. In the case of laptops we can say, for example, the hardware requirements. By the way of how it was implemented, it performs a search based on a list of characteristics passed by the user. This search is carried out in such a way that the answers found meet all the previous requirements, not just one of them.

```
def find_optimal_product_with(self, desired_list=[], list_all=False):
        '''
        Find the cheapest product that has all the characteristics in the desired_list.

        Parameters:
            - desired_list [list]: a list of characteristics to search for;
            - list_all [bool]: if True, return all the products with the characteristics in the desired_list;

        Output:
            - [list]: the cheapest product with the characteristics in the desired_list;
            
            If list_all is True:
            - [list]: a list of all the products with the characteristics in the desired_list;
        '''
        if len(desired_list) == 0:
            return None, None

        possible_products = []
        for row in self.rows:                                                   
            if all(desired in row for desired in desired_list):
                possible_products.append(row)                                   

        if len(possible_products) == 0:
            return None, None
        
        
        cheapest_product = possible_products[0]                                
        for product in possible_products:                           
            if product[self.price_index] < cheapest_product[self.price_index]:
                cheapest_product = product                                     

        if list_all:
            return possible_products, cheapest_product
        else:
            return len(possible_products), cheapest_product
```

Above we have the code without comments, if you want to see the code some of my line comments, you can found it in the notebook. Below is an example of how to use it:

```
n_products, optimal_product = laptop_inventory.find_optimal_product_with(['32GB', '512GB SSD'], list_all=False)

print('We found {} products that match your desire. Here is the cheapest one: \n\n {}'.format(n_products, optimal_product))
```

*Output example:*
> We found 3 products that match your desire. Here is the cheapest one: 
>
>['8872177', 'Toshiba', 'Portege X30-D-10L', 'Ultrabook', '13.3', 'Full HD / Touchscreen 1920x1080', 'Intel Core i7 7500U 2.7GHz', '32GB', '512GB SSD', 'Intel HD Graphics 620', 'Windows 10', '1.05kg', 2799]

## ⌛Complexity Analisys

In the table below you can find my conclusions about the time complexity of each adapted function that was required. 

| *Complexity* | `find_product_with_price_range` | `find_optimal_product_with`|
|:------------:|:-------------------------------:|:--------------------------:|
|     Big O    |           *O(log n)*            |           *O(n)*           |
|     Big θ    |           *Θ(log n)*            |           *Θ(n)*           |
|     Big Ω    |             *Ω(1)*              |           *Ω(n)*           |

---

### 🔹 First Function

As I mentioned before, the overall time complexity of this function is influenced by the calls to `find_first_product_more_expensive`, which is O(log n) each time it's called. **This can only be done because the `self.rows_by_price` internal attribute is a sorted list!**.

> In the `find_first_product_more_expensive` I cannot perform a line count, as I usually do because of the `while` implemented.  
> We know that this function will executed a adaptation of the binary search algorithm, which depends on the length of the input data, in our case the `self.rows_by_price`, the thing is that at each iteration of the while loop, we are able to eliminate half of the elements in the list.
> So we started with the search depending on the size of N and now its possible to understand that the algorithm will reache the answer faster than expected once it works dividing the range of possible answers by 2 every iteration.
> This gives as a function that basically tells *the number of time we need to divide N by 2 to reach 1* well known as log(n).
> Going back to the `find_first_product_more_expensive` we understand that because of the binary search this function has a time complexity of log(N).

Going back to the `find_product_with_price_range` function, you can see that it uses the "helper" function twice, giving the insight that time complexity log(n) dominates its overall time complexity. Below I try to briefly explain the why of each complexity in the table above.

* *Worst Case* (O): In this case, we need to go through the entire list until we find the desired value, something that can happen if the desired values are at the ends of the list.
* *Average Case* (θ): In a generalized way, it is possible to say that to find the desired value, the algorithm continues to follow a logarithmic behavior if the case is not the optimal one.
* *Best Case* (Ω): This case happens when as soon as we start the search we already find the desired value, that is, the value to be searched for is in the middle of the ordered list.

Therefore, I highlight that I preferred to implement the function in this way because I would reuse code created during the evolution process of the guided project and would also maintain an algorithm with a lower complexity, when compared to the other implemented function. I'd like to recall that the final version of the `InventoryExplorer` class has the code with commented informations.

---

### 🔹Second Function

For this function, since in one of the parameter I'm passing a list of characteristics, the algorithm would have to iterate over the rows of the inventory and in together iterate over the list of desired products characteristics. With that in mind and reading over the code, of the final version of the `InventoryExplorer` class, you can see that `(m * p)` dominates over the rest of the complexity by line, since they are both integer number (`p` is the number of characteristics in desired_list and `m` the number of rows), I concluded that the overall time complexity would be in function of `n` - a integer number resulting of `(m * p)`.  

* *Worst Case* (O): This case happens when the product cannot be found in the list and in any other query search, because the algorithm has to iterate over each element anyways. 
* *Average Case* (θ): Here we have a result of the upper bound limit and lower bound being the same, causing the average complexity beaing the same as them.
* *Best Case* (Ω): The complexity here would be equal because even if the product is found right at the start it is still necessary to look over all of products to secure that all of the possible ones were selected.


# 📌Conclusion

In conclusion, cWith what was presented, it was possible to achieve the proposed objectives. Furthermore, I highlight that the step-by-step process of following the guided project gave me a deeper understanding of how to build more accurate and efficient queries, with examples of time execution and the practice of building a python class. As a result, the project was also important for the practice of programming and implementing these searches, enabling the understanding of the complexity of the codes and functions created, as well as the creation of a more documented code and how this could be done in a real work environment.

# References

[Ivanovitch's repository for algorithms and data structures](https://github.com/ivanovitchm/datastructure)

[Dataquest - Guided Project: Building Fast Queries on a CSV](https://app.dataquest.io/m/481/guided-project%3A-building-fast-queries-on-a-csv/1/the-dataset)
