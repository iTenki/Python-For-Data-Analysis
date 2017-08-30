def top_counts(count_dict, n = 10):
	value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:] # 列表切片，只有一行，起始值，到结束值前一位停止