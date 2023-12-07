using System.Text.RegularExpressions;

/// <summary>
/// Returns word ladder graph
/// </summary>
public static class _7_7_LadderGraph
{
    public static Graph<BFSVertex> Run(bool debug = true) 
    {
        const char WILDCARDCHAR = '?';
        
        var graph = new Graph<BFSVertex>();

        //var words = new HashSet<string>(){"POPE","ROPE","PIPE","POLE","POPS","NOPE","PAPE","PORE","HOPE","POSE","LOPE","POKE","MOPE","COPE"}; //one letter difference at most
        var words = new HashSet<string>(){"fool","pool","foil","foul","cool","poll","fail","pole","pall","pope","pale","page","sale","sage"};
        var buckets = new Dictionary<string,HashSet<string>>();

        foreach (var bucketword in words){
            for (int i = 0; i < bucketword.Length; i++){
                var targetWCard = bucketword.ToCharArray();
                targetWCard[i]= WILDCARDCHAR;
                buckets[new string(targetWCard)] = new HashSet<string>();
            }
        }

        foreach (var word in words){
            foreach (var bucketkey in buckets.Keys){ // instead of wordlen**wordlen comparisons, we compare wordlen**(wordlen*4) how is this any better
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

        if (debug){
            foreach (var i in graph){
                Console.WriteLine(i);
            }
        }

        return graph;
    }

    private static String WildCardToRegular(String value) 
    {
        return "^" + Regex.Escape(value).Replace("\\?", ".") + "$"; 
    }
}