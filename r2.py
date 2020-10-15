def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='UTF-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	范振倬_word_count = 0
	范振倬_sticker_count = 0
	范振倬_photo_count = 0
	范振倬_video_count =0
	悅_word_count = 0
	悅_sticker_count = 0
	悅_photo_count = 0
	悅_video_count = 0
	for line in lines:
		s = line.split(' ')
		# print(s)
		if s[1] == '范振倬':
			if s[2] == 'Stickers':
				范振倬_sticker_count += 1
			elif s[2] == 'videos':
				范振倬_video_count += 1
			elif s[2] == 'Photos':
				范振倬_photo_count += 1
			else:
				for m in s[2:]:
					范振倬_word_count += len(m)
		elif s[1] == '悅':
			if s[2] == 'Stickers':
				悅_sticker_count += 1
			elif s[2] == 'videos':
				悅_video_count += 1
			elif s[2] == 'Photos':
				悅_photo_count += 1
			else:
				for m in s[2:]:
					悅_word_count += len(m)
	print('范振倬說了',范振倬_word_count, '個字')
	print('范振倬傳了',范振倬_sticker_count, '張貼圖')
	print('范振倬傳了',范振倬_video_count, '部影片')
	print('范振倬傳了',范振倬_photo_count, '張圖片')

	print('悅說了',悅_word_count, '個字')
	print('悅傳了',悅_sticker_count, '張貼圖')
	print('悅傳了',悅_video_count, '部影片')
	print('悅傳了',悅_photo_count, '張圖片')

	return lines

def write_file(filename, lines):
	with open(filename , 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]范振倬.txt')
	lines = convert(lines) # 覆蓋之前的lines值
	write_file('outputline.txt', lines)


main()