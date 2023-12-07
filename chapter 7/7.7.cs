using System.Text.RegularExpressions;

public static class _7_7
{
    public static Graph<BFSVertex> Run() 
    {
        const char WILDCARDCHAR = '?';
        //string startword = "NOPE"; // unused
        string targetword = "POPE";

        var graph = new Graph<BFSVertex>();

        var words = new List<string>(){"POPE","ROPE","PIPE","POLE","POPS","NOPE","PAPE","PORE","HOPE","POSE","LOPE","POKE","MOPE","COPE"};
        var buckets = new Dictionary<string,List<string>>();

        for (int i = 0; i < targetword.Length; i++){
            var targetWCard = targetword.ToCharArray();
            targetWCard[i]= WILDCARDCHAR;
            buckets[new string(targetWCard)] = new List<string>();
        }

        foreach (var word in words){
            foreach (var bucketkey in buckets.Keys){
                if (Regex.IsMatch(word,WildCardToRegular(bucketkey))){
                    buckets[bucketkey].Add(word);
                }
            }
        }

        foreach (var bucket in buckets){
            foreach (var wordA in bucket.Value){
                foreach (var wordB in bucket.Value){
                    if (wordA == wordB) continue;
                    graph.Add_edge(wordA,wordB);
                }
            }
        }

        foreach (var i in graph)
        {
            Console.WriteLine(i);
        }

        return graph;
    }

    private static String WildCardToRegular(String value) 
    {
        return "^" + Regex.Escape(value).Replace("\\?", ".") + "$"; 
    }
}