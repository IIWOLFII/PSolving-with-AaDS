public abstract class BaseVertex<T> : IEnumerable<T> where T: BaseVertex<T>
{
    public string key {get;}
    public Dictionary<T,int> adj {get;set;}

    protected BaseVertex (string key)
    {
        this.key = key;
        this.adj = new Dictionary<T,int>();
    }

    public void SetNeighbor (T vert, int weight = 0)
    {
        adj[vert] = weight;
    }
    public int GetNeighborWeight (T vert)
    {
        return adj[vert];
    }

    public List<T> GetNeighbors() // just iterate with foreach tbh
    {
        return adj.Keys.ToList();
    }

    public override int GetHashCode() // repr but bad hash
    {
        unchecked
        {
            return (int)Math.Pow(key[0],31);
        }
    }

    public override string ToString()
    {
        string sum = "";
        return $"{key} connected to => {adj.Aggregate(sum,(_,x) => (sum += x.Key.key + ";"))}";
    }

    public IEnumerable<KeyValuePair<T,int>> GetEnumKV()
    {
        foreach (var i in adj)
        {
            yield return i;
        }
    }

    public IEnumerator<T> GetEnumerator()
    {
        foreach (var i in adj)
        {
            yield return i.Key;
        }
    }

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}

public static class VertexExtensions
{
    public static bool In<T>(this T ver, Graph<T> graph) where T: BaseVertex<T>
    {
        return graph.Contains(ver.key);
    }
}