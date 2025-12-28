prefix = """const validWords = `"""
suffix = """`.toUpperCase().split(" ");"""

with open("sanat.js", 'r') as f:
	inp = f.readlines()[0]
inp = inp.strip().removeprefix(prefix).removesuffix(suffix).split(' ')
inp = sorted(inp, key=len)
accepted = set()

def is_compound(w):
	for i in range(3, len(w)+1):
		#print(i, w, w[0:i])
		if w[0:i] in accepted:
			#print('FOUND', w[0:i], 'among', accepted, i, len(w))
			if i == len(w):
				return True
			if i + 3 <= len(w):
				if is_compound(w[i:]):
					return True
	return False

out = []
for w in inp:
	if is_compound(w):
		print(f"discarding {w}")
		continue
		
	accepted.add(w)
	print(f"accepted: {w}!")
	out.append(w)

out = sorted(out)

open("sanat_2.js", 'w').write(prefix + " ".join(out) + suffix)