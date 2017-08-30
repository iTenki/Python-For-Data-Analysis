from collections import defaultdict

def get_counts2(sequence):
	counts = defaultdict(int) # 所有值均会被初始化为
	for x in sequence:
		counts[x] += 1
		return counts
