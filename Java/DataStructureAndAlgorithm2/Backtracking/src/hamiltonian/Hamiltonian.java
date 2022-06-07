package hamiltonian;

public class Hamiltonian {

    int n;   // 그래프 정점들의 개수
    int[] path;   // 해밀토니안 회로 내의 정점들을 저장하는 배열

    public static void main(String[] args) {

        Hamiltonian hamil = new Hamiltonian();

        hamil.path = new int[10];

        // 인접 행렬로 그래프 표현
        int[][] graph = {
                {0, 1, 1, 1},
                {1, 0, 1, 1},
                {1, 1, 0, 1},
                {1, 1, 1, 0}
        };

        hamil.n = 4;
        hamil.path[0] = 1;   // 시작 정점을 1로 설정

        // 해밀토니안 회로를 찾아 출력
        hamil.hamiltonian(graph, 0);

    }

    public void hamiltonian(int[][] graph, int i) {
        int j;

        if (valid(graph, i)) {
            if (i == n - 1) {   // 찾은 해밀토니안 회로 path[0, .. , n-1] 을 출력한다.
                System.out.print("찾은 해밀토니안 회로 : ");
                for (i = 0; i < n; i++) {
                    System.out.print(path[i] + " -> ");
                }
                System.out.println(path[0]);
                return;

            }
        } else {   // i 번째로 방문할 정점으로 시작 정점이 아닌 모든 정점을 시도
            for (j = 2; j <= n; j++) {
                path[i+1] = j;
                hamiltonian(graph, i+1);
            }

        }
    }

    // 경로상의 i 번째 정점이 유효한 선택인지 확인
    public boolean valid(int[][] graph, int i) {
        int j;

        // 마지막 정점이 첫 번째 정점과 인접하지 않은 경우
        if (i == n-1 && graph[path[n-1] - 1][path[0] - 1] == 0) {
            return false;
        // i 번째 정점이 i-1 번째 정점과 인접하지 않은 경우
        } else if (i > 0 && graph[path[i-1] - 1][path[i] - 1] == 0) {
            return false;
        } else {   // i 번째 정점이 이미 선택되었는지 확인
            j = 1;
            while (j < i) {
                if (path[i] == path[j]) return false;
                j++;
            }

        }
        return true;
    }
}
