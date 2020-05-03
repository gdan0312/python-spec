# Практическое задание по регулярным выражениям


def calculate(data, findall):
    matches = findall(r'([a-c])([+-]?)=([a-c]?)([+-]?\d{,3})')
    for v1, sign, v2, n in matches:
        right = data.get(v2, 0) + int(n or 0)
        if sign == '-':
            data[v1] -= right
        elif sign == '+':
            data[v1] += right
        else:
            data[v1] = right
    return data
