def NumsTransform(path_nums):
	with open(path_nums) as f:
		nums = f.readlines()
		numbers = [int(num) for num in nums]
		numbers.sort()
		median = len(numbers) // 2
	print(sum(abs(n - numbers[median]) for n in numbers))

path_nums = input('Путь до файла nums: ')
NumsTransform(path_nums)