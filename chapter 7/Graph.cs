using System.Collections;

public class Graph<Vert_> : IEnumerable<Vert_> where Vert_: BaseVertex<Vert_>
{
    private Dictionary<String,Vert_> masterList;
    public Graph()
    {
        masterList = new Dictionary<String,Vert_>();
    }
    public void Set_vertex(string key)
    {
        Vert_? ver = System.Activator.CreateInstance(typeof(Vert_),key) as Vert_; // ??????????? i need an adult 
        if (ver != null) masterList.Add(key,ver);
    }
    public void Add_vertex(Vert_ ver)
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
    public Vert_ Get_vertex(string key)
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

    public IEnumerator<Vert_> GetEnumerator()
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