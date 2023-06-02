def solution(n):
	#// n까지 뛰는 방법을 차례대로 저장하기 위한 배열을 선언한다. 
 #   // n=1인 경우 dp[1]에서 런타임 에러가 날 것이므로 필요한 배열보다 1칸 더 선언해 줬다.
    dp = [0] * (n+1)
 #   // 2칸까지는 직접 계산한 값을 미리 넣어준다.
    dp[0] = 1
    dp[1] = 2
    
 #   //dp 을 차례로 채워넣는다.
    for i in range(2,n):
        dp[i] = dp[i-2] + dp[i-1]
	
 #   // 정답은 실제 개수를 1234567로 나눈 나머지 값이므로
    return dp[n-1] % 1234567



# -------------
# 2023.06.02 다시 풀어봤는데 깔끔하게 풀림

def solution(n):
    dp=[]
    dp.append(1);dp.append(2)
    for i in range(1, n+1):
        dp.append(dp[i]+dp[i-1])
       # print("dp:",dp)


    return dp[n-1]%1234567
