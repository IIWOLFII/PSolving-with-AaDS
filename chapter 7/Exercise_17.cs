public static class _Exercise_17 // all pairs shortest path problem
{ // https://www.youtube.com/watch?v=Gc4mWrmJBsw https://www.youtube.com/watch?v=oNI0rf2P9gE https://youtu.be/NzgFUwOaoIw?t=198 <-
    public static void Run()
    {
        BlindAttemptBFS();
    }

    private static void BlindAttemptBFS() 
    {// some values are incorrect because bfs doesnt prioritise smallest edges when moving around duh
        var ResAdjMatrix = new int[4,4];            // probably fine with dijkstras // nvm that doesnt work with negatives
        for (int i = 0; i < ResAdjMatrix.GetLength(0); i++)
            for (int j = 0; j < ResAdjMatrix.GetLength(1); j++)
                ResAdjMatrix[i,j] = Int32.MaxValue;

        var keys = new string[]{"1","2","3","4"};

        foreach (var startvertkey in keys)
        {   
            var graph = MakeGraph();
            _7_9_BFS.BFS(graph,startvertkey);

            foreach (var targetvert in graph)
            {
                var cur = graph.Get_vertex(targetvert.key);
                while (cur != null)
                {
                    cur = cur.previous;
                }
                int i = Int32.Parse(startvertkey);
                int j = Int32.Parse(targetvert.key);
                if (ResAdjMatrix[i-1,j-1] > targetvert.distance)
                {
                    ResAdjMatrix[i-1,j-1] = targetvert.distance;
                }
                
            }
        }

        for (int i = 0; i < ResAdjMatrix.GetLength(0); i++){
            for (int j = 0; j < ResAdjMatrix.GetLength(1); j++){
                Console.Write(ResAdjMatrix[i,j]);
                Console.Write("\t");
            }
            Console.WriteLine("");
        }
            
    }

    private static Graph<SearchVertex> MakeGraph() // i cant clone it so this will do for now
    {
        var graph = new Graph<SearchVertex>();
        graph.Add_edge("1","2",9);
        graph.Add_edge("1","3",-4);
        graph.Add_edge("2","1",6);
        graph.Add_edge("2","4",2);
        graph.Add_edge("3","2",5);
        graph.Add_edge("4","3",1);
        return graph;
    }
}