public static class _7_22_Prim
{
    public static void Run()
    {
        var graph = new Graph<SearchVertex>();
        graph.Add_BiDiredge("a","b",2);
        graph.Add_BiDiredge("a","c",3);
        graph.Add_BiDiredge("b","c",1);
        graph.Add_BiDiredge("b","d",1);
        graph.Add_BiDiredge("b","e",4);
        graph.Add_BiDiredge("d","e",1);
        graph.Add_BiDiredge("c","f",5);
        graph.Add_BiDiredge("f","e",1);
        graph.Add_BiDiredge("f","g",1);
        var tree = SpanningTree(graph,"a");
        foreach(var vert in tree) Console.WriteLine(vert);
        foreach(var vert in tree) Console.WriteLine($"->{vert.key}:{vert.distance}"); 
    }    
    private static Graph<SearchVertex> SpanningTree(Graph<SearchVertex> graph,string startVertKey) 
    {
        SearchVertex curVertx;
        Graph<SearchVertex> sTree = new();

        foreach (var vert in graph)
        {
            vert.distance = Int32.MaxValue;
        }
        
        var startVert = graph.Get_vertex(startVertKey);
        startVert.distance = 0;

        var pq = new DJPriorityQueue(maxheap:false);

        sTree.New_vertex(startVert.key);
        pq.Enqueue(startVert);
        
        while (pq.Count > 0)
        {
            curVertx = pq.Dequeue();

            if (curVertx.previous != null)
            {
                sTree.Add_edge(curVertx.previous.key,curVertx.key,curVertx.distance);
                sTree.Get_vertex(curVertx.key).distance = curVertx.distance;
            } 

            foreach (var adjVert in curVertx)
            {
                if (sTree.Contains(adjVert.key)) continue; 

                pq.Enqueue(adjVert);
                var newdistance = curVertx.distance+curVertx.GetNeighborWeight(adjVert);

                if (adjVert.distance > curVertx.GetNeighborWeight(adjVert) && pq.Contains(adjVert))
                {
                    //adjVert.distance = newdistance;
                    adjVert.previous = curVertx;
                    pq.SetDistance(adjVert,newdistance);
                }
            }
        }
        return sTree;
    }
}