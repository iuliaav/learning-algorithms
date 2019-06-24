n = int(input())

text = {
    0: "I love",
    1: "I hate"
}
result = " that ".join([text[i%2] for i in range(1, n+1)])

result.strip()
result += " it"

print(result)
