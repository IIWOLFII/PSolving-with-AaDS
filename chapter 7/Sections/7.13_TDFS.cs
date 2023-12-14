public static class _7_13_Tour_DFS
{

    public static bool Run(string startvertKey,int graphSize, out List<string> path, bool heuristic = true)
    {
        SearchType search;

        path = new List<string>();
        var graph = _7_12_TourGraph.Run(graphSize);

        if (heuristic) search = SearchHeuristic;
        else search = SearchRegular;

        return DFS(graph, graph.Get_vertex(startvertKey), path, search);
    }

    private static bool DFS(Graph<SearchVertex> graph, SearchVertex curvert, List<string> path , SearchType SearchNeighbours, int edgecount = 0)
    {   
        double size = Char.GetNumericValue(graph.First().key[2])+1;
        string breadcrumb = " => " + curvert.key;

        path.Add(breadcrumb);

        if (edgecount >= Math.Pow(size,2)-1) return true; // we are done
        
        curvert.state = verStates.discovered;

        bool done = SearchNeighbours(graph,curvert,path,SearchNeighbours,edgecount);
        
        if (!done) // backtrack
        {
            curvert.state = verStates.unexplored;
            path.Remove(breadcrumb);
        } 

        return done;
    }

    private delegate bool SearchType(Graph<SearchVertex> graph, SearchVertex curvert, List<string> path , SearchType heuristic, int edgecount);

    static bool SearchRegular(Graph<SearchVertex> graph, SearchVertex curvert, List<string> path , SearchType heuristic, int edgecount)
    {
        bool done = false;
        foreach(var neigbour in curvert)
        {
            if (neigbour.state != verStates.unexplored) continue;
            done = DFS(graph,neigbour,path,heuristic, edgecount+1);
            if (done) {break;}
        }
        return done;
    }

    static bool SearchHeuristic(Graph<SearchVertex> graph, SearchVertex curvert, List<string> path , SearchType heuristic, int edgecount)
    {
        bool done = false;
        var adjustment = curvert.OrderBy(x => x.adj.Count).ToList();
        foreach(var neigbour in adjustment)
        {
            if (neigbour.state != verStates.unexplored) continue;
            done = DFS(graph,neigbour,path,heuristic, edgecount+1);
            if (done) {break;}
        }
        return done;
    }
}