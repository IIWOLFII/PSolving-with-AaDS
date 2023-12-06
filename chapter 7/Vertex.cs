public class Vertex<T> : IEnumerable<Vertex<T>>
{
    public readonly string key;
    public T? value;
    public Dictionary<Vertex<T>,int> adj {get;set;}

    public Vertex (string key, T? value = default(T))
    {
        this.key = key;
        this.value = value;
        this.adj = new Dictionary<Vertex<T>,int>();
    }

    public void SetNeighbor (Vertex<T> vert, int weight = 0)
    {
        adj[vert] = weight;
    }
    public int GetNeighbor (Vertex<T> vert)
    {
        return adj[vert];
    }

    public List<Vertex<T>> GetNeighbors() // just iterate with foreach tbh
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

    public IEnumerator<Vertex<T>> GetEnumerator()
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
    public static bool In<T>(this Vertex<T> ver, Graph<T> graph)
    {
        return graph.Contains(ver.key);
    }
}