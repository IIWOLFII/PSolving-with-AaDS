public static class _7_6
{
    public static void Run()
    {
        var Graph = new Graph<int>();
        for (var i = 0;i < 6; i++)
        {
            Graph.Set_vertex(i.ToString());
        }

        foreach (var i in Graph.Get_vertices()) Console.WriteLine(i);

        Graph.Add_edge("0","1",5);
        Graph.Add_edge("0","5",2);
        Graph.Add_edge("1","2",4);
        Graph.Add_edge("2","3",9);
        Graph.Add_edge("3", "4", 7);
        Graph.Add_edge("3", "5", 3);
        Graph.Add_edge("4", "0", 1);
        Graph.Add_edge("5", "4", 8);
        Graph.Add_edge("5", "2", 1);

        foreach (var vert in Graph)
            foreach (var w in vert.GetNeighbors())
                Console.WriteLine($"({vert.key}, {w.key})");
    }
}