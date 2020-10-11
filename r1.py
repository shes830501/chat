def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='UTF-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Yuan':
			person = 'Yuan'
			continue # 不執行以下程式 直接跳往下一迴圈
		if line == '宣雨':
			person = '宣雨'
			continue # 不執行以下程式 直接跳往下一迴圈
		if person: # person is value
			new.append(person + ':' + line )
	return new

def write_file(filename, lines):
	with open(filename , 'w') as f:
		for line in lines:
			f.write(line + '\n')
def main():
	lines = read_file('input.txt')
	lines = convert(lines) # 覆蓋之前的lines值
	write_file('output.txt', lines)

main()