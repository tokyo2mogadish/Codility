using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Linq;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solution(3, "1A 2D 1K ").ToString());
            Console.ReadLine();
        }
        public static int solution(int N, string S)
        {
            // write your code in C# 6.0 with .NET 4.5 (Mono)
            string[] str = S.Split(' ');
            if (S == "")
            {
                return N * 2;
            }
            List<String> occupied = new List<String>();
            int available = 0;

            //occupied = Arrays.asList(str);
            occupied = str.OfType<string>().ToList();

            for(int i = 1; i<= N ; i++)
            {
                int count = 0;
            
                if(!occupied.Contains(i + "B") && !occupied.Contains(i + "C") && !occupied.Contains(i + "D") && !occupied.Contains(i + "E"))
                {
                    count++;
                }
                
                if(!occupied.Contains(i + "F") && !occupied.Contains(i + "G") && !occupied.Contains(i + "H") && !occupied.Contains(i + "J"))
                {
                    count++;
                }

                if (!occupied.Contains(i + "D") && !occupied.Contains(i + "E") && !occupied.Contains(i + "F") && !occupied.Contains(i + "G"))
                {
                    switch (count)
                        {
                        case 0:
                                count += 1;
                                break;
                        case 1:
                                
                                break;
                        case 2:
                                
                                break;

                        }
                                         
                }

                available += count;
                
            }
            
            return available;
        }

    }
}
