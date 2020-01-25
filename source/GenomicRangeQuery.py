import simplegui

S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
def GenomicRangeQuery(S, P, Q):
    result = []
    for i in range(len(P)):
        
        if ('A' in S[P[i]:Q[i]+1]):
            result.append(1)
        elif('C' in S[P[i]:Q[i]+1]):
            result.append(2)
        elif('G' in S[P[i]:Q[i]+1]):
            result.append(3)
        else:
            result.append(4)
    return result

print GenomicRangeQuery(S, P, Q)

print '----GenomicRangeQuery C#----'
#class Program
#    {
#        static void Main(string[] args)
#        {
#            string S = "CAGCCTA";
#            int[] P = new int[] { 2, 5, 0 };
#            int[] Q = new int[] { 4, 5, 6 };
#
#            //Console.WriteLine(MaxCounters(N, A).ToString());
#            Console.WriteLine("{0}", string.Join(", ", GenomicRangeQuery(S, P, Q)));
#            Console.ReadLine();
#        }
#
#        public static int[] GenomicRangeQuery(string S, int[] P, int[] Q)
#        {
#            List<int> test_list = new List<int>();
#            for (int i = 0; i < P.Length; i++) 
#            {
#                string s = S.Substring(P[i], Math.Abs(P[i] - Q[i])+1);//razlikuje se od pythona pošto slice tamo radi sa drugim parametrom koji je index a ovde je duzina substringa
#                //if (S.Substring(P[i], S.Length - Q[i]).Contains('A'))
#                if(s.Contains('A'))
#                {
#                    test_list.Add(1);
#                }
#                else if (s.Contains('C'))
#                {
#                    test_list.Add(2);
#                }
#                else if (s.Contains('G'))
#                {
#                    test_list.Add(3);
#                }
#                else
#                {
#                    test_list.Add(4);
#                }
#                
#            }
#            return test_list.ToArray();
#
#        }
#    }