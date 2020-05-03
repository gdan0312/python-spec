# Практическое задание по регулярным выражениям


def calculate(data, findall):
    matches = findall(r'([a-c])([+-]?)=([a-c]?)([+-]?\d{,3})')
    for v1, sign, v2, n in matches:
        if sign == '-':
            data[v1] = data[v1] - data.get(v2, 0) - int(n or 0)
        elif sign == '+':
            data[v1] = data[v1] + data.get(v2, 0) + int(n or 0)
        else:
            data[v1] = data.get(v2, 0) + int(n or 0)
    return data
