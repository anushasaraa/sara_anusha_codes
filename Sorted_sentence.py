def solve():
    s = input().strip()
    words = s.split()
    result = [""] * len(words)

    for word in words:
        for ch in word:
            if ch.isdigit():
                pos = int(ch) - 1
                result[pos] = word.replace(ch, "")
                break

    print(" ".join(result))

if __name__ == "__main__":
    solve()
