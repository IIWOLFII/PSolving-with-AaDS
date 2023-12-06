// public class VertexBFS<T> : IBaseVertex<T>
// {
//     int distance = 0;
//     VertexBFS<T>? previous;
//     public VertexBFS(string key, int distance, VertexBFS<T>? prev = null, T? value = default) : base(key, value)
//     {
//         this.distance = distance;
//         this.previous = prev;
//     }
//     public override List<IBaseVertex<T>> GetNeighbors() // just iterate with foreach tbh
//     {
//         return adj.Keys.ToList();
//     }
    
// }

public class VertexBFS<T> : IEnumerable<VertexBFS<T>> // c# is too dogshit for a method to simply return 
{                           // data of a type of current class idk i'll make it work properly later maybe
    public readonly string key;
    public T? value;
    public Dictionary<VertexBFS<T>,int> adj {get;set;}
    public int distance;
    public VertexBFS<T>? previous;

    public VertexBFS (string key, int dist = 0, T? value = default(T), VertexBFS<T>? prev = null)
    {
        this.key = key;
        this.value = value;
        this.adj = new();
        this.previous = prev;
        this.distance = dist;
    }

    public void SetNeighbor (VertexBFS<T> vert, int weight = 0)
    {
        adj[vert] = weight;
    }
    public int GetNeighbor (VertexBFS<T> vert)
    {
        return adj[vert];
    }

    public List<VertexBFS<T>> GetNeighbors() // just iterate with foreach tbh
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

    public IEnumerator<VertexBFS<T>> GetEnumerator()
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

