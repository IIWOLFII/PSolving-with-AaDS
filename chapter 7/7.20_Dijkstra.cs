public static class _7_20_Dijkstra
{
    public static void Run()
    {
        var graph = new Graph<SearchVertex>();
        graph.Add_BiDirEdge("u","v",2);
        graph.Add_BiDirEdge("u","x",1);
        graph.Add_BiDirEdge("u","w",5);
        graph.Add_BiDirEdge("v","x",2);
        graph.Add_BiDirEdge("v","w",3);
        graph.Add_BiDirEdge("x","y",1);
        graph.Add_BiDirEdge("x","w",3);
        graph.Add_BiDirEdge("w","y",1);
        graph.Add_BiDirEdge("w","z",5);
        graph.Add_BiDirEdge("y","z",1);
        var startKey = "u";
        DijkstraPathsFrom(graph,startKey);
        Console.WriteLine($"Distances from {startKey} to:");
        foreach(var vert in graph) Console.WriteLine($"->{vert.key}:{vert.distance}");
    }

    private static void DijkstraPathsFrom(Graph<SearchVertex> graph,string startVertKey)
    {
        foreach (var vert in graph){
            vert.distance = Int32.MaxValue;}

        graph.Get_vertex(startVertKey).distance = 0;

        int totalDistance = 0;
        SearchVertex curVertx;

        var pq = new DJPriorityQueue(maxheap:false, graph.OrderBy(x=> x.distance).ToList());

        while (pq.Count > 0)
        {
            curVertx = pq.Dequeue();
            foreach(var adjVert in curVertx)
            {
                totalDistance = curVertx.distance + curVertx.GetNeighborWeight(adjVert); // accumulated dist + edge weight
                if (totalDistance < adjVert.distance)
                {
                    pq.SetDistance(adjVert,totalDistance);
                    adjVert.previous = curVertx;
                }
            }
        }
    }
}

public class DJPriorityQueue : MyPriorityQueue<SearchVertex>
{
    public DJPriorityQueue(bool maxheap) : base(maxheap){}
    public DJPriorityQueue(bool maxheap, List<SearchVertex> list) : base(maxheap, list){}

    protected override bool PriorityOver(SearchVertex item1, SearchVertex item2)
    {
        int res = item1.distance.CompareTo(item2.distance);
        if (res >= 0) return maxheap;
        return !maxheap;
    }

    public void SetDistance(SearchVertex vert, int newDistance)
    {
        vert.distance = newDistance;
        Heapify();
    }
}