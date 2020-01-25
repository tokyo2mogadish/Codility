# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

import simplegui

def solution(N, A):
    test_array =[0]*len(range(1, max(A)))
    for i in A:
        if(i<=N):
            test_array[i-1] +=1
        else:
            test_array = [max(test_array)]*len(range(1, max(A)))
    
    return test_array
    
#class Program
#    {
#       static void Main(string[] args)
#       {
#           int[] A = new int[] { 3, 4, 4, 6, 1, 4, 4 };
#           int N = 5;
#           //Console.WriteLine(MaxCounters(N, A).ToString());
#           Console.WriteLine("[{0}]", string.Join(", ", MaxCounters(N, A)));
#           Console.ReadLine();
#       }

#       public static int[] MaxCounters(int N, int[] A)
#       {
#           int[] test_array = Enumerable.Repeat<int>(0, A.Length-2).ToArray();
#           foreach (int item in A)
#           {
#               if (item <= N)
#               {
#                   test_array[item - 1] += 1;
#               }
#               else
#               {
#                   test_array = Enumerable.Repeat<int>(test_array.Max(), A.Length-2).ToArray();
#               }
#           }
#           return test_array;
#       }