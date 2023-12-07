public static class _7_12_Tour // todo
{
    public static void Run(int size)
    {
        var graph = BuildKnightGraph(size);
        // graph build_graph{
        //      create nxn loop
        //          add vert at x -> n, y -> j
        //      foreach vert in graph
        //          generate legelmoves(vert)


        // genmoves
        //      foreahc offset
        //              if offset exists in graph:
        //                      addedge (from vert to offset)
    }

    private static Graph<BFSVertex> BuildKnightGraph(int n) // topleft is (0;n-1) bottomright is (n-1;0)
    {
        var graph = new Graph<BFSVertex>();

        for (int y = n-1; y > -1; y--){
            for (int x = 0; x < n; x++){
                graph.Set_vertex($"{x}:{y}"); // should i use 2dvector key?
            }
        }
        return graph;
    }

    private static void GenLegalEdges(BFSVertex vert) // todo
    {
        //static  moves = // figure out what kind of key i will have then bake an array of moves
    }
}