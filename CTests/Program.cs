using System;

namespace myApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("This is C# and how great it is!");
            Console.WriteLine(TestMethod(3));
        }

        static int TestMethod(int input)
        {
            int response = -1;
            response = input;
            return response;
        }
    }
}