def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines): #傳進清單lines
	new = []
	傅胖胖_word_count = 0
	悅_word_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0][ :5]
		name = s[0][5:]
		if name == '傅胖胖':
			for m in s[1:]:
				傅胖胖_word_count += len(m)
			new.append(time + ' ' + name + ':' + m)

		elif name == '悅':
			for m in s[1:]:
				悅_word_count += len(m)
			new.append(time + ' ' + name + ':' + m)

		else :
			day = s[0][ :10]
			date = s[0][10:]
			new.append(day + ' ' + date)

	return new

def write_file(filename, new):
	with open(filename, 'w') as f:
		for m in new:
			f.write(m + '\n')

def main():
	lines = read_file('[LINE]傅胖胖.txt')
	new = convert(lines) # 覆蓋之前的lines值
	write_file('outputlineee.txt', new)

main() #進入點
	