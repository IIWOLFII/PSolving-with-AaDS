// absolute dogshit explanation in the most dogshit chapter of this book
// mf didnt even bother to mention the concept of low link values

public static class _7_18_SCC
{
    public static void Run()
    {
        Graph<SearchVertex> graph = _7_17_TopoGraph.BuildGraph();
        var tgraph = graph.TransposedCopy();

        _7_15_DFS.Run(graph,"3/4 cup milk");
        _7_15_DFS.Run(tgraph,graph.Where(x => x.closingTime == graph.Max(x=>x.closingTime)).First().key); // start with highest closing time vertex

        var travellist = graph.OrderBy(x => -x.closingTime).ToList();
        // foreach (var i in travellist) Console.WriteLine($"{i.key} : {i.distance}/{i.closingTime}"); // topo travel
        // Console.WriteLine("=========");

        travellist = tgraph.OrderBy(x => -x.closingTime).ToList();
        // foreach (var i in travellist) Console.WriteLine($"{i.key} : {i.distance}/{i.closingTime}"); // reversed topo travel but not really (i didnt touch dfs, only start vert)
        PrintSCC(travellist);

    }

    private static void PrintSCC(List<SearchVertex> travellist) // doesnt really work because why would it
    {
        var groups = new Dictionary<int,List<string>>();
        HashSet<SearchVertex> visited = new();

        int counter = 1;
        bool done = false;

        foreach (var vert in travellist)
        {
            done = true;

            if (visited.Contains(vert)) continue;
            else
            {
                groups[counter] = new List<string>();
                done = false;
                visited.Add(vert);
                groups[counter].Add(vert.key);
            }

            foreach (var adj in vert)
            {
                if (visited.Contains(adj)) continue;
                visited.Add(adj);
                groups[counter].Add(adj.key);
            }

            if (done) break;
            counter++;
        }

        Console.WriteLine($"=================");
        foreach (var group in groups)
        {
            Console.WriteLine($"Group {group.Key} ::::");
            foreach (var vert in group.Value)
                Console.WriteLine(vert);
            Console.WriteLine($"=================");
        }
    }
}


