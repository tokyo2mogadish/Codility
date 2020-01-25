# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

import simplegui

A = [200, 10000000000, 10, 200, 3, 1]

def Distinct(A):
    # write your code in Python 3.6
    return len(set(A))

print (Distinct(A))

#https://app.codility.com/demo/results/trainingVREC2V-QTE/

print ('----Distinct in C#----')
#class Program
#    {
#        static void Main(string[] args)
#        {
#            int[] A = new int[] { 200, 100000, 10, 200, 3, 1 };
            
#            //Console.WriteLine(MaxCounters(N, A).ToString());
#            Console.WriteLine("{0}", string.Join(", ", Distinct(A)));
#            Console.ReadLine();
#        }

#        public static int Distinct(int[] A)
#        {
#            return A.Distinct().ToArray().Length;
#        }
#    }
