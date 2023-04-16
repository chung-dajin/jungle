N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
def divide(x, y, N) :
    global blue, white
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] : 
                divide(x, y, N//2)    
                divide(x+N//2, y, N//2)
                divide(x, y+N//2, N//2)
                divide(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        white += 1
    else :
        blue += 1
divide(0, 0, N)
print(white)
print(blue)