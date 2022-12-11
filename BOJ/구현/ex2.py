def solution(n, words):
    answer = []

    fail = False
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            num = (i % n) + 1
            turn = (i // n) + 1
            fail = True
            break

        if words[i] in words[:i]:
            num = (i % n) + 1
            turn = (i // n) + 1
            fail = True
            break

    if fail == False:
        num, turn = 0, 0

    answer = [num, turn]
    return answer


# ans = solution(
#     5,
#     [
#         "hello",
#         "observe",
#         "effect",
#         "take",
#         "either",
#         "recognize",
#         "encourage",
#         "ensure",
#         "establish",
#         "hang",
#         "gather",
#         "refer",
#         "reference",
#         "estimate",
#         "executive",
#     ],
# )

# ans = solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])

ans = solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
print(ans)
