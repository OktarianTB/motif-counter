# Network Motif Counter
This is a small Python Script I created for an assignment to count the number of occurences of motifs in a small graph. The original version can be found [here](https://gist.github.com/tpoisot/8582648) by [tpoisot](https://gist.github.com/tpoisot). It was updated to Python 3+ and adapted to work with motifs of all sizes, not just triplets. It currently supports only directed graphs, but there is an easy function to use that allows you to use it with undirected graph.

<br/><br/>
**All network graphs are defined using [NetworkX](https://networkx.org/documentation/stable/tutorial.html). Here is an example of the [Krackhardt Kite](https://en.wikipedia.org/wiki/Krackhardt_kite_graph):**

![Kite](/images/kite.png)

```python
G = nx.Graph([(0,1), (0,2), (0,3), (1,3), (1,2), (2,3), (1,4), (2,5), (3,4), (3,5), 
    (4,5), (3,6), (4,6), (5,6), (2,7), (5,7), (7,8), (8,9)])
```

<br/><br/>
**Similarly, here are 3 motifs:**


![Motif A](/images/motifA.png)
```python
motif_A = nx.Graph([(0,1), (0,2), (1,2), (1,3), (2,3)])
```
<br/>

![Motif B](/images/motifB.png)
```python
motif_B = nx.Graph([(0,1), (0,2), (1,2), (2,3), (2,4)])
```
<br/>

![Motif C](/images/motifC.png)
```python
motif_C = nx.Graph([(0,1), (0,2), (0,3), (1,3), (1,2), (2,3)])
```

<br/><br/>
**Then to count the number of occurences of each motif:**


```python
get_motif_count_undirected(G, motif_A) # outputs 9
get_motif_count_undirected(G, motif_B) # outputs 0
get_motif_count_undirected(G, motif_C) # outputs 2
```


