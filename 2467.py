n = int(input())
nums = list(map(int, input().split()))

l = 0
r = n - 1

answer = [nums[l], nums[r]]
while l < r:
    if abs(sum(answer)) > abs(nums[l] + nums[r]):
        answer = [nums[l], nums[r]]
    if nums[l] + nums[r] < 0:
        l += 1
    else:
        r -= 1

print(*answer)
