inp = open("nykysuomensanalista2024.txt", 'r').readlines()
out = []

for w in inp:
	w, _ = w.split('\t', 1)
	w = w.replace('š', 'sh').replace('’', '').replace('ž', 'z').replace('ô', 'o')
	if len(w) < 3 or len(w) > 10:
		continue;
	fail = False
	for c in w:
		if (c < 'a' or c > 'z') and c != 'å' and c != 'ä' and c != 'ö':
			if (c != '‑' and c != '-' and c != ' '):
				print(f"HYLÄTTY: '{w}' koska sisälsi: {c}")
			fail = True
			break

	if fail:
		continue

	#print(w)
	out.append(w + " ")

open("sanat.txt", 'w').writelines(out)