/// <summary>
/// BFSearch
/// </summary>
public static class _7_9 
{
    ///<summary>
    /// Performs BFS, returns ????
    ///</summary>
    ///<params>
    /// Requires a graph with BFSVertices and a starting word from inside the graph
    ///</params>
    public static void Run(Graph<BFSVertex> graph, string startingword)
    {
        int dist_start = 0;
        int dist_previous = 0;
        var queueVerts = new Queue<BFSVertex>();
        queueVerts.Enqueue(graph.Get_vertex(startingword));
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
                }
            }
            curVert.state = verStates.exhausted;
        }
    }

    private static void TraversePrint()
    {
        // todo
    }
}

