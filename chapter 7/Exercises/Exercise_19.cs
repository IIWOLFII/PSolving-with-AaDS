public static class _Exercise_19 /// Two jugs, a 4-gallon and a 3-gallon. How can you get exactly two gallons of water in the 4-gallon jug
{ // Parametrizeable (i think)
    public static void Run(int Jar1, int Jar2, int goalWaterInBig)
    {
        var graph = _Exercise_18.BuildJugGraph(Jar1,Jar2);
        string start = "0:0";
        
        _7_9_BFS.BFS(graph,start);

        for (int i = 0; i < Math.Max(Jar1,Jar2)-1; i++)
        {
            string endgoal = $"{goalWaterInBig}:{i}";
            Console.WriteLine($"Path from {start} to {endgoal}");
            _7_9_BFS.PrintPathToStart(graph,endgoal);
            Console.WriteLine($"===============");
        }
    }
}