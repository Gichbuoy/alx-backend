## Caching
- A caching system is a mechanism used in computing to temporarily store and manage frequently accessed or recently used data, with the goal of speeding up subsequent access to that data. Instead of fetching the data from the original source every time it is needed, the system stores a copy of the data in a cache, which is a faster but smaller and more easily accessible storage space.


### FIFO:
`FIFO` stands for "**_First In, First Out_**." It is a caching or queuing policy where the first item that is added to the cache is the first one to be removed when the cache reaches its capacity.

### LIFO:
`LIFO` stands for "**_Last In, First Out_**." In this policy, the most recently added item to the cache is the first to be removed when the cache is full. It operates opposite to FIFO.

### LRU:
`LRU` stands for "**_Least Recently Used_**." This caching policy removes the least recently accessed item from the cache when it reaches its limit, prioritizing items that have been accessed more recently.

### MRU:
`MRU` stands for "_Most Recently Used_." In contrast to LRU, this caching policy removes the most recently accessed item when the cache is full, prioritizing items that have been accessed least recently.

### LFU:
`LFU` stands for "_Least Frequently Used_." This policy removes the item from the cache that has been accessed the least number of times.


## Purpose of a Caching System:
The primary purpose of a caching system is to improve performance by reducing the time it takes to access frequently used or recently accessed data. 
- Caching minimizes the need to repeatedly fetch the same data from slower storage locations, such as databases or remote servers.

