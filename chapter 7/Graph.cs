using System.Collections;

public class Graph<T> : IEnumerable<Vertex<T>>
{
    private Dictionary<String,Vertex<T>> masterList;
    public Graph()
    {
        masterList = new Dictionary<String,Vertex<T>>();
    }
    public void Set_vertex(string key)
    {
        masterList.Add(key,new Vertex<T>(key));
    }
    public void Add_vertex(Vertex<T> ver)
    {
        masterList.Add(ver.key,ver);
    }
    public void Add_edge(string from, string to, int weight = 0)
    {
        if (!this.Contains(from))
        {
            Set_vertex(from);
        }
        if (!this.Contains(to))
        {
            Set_vertex(to);
        }
        masterList[from].SetNeighbor(masterList[to],weight);
    }
    public Vertex<T> Get_vertex(string key)
    {
        return masterList[key];
    }
    public List<string> Get_vertices()
    {
        return masterList.Select(x => $"Vertex({x.Key})").ToList();
    }

    public bool Contains(string key)
    {
        return masterList.ContainsKey(key);
    }

    public IEnumerator<Vertex<T>> GetEnumerator()
    {
        foreach(var i in masterList)
        {
            yield return i.Value;
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();;
    }
}