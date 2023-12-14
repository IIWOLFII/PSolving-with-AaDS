public static class _Exercise_17 // all pairs shortest path problem
{ // 
    public static void Run()
    {
        int[,] result = FloydWarshall(MakeGraph());
        PrintAdjMatrx(result);
        
        //BlindAttemptBFS();
    }

    private static int[,] FloydWarshall(Graph<SearchVertex> graph)
    {
        int nKeys = graph.Count();

        int[,] matrix = new int[nKeys,nKeys];

        for (int i = 0; i < matrix.GetLength(0); i++){
            for (int j = 0; j < matrix.GetLength(1); j++){

                int? weight = graph.Get_vertex($"{i+1}").TryGetNeighborWeight(graph.Get_vertex($"{j+1}"));

                if (weight != null){
                    matrix[i,j] = (int)weight;
                    continue;
                }

                if (i == j){
                    matrix[i,j] = 0;
                    continue;
                }

                matrix[i,j] = int.MaxValue;
            }
        }

        for (int k = 0; k < nKeys; k++){ // foreach (key in graph)
            for (int row = 0; row < nKeys; row++){ // foreach (vertStart in graph)

                if (row == k) continue; // for 2:3 we cant traverse  through 2:2 2:3

                for (int col = 0; col < nKeys; col++) // foreach (vertEnd in graph)
                {
                    if (col == k) continue; // for 3:2 we cant traverse  through 3:3 2:3

                    if (matrix[col,k] == int.MaxValue || matrix[k,row] == int.MaxValue) continue; // if there are no edges through k then skip this calculation

                    //if (matrix[col,row] > matrix[col,k] + matrix[k,row])
                    //    matrix[col,row] = matrix[col,k] + matrix[k,row];
                    matrix[col,row] = Math.Min(matrix[col,row], matrix[col,k] + matrix[k,row]);
                    //Console.WriteLine($"matrix[{col},{row}] through {k} = min(matrix[{col},{row}]:{matrix[col,row]}, matrix[{col},{k}]:{matrix[col,k]}]) + matrix[{k},{row}]:{matrix[k,row]}");
                }
            }
        }

        return matrix;
    }

    private static void BlindAttemptBFS() 
    {
        var ResAdjMatrix = new int[4,4];
        for (int i = 0; i < ResAdjMatrix.GetLength(0); i++)
            for (int j = 0; j < ResAdjMatrix.GetLength(1); j++)
                ResAdjMatrix[i,j] = Int32.MaxValue;

        var keys = new string[]{"1","2","3","4"};

        foreach (var startvertkey in keys){   
            var graph = MakeGraph();
            _7_9_BFS.BFS(graph,startvertkey);

            foreach (var targetvert in graph){
                var cur = graph.Get_vertex(targetvert.key);
                while (cur != null){
                    cur = cur.previous;
                }
                int i = Int32.Parse(startvertkey);
                int j = Int32.Parse(targetvert.key);
                if (ResAdjMatrix[i-1,j-1] > targetvert.distance){
                    ResAdjMatrix[i-1,j-1] = targetvert.distance;
                }
            }
        }

        PrintAdjMatrx(ResAdjMatrix);
            
    }

    private static void PrintAdjMatrx(int[,] AdjMatrix)
    {
        for (int i = 0; i < AdjMatrix.GetLength(0); i++){
            for (int j = 0; j < AdjMatrix.GetLength(1); j++){
                Console.Write(AdjMatrix[i,j]);
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