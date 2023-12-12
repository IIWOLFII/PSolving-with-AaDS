using System.Collections;

public class Graph<Vert_> : IEnumerable<Vert_> where Vert_: BaseVertex<Vert_>
{
    private Dictionary<String,Vert_> masterList;
    public Graph()
    {
        masterList = new Dictionary<String,Vert_>();
    }
    public void New_vertex(string key)
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
            New_vertex(from);
        }
        if (!this.Contains(to))
        {
            New_vertex(to);
        }
        masterList[from].SetNeighbor(masterList[to],weight);
    }
    public void Add_BiDirEdge(string from, string to, int weight = 0)
    {
        Add_edge(from,to,weight);
        Add_edge(to,from,weight);
    }
    
    public Vert_ Get_vertex(string key)
    {
        return masterList[key];
    }

    public Graph<Vert_> TransposedCopy()
    {
        var newgraph = new Graph<Vert_>();
        foreach (var vert in masterList)
            foreach (var adj in vert.Value)
                {
                    newgraph.Add_edge(adj.key,vert.Value.key);
                }
        return newgraph;
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