public static class _7_15_DFS
{
    static int currentstep = 0;

    public static Graph<SearchVertex> Run(int graphSize)
    {
        currentstep = 0;
        var graph = _7_12_TourGraph.Run(graphSize);
        
        foreach (var vert in graph)
        {
            if (vert.state != verStates.unexplored) continue;
            DFS(graph, graph.Get_vertex(vert.key));
        }
        return graph;
    }

    private static void DFS(Graph<SearchVertex> graph, SearchVertex curvert)
    {   
        curvert.state = verStates.discovered;

        curvert.distance = ++currentstep;

        foreach (var vertNeighbour in curvert)
        {
            if (vertNeighbour.state != verStates.unexplored) continue;
            vertNeighbour.previous = curvert;
            DFS(graph,vertNeighbour);
        }

        curvert.state = verStates.exhausted;
        curvert.closingTime = ++currentstep;
    }
}

