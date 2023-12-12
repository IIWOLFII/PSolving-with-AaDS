public class SearchVertex : BaseVertex<SearchVertex>, IComparable
{
    public int distance = 0;
    public int closingTime = 0;
    public SearchVertex? previous = null;
    public verStates state = 0;
    public SearchVertex(string key) : base(key) {}

    public int CompareTo(object? obj) 
    {
        throw new NotSupportedException("You reallly should just compare the fields instead");
    }
}

public enum verStates
{
    unexplored = 0,
    discovered = 1,
    exhausted = 2,
}