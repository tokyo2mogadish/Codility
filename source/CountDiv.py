import simplegui
import math

A = 100
B = 123000000
K = 2

def CountDiv(A, B, K):
    # write your code in Python 3.6
    return math.floor(B/K) - math.floor(A/K) + ( 1 if A%K == 0 else 0)

print (CountDiv(A, B, K))

#https://app.codility.com/demo/results/trainingHT22EY-JMY/

print ('----CountDiv in C#----')
#class Program
#    {
#        static void Main(string[] args)
#        {
#            int A = 100;
#            int B = 123000000;
#            int K = 2;

#            Console.WriteLine("{0}", string.Join(", ", CountDiv(A, B, K)));
#            Console.ReadLine();
#        }
#        public static double CountDiv(int A, int B, int K)
#        {
#            int remainder = 0;
#            if (A % K == 0)
#            {
#                remainder = 1;
#            }
#            return (Math.Floor((double)B/K) - Math.Floor((double)A/K) + remainder);
#        }
#    }
