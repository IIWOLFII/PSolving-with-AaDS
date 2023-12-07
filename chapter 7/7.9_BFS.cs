
/// <summary>
/// BFSearch
/// </summary>
public static class _7_9_BFS 
{
    ///<summary>
    /// Performs BFS updates graph verts
    ///</summary>
    ///<params>
    /// Requires a graph with BFSVertices and a target word from inside the graph
    ///</params>
    public static void Run(Graph<BFSVertex> graph, string targetword)
    {
        var targetvert = graph.Get_vertex(targetword);
        targetvert.distance = 0;
        targetvert.previous = null;
    
        var queueVerts = new Queue<BFSVertex>();
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
    }

    ///<summary>
    /// Paths to last BFS vert from given vert of a graph
    ///</summary>
    private static void FindTargetFrom(Graph<BFSVertex> graph, string startvert)
    {
        var cur = graph.Get_vertex(startvert);
        while (cur != null)
        {
            Console.WriteLine(cur.key);
            cur = cur.previous;
        }
    }

    public static void PathFromTo(Graph<BFSVertex> bFSVertices, string startingVertKey, string targetVertKey)
    {
        Run(bFSVertices,targetVertKey);
        FindTargetFrom(bFSVertices,startingVertKey);
    }
}

