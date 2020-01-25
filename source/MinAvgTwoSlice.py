import simplegui

A = [4, 2, 2, 5, 1, 5, 8]
def MinAvgTwoSlice(A):
    min = 1001
    minIndex = 0
    for i in range(len(A)-1):
        
        if (float(A[i])+float(A[i+1]))/2.0< min:
            min = (float(A[i])+float(A[i+1]))/2.0
            minIndex =  i
       
        if ((i+2<= len(A)-1) and float(A[i]+A[i+1]+A[i+2])/3.0< min) :
            min  = float(A[i]+A[i+1]+A[i+2])/3.0
            minIndex = i
    
    return minIndex

#Codility result link : https://app.codility.com/demo/results/trainingZWZH2N-C6H/

# C# Code
#class Program
#    {
#        static void Main(string[] args)
#        {
#            int[] A = new int[] { 4, 2, 2, 5, 1, 5, 8 };
#            Console.WriteLine("{0}", string.Join(", ", MinAvgTwoSlice(A)));
#            Console.ReadLine();
#        }
#
#        public static int MinAvgTwoSlice(int[] A)
#        {
#            double min = 1001;
#            int minIndex = 0;
#
#            for (int i=0; i < A.Length-1; i++)
#            {
#                if ((A[i] + A[i + 1]) / 2.0 < min)
#                {
#                    min = (A[i] + A[i + 1]) / 2.0;
#                    minIndex = i;
#                }
#                if( i+2< A.Length-1 && ((A[i] + A[i + 1]+ A[i+1])/ 3.0 < min))
#                {
#                    min = (A[i] + A[i + 1]+ A[i+1]) / 2.0;
#                    minIndex = i;
#                }
#            }
#
#            return minIndex;
#        }
#    }


    