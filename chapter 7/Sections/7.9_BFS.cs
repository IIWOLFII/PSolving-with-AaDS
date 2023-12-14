
/// <summary>
/// BFSearch
/// </summary>
public static class _7_9_BFS 
{
    public static void Run()
    {
        var graph = BFS(_7_7_LadderGraph.Run(debug:false),"sage");
        PrintPathToStart(graph,"fool");
    }

    ///<summary>
    /// Performs BFS updates graph verts
    ///</summary>
    ///<params>
    /// Requires a graph with SearchVertex and a target word from inside the graph
    ///</params>
    public static Graph<SearchVertex> BFS(Graph<SearchVertex> graph, string startKey)
    {
        var targetvert = graph.Get_vertex(startKey);
        targetvert.distance = 0;
        targetvert.previous = null;
    
        var queueVerts = new Queue<SearchVertex>();
        queueVerts.Enqueue(targetvert);

        while (queueVerts.Count > 0)
        {
            var curVert = queueVerts.Dequeue();
            foreach (var neighbor in curVert.GetNeighbors())
            {
                if (neighbor.state == verStates.unexplored)
                {
                    neighbor.state = verStates.discovered;
                    neighbor.distance = curVert.distance + 1;
                    neighbor.previous = curVert;
                    queueVerts.Enqueue(neighbor);
                }
            }
            curVert.state = verStates.exhausted;
        }
        return graph;
    }

    ///<summary>
    /// Prints path starting from argument vertex to starting vertex from which BFS was called
    ///</summary>
    public static void PrintPathToStart(Graph<SearchVertex> graph, string startvert)
    {
        var cur = graph.Get_vertex(startvert);
        while (cur != null)
        {
            Console.WriteLine(cur.key);
            cur = cur.previous;
        }
    }
}

