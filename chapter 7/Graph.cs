using System.Collections;

public class Graph<vertex> : IEnumerable<vertex> where vertex: BaseVertex<vertex>
{
    private Dictionary<String,vertex> masterList;
    public Graph()
    {
        masterList = new Dictionary<String,vertex>();
    }
    public void Set_vertex(string key)
    {
        vertex ver = System.Activator.CreateInstance(typeof(vertex),key) as vertex; // ??????????? i need an adult 
        masterList.Add(key,ver); // todo
    }
    public void Add_vertex(vertex ver)
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
    public vertex Get_vertex(string key)
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

    public IEnumerator<vertex> GetEnumerator()
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