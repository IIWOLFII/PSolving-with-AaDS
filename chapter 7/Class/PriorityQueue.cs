// havent done this in like half a year

public class MyPriorityQueue<T> where T : IComparable
{
    protected readonly bool maxheap;
    protected List<T> storage;
    public int Count {get {return storage.Count;}}

    public MyPriorityQueue (bool maxheap, List<T> list)
    {
        this.maxheap = maxheap;
        this.storage = list;

        if (storage.Count > 0) Heapify();
    }   

    public MyPriorityQueue (bool maxheap) : this (maxheap, new List<T>()) {}

    public override string ToString()
    {
        string res = "";
        int idx = 0;
        var newline_pos = new int[]{0,2,6,14,30,62,126,254,510};

        foreach (var i in storage)
        {
            res += i + " ";
            if (newline_pos.Contains(idx)) res += "\n";
            idx++;
        }
        return res;
    }

    public T Peek()
    {
        return storage[0];
    }

    public bool Contains(T item)
    {
        return storage.Contains(item);
    }

    public void Enqueue(T item)
    {
        storage.Add(item);
        BubbleUp();
    }

    public T Dequeue()
    {
        int lastItemIdx = storage.Count-1;

        SwapItems(0,lastItemIdx);

        T item = storage[lastItemIdx];
        storage.RemoveAt(lastItemIdx);
        BubbleDown(0);

        return item;
    }

    private void BubbleUp(int? idx = null)
    {
        int curidx;
        if (idx == null) curidx = storage.Count-1;
        else curidx = (int)idx;

        Func<int,int> getparentidx = (x) => (x -1) / 2;

        while (PriorityOver(storage[curidx],storage[getparentidx(curidx)]) && curidx > 0) 
        {
            int parentidx = getparentidx(curidx);

            T tmp = storage[curidx];
            storage[curidx] = storage[parentidx];
            storage[parentidx] = tmp;

            curidx = (curidx -1) / 2;
        }
    }

    protected void Heapify()
    {
        int i = storage.Count / 2 - 1;
        while (i >= 0)
        {
            BubbleDown(i);
            i--;
        }
    }

    private void BubbleDown(int idx)
    {   
        while (true)
        {
            int highPChild_idx;
            if (!HPChild(idx, out highPChild_idx)) break;

            if (PriorityOver(storage[idx],storage[highPChild_idx])) break;

            SwapItems(idx,highPChild_idx);
            idx = highPChild_idx;
        }
    }
    
    private bool HPChild(int idx, out int highPChild_idx)
    {
        highPChild_idx = default(int);

        if (storage.Count-1 < idx*2+1) return false;// if left child doesnt exist then return false

        if (storage.Count-1 < idx*2+2) // if right child doesnt exist then return left child
        {
            highPChild_idx = idx*2+1;
            return true;
        }

        var leftIsHighPriority = PriorityOver(storage[idx*2+1], storage[idx*2+2]);
        highPChild_idx = leftIsHighPriority? idx*2+1 : idx*2+2;
        return true;
    }

    private void SwapItems(int idx1, int idx2)
    {
        T tmp = storage[idx1];
        storage[idx1] = storage[idx2];
        storage[idx2] = tmp;
    }

    protected virtual bool PriorityOver(T item1, T item2)
    {
        int res = item1.CompareTo(item2);
        if (res >= 0) return maxheap;
        return !maxheap;
    }

    
}


/*
var lis = new List<int>(){5,9,11,14,18,19,21,33,17,27}; //enq deq
//var lis = new List<int>(){9,6,5,2,3}; //heapify
var q = new MyPriorityQueue<int>(true,lis);

q.Enqueue(7);

q.Dequeue();

Console.WriteLine(q);
*/