public class SearchVertex : BaseVertex<SearchVertex>
{
    public int distance = 0;
    public int closingTime = 0;
    public SearchVertex? previous = null;
    public verStates state = 0;
    public SearchVertex(string key) : base(key) {}
}

public enum verStates
{
    unexplored = 0,
    discovered = 1,
    exhausted = 2,
}