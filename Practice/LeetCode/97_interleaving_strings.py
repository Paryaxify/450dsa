def isInterleaving(s1: str, s2: str, s3: str) -> bool:
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)

    # check whether the length of s3 is comparable to s1 and s2 or not
    if l1 + l2 != l3:
        return False

    queue = [(0, 0)]
    visited = set((0, 0))

    while queue:
        s1_index, s2_index = queue.pop(0)
        if s1_index + s2_index == l3:
            return True
        if s1_index + 1 <= l1 and s1[s1_index] == s3[s1_index + s2_index] and (s1_index + 1, s2_index) not in visited:
            queue.append((s1_index + 1, s2_index))
            visited.add((s1_index + 1, s2_index))
        if s2_index + 1 <= l2 and s2[s2_index] == s3[s1_index + s2_index] and (s1_index, s2_index + 1) not in visited:
            queue.append((s1_index, s2_index + 1))
            visited.add((s1_index, s2_index + 1))

    return False


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print(isInterleaving(s1, s2, s3))
