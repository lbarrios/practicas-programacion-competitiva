#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
    int T; // 1 <= T <= 1000
    cin >> T;
    vector<int32_t> Xs; // Xi for i < N
    Xs.reserve(1 << 19); // aprox 500k
    vector<uint32_t> Xodds;
    Xodds.reserve(1 << 19);

    for (int t = 0; t < T; ++t) {
        uint32_t N;
        uint32_t O;
        int64_t D;
        // 2 ≤ N ≤ 5 × 10^5.
        // 0 ≤ O ≤ N.
        // -10^15 ≤ D ≤ 10^15.
        cin >> N >> O >> D;
        Xs.resize(N);
        //cout << N << " " << O << " " << D << endl;
        int32_t A, B, C, M;
        int32_t L;
        // 0 ≤ X1, X2, A, B, C ≤ 10^9.
        // 1 ≤ M ≤ 10^9.
        // L = 0 for small dataset, -5 × 10^8 ≤ L ≤ 0 for large dataset
        cin >> Xs[0] >> Xs[1] >> A >> B >> C >> M >> L;
        //cout << Xs[0] << " " << Xs[1] << " " << A << " " << B << " " << C << " " << M << " " << L << endl;

        Xodds.clear();
        if (L == 0) {
            for (uint32_t i = 2; i < N; ++i) {
                // Xi = (A × X(i-1) + B×X(i-2) + C) modulo M, for i = 3 to N.
                Xs[i] = (A * Xs[i - 1] + B * Xs[i - 2] + C) % M;
                if (Xs[i] % 1) {
                    Xodds.push_back(i);
                }
            }
        } else {
            for (uint32_t i = 2; i < N; ++i) {
                // Xi = (A × X(i-1) + B×X(i-2) + C) modulo M, for i = 3 to N.
                // Si = Xi + L.
                Xs[i] = ((((A * Xs[i - 1] + B * Xs[i - 2] + C) % M) + M) % M);
                //cout << "Xs[" << i << "]=" << Xs[i] << endl;
            }
        }

        if (L < 0) {
            for (uint32_t i = 0; i < N; ++i) {
                Xs[i] += L;
            }
        }
        /*
        cout << "Ss : [ ";
        for (uint32_t i = 0; i < N; ++i) {
            cout << Xs[i] << " ";
        }
        cout << "]" << endl;
        */

        int64_t sum = 0, max_sum = numeric_limits<int64_t>::min();
        size_t left_sum_index = 0, left_odd_index = 0;
        for (uint32_t i = 0; i < N; ++i) {
            sum += Xs[i];
            if (Xs[i] % 2) {
                //cout << "Xs[" << i << "] is odd" << endl;
                Xodds.push_back(i);
                if (Xodds.size() - left_odd_index > O) {
                    //cout << "maximum odds " << O << " at i: " << i << endl;
                    while (left_sum_index <= Xodds[left_odd_index]) {
                        sum -= Xs[left_sum_index];
                        left_sum_index++;
                    }
                    left_odd_index++;
                }
            }
            while (sum > D and left_sum_index < i) {
                sum -= Xs[left_sum_index];
                left_sum_index++;
            }
            if (sum <= D) {
                max_sum = max(sum, max_sum);
            }
            //cout << "sum " << sum << " max_sum " << max_sum << endl;
        }

        if (max_sum != numeric_limits<int64_t>::min()) {
            std::cout << "Case #" << t + 1 << ": " << max_sum << std::endl;
        } else {
            std::cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << std::endl;
        }

    }

    return 0;
}