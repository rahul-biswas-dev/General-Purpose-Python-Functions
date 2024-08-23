def convert_binary(n):
	if n > 1:
		convert_binary(n // 2)
	print(n % 2, end = "")


a = int(input("enter number:"))
convert_binary(a)

print(f" is the binary of given number:-{a}")