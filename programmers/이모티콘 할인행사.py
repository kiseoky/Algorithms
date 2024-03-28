def solution(users, emoticons):
    answer = [0, 0]
    m = len(emoticons)
    rate_cases = []

    def make_rates(k, rates):
        if k == m - 1:
            rate_cases.append(rates)
            return

        for rate in [40, 30, 20, 10]:
            make_rates(k + 1, rates + [rate])

    make_rates(-1, [])
    for rates in rate_cases:
        result = [0, 0]
        for user in users:
            spend = 0
            for i, rate in enumerate(rates):
                if rate >= user[0]:
                    price = emoticons[i] // 100 * (100 - rate)
                    spend += price

            if spend >= user[1]:
                result[0] += 1
            else:
                result[1] += spend

        answer = max(answer, result)
    return answer