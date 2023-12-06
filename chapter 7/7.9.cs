public static class _7_9
{
    public static void Run(VertexBFS<verStates> start)
    {
        int dist_start = 0;
        int dist_previous = 0;
        var queueVerts = new Queue<VertexBFS<verStates>>();
        queueVerts.Enqueue(start);
        while (queueVerts.Count > 0)
        {
            var curVert = queueVerts.Dequeue();
            foreach (var neighbor in curVert.GetNeighbors())
            {
                if (neighbor.value == verStates.unexplored)
                {
                    neighbor.value = verStates.discovered;
                    neighbor.distance = curVert.distance + 1;
                    neighbor.previous = curVert;
                    queueVerts.Enqueue(neighbor); //todo GetNeighbors returns wrong fucking type despite being derived
                    // https://stackoverflow.com/questions/2070766/how-to-reference-current-class-type-using-generics
                }
            }
            curVert.value = verStates.exhausted;
        }


    }

    public enum verStates
    {
        unexplored = 0,
        discovered = 1,
        exhausted = 2,
    }
}