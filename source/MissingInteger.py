# MissingInteger

import simplegui

def solution(A):
    B= list(sorted(A))

    if 1 not in A:
        return 1
    
    for i in range(1, max(B)):
        if i not in B:
            return i        

    return (max(B)+1)

#C#
 class Program
    {
        static void Main(string[] args)
        {
            int[] A = new int[] { -1, -3, 0, 1, 3, 5, 4567 };
            
            //Console.WriteLine(MaxCounters(N, A).ToString());
            Console.WriteLine("{0}", string.Join(", ", MissingInteger( A)));
            Console.ReadLine();
        }

        public static int MissingInteger(int[] A)
        {
            Array.Sort(A);

            if (!A.Contains(1))
            {
                return 1;
            }
            for (int i =1; i < A.Max(); i++)
            {
                if (!A.Contains(i))
                {
                    return i;
                }
            }
            return (A.Max()+1);
        }
    }