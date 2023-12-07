public class BFSVertex : BaseVertex<BFSVertex>
{
    public int distance = 0;
    public BFSVertex? previous = null;
    public verStates state = 0;
    public BFSVertex(string key) : base(key) {}
}

public enum verStates
{
    unexplored = 0,
    discovered = 1,
    exhausted = 2,
}