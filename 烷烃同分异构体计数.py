# 利用生成函数、Burnside引理和Polya枚举理论计算烷基和烷烃的异构体数量，而不考虑立体化学。
# 烷基的生成函数为：A(x) = 1 + A_1 x + A_2 x^2 + A_3 x^3 + ...,
# 其中A_ m是具有m个碳的烷基异构体的量。
# 基于Polya理论，A(x) = 1 + x * [A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3)] / 6 .
# 使用 A_1, A_2, ..., A_m，我们可以算出A_(m + 1) .
# 对于具有一个索引碳原子的烷烃，
# P(x) = P_1 x + P_2 x^2 + P_3 x^3 + ... ,
# P(x) = x * [A(x)^4 + 6*A(x)^2*A(x^2) + 3*A(x^2)^2 + 8*A(x)*A(x^3) + 6A(x^4)] / 24 .
# 对于具有一个指数碳-碳键的烷烃，
# Q(x) = Q_1 x + Q_2 x^2 + Q_3 x^3 + ... ,
# Q(x) = [A(x)^2 + A(x^2)] / 2 - A(x) .
# 最后，对于烷烃，
# C(x) = C_1 x + C_2 x^2 + C_3 x^3 + ... ,
# C(x) = P(x) - Q(x) + A(x^2) - 1 .

#############################################################################
#  The original text:                                                       #
#  Using the generating function, Burnside's lemma and Polya's enumeration  #
#  theory to compute the amount of isomers for alkyl and alkane without     #
#  considering stereochemistry.                                             #
#                                                                           #
#  The generating function for alkyl is:                                    #
#  A(x) = 1 + A_1 x + A_2 x^2 + A_3 x^3 + ... ,                             #
#  in which A_m is the amount of alkyl isomers with m carbons.              #
#  Based on Polya's theory,                                                 #
#  A(x) = 1 + x * [A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3)] / 6 .                 #
#  Using A_1, A_2, ..., A_m, we can figure out A_(m + 1) .                  #
#                                                                           #
#  For alkane with one indexed carbon atom,                                 #
#  P(x) = P_1 x + P_2 x^2 + P_3 x^3 + ... ,                                 #
#  and we have:                                                             #
#  P(x) = x * [A(x)^4 + 6*A(x)^2*A(x^2) + 3*A(x^2)^2 + 8*A(x)*A(x^3)        #
#              + 6A(x^4)] / 24 .                                            #
#  For alkane with one indexed carbon-carbon bond,                          #
#  Q(x) = Q_1 x + Q_2 x^2 + Q_3 x^3 + ... ,                                 #
#  and we have:                                                             #
#  Q(x) = [A(x)^2 + A(x^2)] / 2 - A(x) .                                    #
#  Finally, for alkane,                                                     #
#  C(x) = C_1 x + C_2 x^2 + C_3 x^3 + ... ,                                 #
#  and we also have:                                                        #
#  C(x) = P(x) - Q(x) + A(x^2) - 1 .                                        #
#############################################################################

A = [1, ]
P = [0, ]
Q = [0, ]
C = [1, ]


def Calc_A_m(m: int) -> None:
    if len(A) > m: return
    if len(A) < m: Calc_A_m(m - 1)
    if len(A) == m:
        ans = 0
        # term 1: x * A(x)^3
        t = 0
        for i in range(m):
            for j in range(m - i):
                t += A[i] * A[j] * A[m - 1 - i - j]
        ans += t
        # term 2: x * 3 * A(x) * A(x^2)
        t = 0
        for j in range((m + 1) // 2):
            t += A[m - 1 - 2 * j] * A[j]
        ans += 3 * t
        # term 3: x * 2 * A(x^3)
        t = 0
        if not ((m - 1) % 3):
            t = A[(m - 1) // 3]
        ans += 2 * t
        # divided by 3!
        ans //= 6
        A.append(ans)
    return


def Calc_P_m(m: int) -> None:
    if len(P) > m: return
    if len(A) < m: Calc_A_m(m - 1)
    ans = 0
    # term 1: x * A(x)^4
    t = 0
    for i in range(m):
        for j in range(m - i):
            for k in range(m - i - j):
                t += A[i] * A[j] * A[k] * A[m - 1 - i - j - k]
    ans += t
    # term 2: x * 6 * A(x)^2 * A(x^2)
    t = 0
    for k in range((m + 1) // 2):
        for i in range(m - 2 * k):
            t += A[i] * A[m - 1 - i - 2 * k] * A[k]
    ans += 6 * t
    # term 3: x * 3 * A(x^2)^2
    t = 0
    if not ((m - 1) % 2):
        for i in range((m + 1) // 2):
            t += A[i] * A[(m - 1 - 2 * i) // 2]
    ans += 3 * t
    # term 4: x * 8 * A(x) * A(x^3)
    t = 0
    for j in range((m + 2) // 3):
        t += A[m - 1 - 3 * j] * A[j]
    ans += 8 * t
    #  term 5: x * 6 * A(x^4)
    t = 0
    if not ((m - 1) % 4):
        t = A[(m - 1) // 4]
    ans += 6 * t
    # divided by 4!
    ans //= 24
    for t in range(len(P), m): P.append(None)
    if len(P) == m: P.append(ans)
    else: P[m] = ans
    return


def Calc_Q_m(m: int) -> None:
    if len(Q) > m: return
    if len(A) <= m: Calc_A_m(m)
    if m == 1:
        Q.append(0)
        return
    ans = 0
    # term 1: A(x)^2
    t = 0
    for i in range(m + 1):
        t += A[i] * A[m - i]
    ans += t
    # term 2: A(x^2)
    t = 0
    if not (m % 2):
        t = A[m // 2]
    ans += t
    # divided by 2!
    ans //= 2
    # term 3: - A(x)
    ans -= A[m]
    for t in range(len(Q), m): Q.append(None)
    if len(Q) == m: Q.append(ans)
    else: Q[m] = ans
    return


def Calc_C_m(m: int) -> None:
    if len(A) <= m: Calc_A_m(m)
    if len(P) <= m: Calc_P_m(m)
    if len(Q) <= m: Calc_Q_m(m)
    if not (m % 2):
        ans = P[m] - Q[m] + A[m // 2]
    else:
        ans = P[m] - Q[m]
    for t in range(len(C), m): C.append(None)
    if len(C) == m: C.append(ans)
    else: C[m] = ans
    return


CALC_CARBON = 20
for num in range(1, CALC_CARBON + 1):
    Calc_A_m(num)
    Calc_P_m(num)
    Calc_Q_m(num)
    Calc_C_m(num)

print('CH%d-: %d' % (2 * 1 + 1, A[1]))
for num in range(2, CALC_CARBON + 1):
    print('C%dH%d-: %d' % (num, 2 * num + 1, A[num]))
print()
print('CH%d: %d' % (2 * 1 + 2, A[1]))
for num in range(2, CALC_CARBON + 1):
    print('C%dH%d: %d' % (num, 2 * num + 2, C[num]))


