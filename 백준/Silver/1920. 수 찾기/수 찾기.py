n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
nums1.sort()

for num in nums2:
    lt = 0
    rt = n - 1
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums1[mid] > num:
            rt = mid - 1
        elif nums1[mid] < num:
            lt = mid + 1
        else:
            print(1)
            break
    else:
        print(0)