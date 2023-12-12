public static class _7_22_Prim
{
    public static void Run()
    {
        var graph = new Graph<SearchVertex>();
        graph.Add_BiDirEdge("a","b",2);
        graph.Add_BiDirEdge("a","c",3);
        graph.Add_BiDirEdge("b","c",1);
        graph.Add_BiDirEdge("b","d",1);
        graph.Add_BiDirEdge("b","e",4);
        graph.Add_BiDirEdge("d","e",1);
        graph.Add_BiDirEdge("c","f",5);
        graph.Add_BiDirEdge("f","e",1);
        graph.Add_BiDirEdge("f","g",1);
        var tree = SpanningTree(graph,"a");
        foreach(var vert in tree) Console.WriteLine(vert);
        foreach(var vert in tree) Console.WriteLine($"->{vert.key}:{vert.distance}"); 
    }    
    private static Graph<SearchVertex> SpanningTree(Graph<SearchVertex> graph,string startVertKey) 
    { // idk how to get it to work
        SearchVertex curVertx;
        Graph<SearchVertex> sTree = new();

        foreach (var vert in graph)
        {
            vert.distance = Int32.MaxValue;
        }

        graph.Get_vertex(startVertKey).distance = 0;
        int totaldistance = 0;

        var pq = new DJPriorityQueue(maxheap:false);
        pq.Enqueue(graph.Get_vertex(startVertKey));
        
        while (pq.Count > 0)
        {
            curVertx = pq.Dequeue();
            totaldistance = curVertx.distance;
            (int dist, SearchVertex vert) minDistVert = (int.MaxValue,null);

            foreach (var adjVert in curVertx)
            {
                //if (sTree.Contains(adjVert)) continue;
                var newdistance = totaldistance+curVertx.GetNeighborWeight(adjVert);

                if (adjVert.distance > newdistance)
                {
                    adjVert.distance = newdistance;
                    pq.SetDistance(adjVert,newdistance);
                }
                if (pq.Contains(adjVert) && adjVert.distance < minDistVert.dist) //!sTree.Contains(adjVert.key)
                {
                    minDistVert = (adjVert.distance, adjVert);
                } // todo it took c because it had same cost edge as b but instead its supposed to scan these two to move to the one with smallest edgecost
            }

            if (minDistVert.vert != null)
            {
                sTree.Add_edge(curVertx.key,minDistVert.vert.key,minDistVert.dist);
                sTree.Get_vertex(minDistVert.vert.key).distance = minDistVert.vert.distance;
                sTree.Get_vertex(curVertx.key).distance = curVertx.distance;
                sTree.Get_vertex(minDistVert.vert.key).previous = sTree.Get_vertex(curVertx.key);
            }

        }
        return sTree;
    }
}