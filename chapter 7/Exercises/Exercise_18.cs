public static class _Exercise_18 // Two jugs, a 4-gallon and a 3-gallon. How can you get exactly two gallons of water in the 4-gallon jug
{ // 
    public static void Run()
    {
        var graph = BuildJugGraph();
        // (int x,int y)[] moves = new (int x,int y)[]{(-1, -2),(-1, 2),(-2, -1),(-2, 1),(1, -2),(1, 2),(2, -1),(2, 1)};
        
        // foreach(var vert in graph){
        //     _7_12_TourGraph.GenLegalEdges(vert,graph,moves);
        // }

        // var resultGraph = _7_9_BFS.BFS(graph,"2:2");
        // _7_9_BFS.PrintPathToStart(resultGraph,"0:0");
    }

    static private Graph<SearchVertex> BuildJugGraph(int jug1size = 4, int jug2size = 3)
    {
        var graph = new Graph<SearchVertex>();

        for(int bjug =0; bjug < Math.Max(jug1size+1,jug2size+1); bjug++)
        {
            for(int sjug =0; sjug < Math.Min(jug1size+1,jug2size+1); sjug++)
            {
                var vertex = new SearchVertex($"{bjug}:{sjug}");
                graph.New_vertex($"{bjug}:{sjug}");
            }
        }

        return graph;
    }
}