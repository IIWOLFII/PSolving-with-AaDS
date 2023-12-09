public static class _7_17_TopoGraph
{
    public static void Run()
    {
        Graph<SearchVertex> graph = BuildGraph();
        _7_15_DFS.Run(graph,"3/4 cup milk");

        var travellist = graph.OrderBy(x => -x.closingTime).ToList();
        foreach (var i in travellist) Console.WriteLine($"{i.key} : {i.distance}/{i.closingTime}");
    }
    public static Graph<SearchVertex> BuildGraph()
    {
        var graph = new Graph<SearchVertex>();

        graph.Add_edge("3/4 cup milk","1 cup mix");
        graph.Add_edge("1 egg","1 cup mix");
        graph.Add_edge("1 tbl oil","1 cup mix");
        graph.Add_edge("1 cup mix","pour 1/4 cup");
        graph.Add_edge("1 cup mix","heat syrup");
        graph.Add_edge("heat syrup","eat");
        graph.Add_edge("heat griddle","pour 1/4 cup");
        graph.Add_edge("pour 1/4 cup","turn when bubbly");
        graph.Add_edge("turn when bubbly","eat");

        return graph;
    }
}