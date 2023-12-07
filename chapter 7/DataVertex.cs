public class DataVertex<T> : BaseVertex<DataVertex<T>>
{
    T value;
    public DataVertex(string key, T value) : base(key)
    {
        this.value = value;
    }

}

