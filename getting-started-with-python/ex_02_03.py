xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
#input이 반환하는 것은 문자열
#문자열 * 문자열을 하면 에러가 발생하기 때문에 숫자로 형변환 필요
xp = float(xh) * float(xr)
print("Pay:", xp)