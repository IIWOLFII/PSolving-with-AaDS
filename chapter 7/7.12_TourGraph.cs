public static class _7_12_TourGraph
{
    static (int x,int y)[] moves = new (int x,int y)[]{(-1, -2),(-1, 2),(-2, -1),(-2, 1),(1, -2),(1, 2),(2, -1),(2, 1)};
    
    public static Graph<SearchVertex> Run(int size)
    {
        var graph = BuildKnightGraph(size);
        foreach(var vert in graph){
            GenLegalEdges(vert,graph);
        }

        // int sum = 0;
        // graph.Aggregate(sum,(_,x) => (sum += x.adj.Count));
        // Console.WriteLine(sum);

        // foreach(var i in graph)
        // {
        //     Console.WriteLine(i);
        // }

        return graph;
    }

    private static Graph<SearchVertex> BuildKnightGraph(int n) // topleft is (0;n-1) bottomright is (n-1;0)
    {
        var graph = new Graph<SearchVertex>();

        for (int y = n-1; y > -1; y--){
            for (int x = 0; x < n; x++){
                graph.Set_vertex($"{x}:{y}");
            }
        }
        return graph;
    }

    private static void GenLegalEdges(SearchVertex vert, Graph<SearchVertex> graph)
    {
        foreach(var move in moves){
            string moveXY = $"{Char.GetNumericValue(vert.key[0]) +move.x}:{Char.GetNumericValue(vert.key[2])+move.y}";
            if (graph.Contains(moveXY)){
                graph.Add_edge(vert.key,moveXY);
            }
        }
    }
}