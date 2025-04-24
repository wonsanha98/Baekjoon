# 자르는 위치 값을 정렬 -> 최대 간격 찾기 -> 최대 면적 계산


width_max, height_max = (input().split())
width_max = int(width_max)
height_max = int(height_max)

width_cut = []
height_cut = []

test = int(input())
for i in range(test):
    cut = list(map(int, input().split()))

    # 자르기가 가로인지 세로인지 정해서 값을 가로, 세로 컷에 넣는다.

    if cut[0] == 0:
        height_cut.append(cut[1])
    else:
        width_cut.append(cut[1])

width_cut.sort()
height_cut.sort()

width = []
height = []

if len(width_cut) != 0:
    last = 0
    for i in width_cut:
        width.append(i - last)
        last = i
    width.append(width_max - width_cut[-1])
else:       # 자른 값이 없으면 최대 값을 넣어준다.
    width.append(width_max) 

if len(height_cut) != 0:
    last = 0
    for i in height_cut:
        height.append(i - last)
        last = i
    height.append(height_max - height_cut[-1])
else:       # 자른 값이 없으면 최대 값을 넣어준다.
    height.append(height_max)

width.sort()
height.sort()
 
if len(width) != 0 and len(height) != 0:
    print(width[-1] * height[-1])
elif len(width) == 0:
    print(height[-1])
else:
    print(width[-1])