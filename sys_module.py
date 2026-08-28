import sys

print("실행 파일명 : ",sys.argv[0])
for i, arg in eumerate(sys.argv[1:], start = 1):
    print("인자", i, ":", arg)
sys.exit(0)

for i in range(1,10000000000):
    print("exit() 함수로 인해 살행되지 않음")
