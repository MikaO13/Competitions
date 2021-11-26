tv, tc, sv, ev = map(int, input().split())

print(abs(tc * 2 * (ev - sv) + tv * (ev - sv - 1)))