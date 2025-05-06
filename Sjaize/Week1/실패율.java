import java.util.stream.IntStream;
import java.util.Comparator;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] numPerson = new int[N+2];
        
        for (int person = 0; person < stages.length; person++) {
            int stage = stages[person];
            numPerson[stage]++;
        }
        
        double[] rates = new double[N+2];
        int total_person = stages.length;
        int eliminated = 0;
        
        for (int stage = 1; stage < N+1; stage++) {
            rates[stage] = (double) numPerson[stage] / (total_person - eliminated);
            eliminated = eliminated + numPerson[stage];
            if (eliminated == total_person) {
                break;
            }
        }
        
        return IntStream.range(1, N+1)
                        .boxed()
                        .sorted((a, b) -> Double.compare(rates[b], rates[a]))
                        .mapToInt(i -> i)
                        .toArray();
    }
}
