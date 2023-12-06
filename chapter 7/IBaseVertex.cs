// public abstract class IBaseVertex<T> : IEnumerable<IBaseVertex<T>>
// {
//     private protected string key {get; set;}
//     public T? value {get; set;}
//     public Dictionary<IBaseVertex<T>,int> adj {get;set;}

//     public IBaseVertex (string key, T? value = default(T))
//     {
//         this.key = key;
//         this.value = value;
//         this.adj = new Dictionary<IBaseVertex<T>,int>();
//     }

//     public void SetNeighbor (IBaseVertex<T> vert, int weight = 0)
//     {
//         adj[vert] = weight;
//     }
//     public int GetNeighbor (IBaseVertex<T> vert)
//     {
//         return adj[vert];
//     }

//     public virtual List<IBaseVertex<T>> GetNeighbors() // just iterate with foreach tbh
//     {
//         return adj.Keys.ToList();
//     }

//     public override int GetHashCode() // repr but bad hash
//     {
//         unchecked
//         {
//             return (int)Math.Pow(key[0],31);
//         }
//     }

//     public override string ToString()
//     {
//         string sum = "";
//         return $"{key} connected to => {adj.Aggregate(sum,(_,x) => (sum += x.Key.key + ";"))}";
//     }

//     public IEnumerator<IBaseVertex<T>> GetEnumerator()
//     {
//         foreach (var i in adj)
//         {
//             yield return i.Key;
//         }
//     }

//     System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
//     {
//         return GetEnumerator();
//     }
// }