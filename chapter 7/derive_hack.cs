/*
var b = new B();
var dumm = new B(){customfield = 5};
b.spisok.Add(dumm);

Console.WriteLine(b.ret().First().customfield);
Console.WriteLine(b.ret().First().GetType());

abstract class A<T> where T: A<T>
{
    public virtual List<T> spisok {get;set;}
    protected A()
    {
        spisok = new();
    }
    public virtual List<T> ret()
    {
        return spisok;
    }
}

class B : A<B>
{
    public int customfield = 3;
}
*/

