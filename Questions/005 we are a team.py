"""

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;


class UnionFindeSet {
private:
    vector<long long> fa;
    int count;

public:
    UnionFindeSet(long long n) {
        fa.resize(n);
        for (long long i = 0; i < n;i++)
            fa[i] = i;
        count = 0;
    }

    long long find(long long x) {
        if (x != fa[x]) {
            fa[x] = find(fa[x]);
            return fa[x];
        }
        return x;
    }

    void Union(long long x, long long y) {
        int x_fa = find(x);
        int y_fa = find(y);
        if (x_fa != y_fa) {
            fa[y_fa] = x_fa;
            count--;
        }

    }

};


int main() {
    long long n, m;
    cin >> n >> m;
    long long a, b, c;
    UnionFindeSet ufs(n + 2);
    for (long long i = 0; i < m; i++) {
        cin >> a >> b >> c;
        if (a<1 || a>n || b<1 || b>n) {
            cout << "da pian z" << endl;
        }
        else if (c == 0) {
            ufs.Union(a, b);
        }
        else if (c == 1) {
            int a_fa = ufs.find(a);
            int b_fa = ufs.find(b);
            if (a_fa != b_fa)
                cout << "we are not a team" << endl;
            else
                cout << "we are a team" << endl;
        }
        else {
            cout << "da pian z" << endl;
        }
    }

    return 0;
}

"""