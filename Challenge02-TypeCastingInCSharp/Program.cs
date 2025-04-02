class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter  a number");
        int number = int.Parse(Console.ReadLine());

        if (number % 2 == 0)
        {
            Console.WriteLine("It's Even!");
        }
        else
        {
            Console.WriteLine("It's Odd!");
        }
        Console.ReadKey();
    }
}


