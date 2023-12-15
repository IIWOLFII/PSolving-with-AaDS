public static class _Exercise_18 // Two jugs, a 4-gallon and a 3-gallon. How can you get exactly two gallons of water in the 4-gallon jug
{
    public static void Run()
    {
        var graph = BuildJugGraph();
        string start = "0:0";
        int goalWaterInBig = 2;
        
        _7_9_BFS.BFS(graph,start);

        for (int i = 0; i < 4; i++)
        {
            string endgoal = $"{goalWaterInBig}:{i}";
            Console.WriteLine($"Path from {start} to {endgoal}");
            _7_9_BFS.PrintPathToStart(graph,endgoal);
            Console.WriteLine($"===============");
        }
            
    }

    static public Graph<SearchVertex> BuildJugGraph(int jug1size = 4, int jug2size = 3)
    {
        var graph = new Graph<SearchVertex>();

        int bigjugMax = Math.Max(jug1size,jug2size);
        int minjugMax = Math.Min(jug1size,jug2size);


        for(int bjug =0; bjug < bigjugMax+1; bjug++)
        {
            for(int sjug =0; sjug < minjugMax+1; sjug++)
            {
                string smallpour = $"{Math.Max(0,bjug-(minjugMax - sjug))}:{Math.Min(sjug+bjug,minjugMax)}";
                string bigpour = $"{Math.Min(bjug+sjug,bigjugMax)}:{Math.Max(0,sjug-(bigjugMax - bjug))}";
                string curpos = $"{bjug}:{sjug}";

                if (curpos != $"{bjug}:{minjugMax}") graph.Add_edge(curpos,$"{bjug}:{minjugMax}"); // fill small
                if (curpos != $"{bjug}:0") graph.Add_edge(curpos,$"{bjug}:0"); // drain small

                if (curpos != $"{bigjugMax}:{sjug}") graph.Add_edge(curpos,$"{bigjugMax}:{sjug}"); // fill large
                if (curpos != $"0:{sjug}") graph.Add_edge(curpos,$"0:{sjug}"); // drain large

                if (curpos != smallpour) graph.Add_edge(curpos, smallpour); // pour into small jug
                if (curpos != bigpour) graph.Add_edge(curpos, bigpour); // pour into large jug
            }
        }

        return graph;
    }
}