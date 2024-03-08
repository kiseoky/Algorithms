# 코드가 난장판이지만 풀었다.
# 코테 당시에는 몰랐는데 3번보다 4, 5번이 더 풀만했던 것 같다. 순서대로 풀어야겠다고 생각했었는데 그러지 말아야지

# 틀렸던 부분: 버린 카드 더미에서 카드를 뽑은 후 set에서 지워주지 않아 테스트코드 2개를 계속 틀렸었다.
def solution(coin, cards):
    answer = 0
    n = len(cards)
    hand_set = set()
    discard_set = set()
    life = 0

    def add(cards):
        nonlocal coin, life
        for card in cards:
            pair = n + 1 - card
            if coin >= 1 and pair in hand_set:
                coin -= 1
                life += 1
                hand_set.remove(pair)
            else:
                discard_set.add(card)

    def get_from_discard():
        nonlocal coin, life
        for card in discard_set:
            pair = n + 1 - card
            if coin >= 2 and pair in discard_set:
                coin -= 2
                life += 1
                discard_set.remove(pair)
                discard_set.remove(card)
                return

    for card in cards[:n // 3]:
        pair = n + 1 - card
        if pair in hand_set:
            life += 1
        hand_set.add(card)

    for idx in range(n // 3, n, 2):
        nxt_cards = cards[idx:idx + 2]
        add(nxt_cards)
        life -= 1

        if coin >= 2 and life < 0:
            get_from_discard()
        if life < 0:
            break

        answer += 1

    return answer + 1
