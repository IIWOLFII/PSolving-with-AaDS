public static class _7_15_DFS
{
    static int currentstep = 0;

    public static Graph<SearchVertex> Run(Graph<SearchVertex> graph, string? startvertKey = null)
    {
        currentstep = 0;
        
        if (startvertKey != null) DFS(graph, graph.Get_vertex(startvertKey));

        foreach (var vert in graph)
        {
            if (vert.state != verStates.unexplored) continue;

            DFS(graph, graph.Get_vertex(vert.key));
        }
        return graph;
    }
    public static Graph<SearchVertex> Run(int graphSize, string? startvertKey = null)
    {
        var graph = _7_12_TourGraph.Run(graphSize);
        return Run(graph,startvertKey);
    }

    private static void DFS(Graph<SearchVertex> graph, SearchVertex curvert)
    {   
        curvert.state = verStates.discovered;

        curvert.distance = ++currentstep;

        foreach (var vertNeighbour in curvert)
        {
            if (vertNeighbour.state != verStates.unexplored) continue;
            //vertNeighbour.previous = curvert;
            DFS(graph,vertNeighbour);
        }

        curvert.state = verStates.exhausted;
        curvert.closingTime = ++currentstep;
    }
}

