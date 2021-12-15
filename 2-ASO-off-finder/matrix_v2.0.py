from comf import *
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


def find_match(aso, genome, allowed_difference):
	fragment_length = int(round(len(aso) / (allowed_difference+1)))
	frag_list = []
	match_result = []
	for i in range(allowed_difference+1):
		start = i * fragment_length
		end = min((i+1)*fragment_length, len(aso))

		frag_list.append(aso[start:end])

	index_result = []
	for fragment in frag_list:
		index = -1
		while True:
			index = genome.find(fragment, index+1)
			if index == -1:
				break
			index_result.append(index)

	if len(index_result) == 0:
		return match_result

	for index_hit in index_result:
		start = max(0, index_hit-len(aso))
		end = min(len(genome), index_hit+len(aso))
		genome = genome[start:end]

		# Create distance matrix
		D = []
		T = []
		for i in range(len(aso)+1):
			D.append([0]*(len(genome)+1))
	
		# Fill in the first column of the matrix
		for i in range(len(aso)+1):
			D[i][0] = i

		for i in range(len(aso)+1):
			sub_T = []
			for j in range(len(genome)+1):
				sub_T.append('0')
			T.append(sub_T)

		for j in range(1, len(genome)+1):
			T[0][j] = 'left'
		for i in range(1, len(aso)+1):
			T[i][0] = 'up'

		T[0][0] = 'done'

		# Fill in the rest of the matrix
		for i in range(1, len(aso)+1): # First row/column already filled, start from 1
			for j in range(1, len(genome)+1):
				matrix_left = D[i][j-1] + 1
				matrix_above = D[i-1][j] + 1
			
				if aso[i-1] == genome[j-1]: # If ASO and genome sequence is same
					matrix_diagonal = D[i-1][j-1] # Do not add 1
				else: # If ASO and genome sequence is different
					matrix_diagonal = D[i-1][j-1] + 1 # Add 1
			
				# Acquire minimum distance from 3 positions
				D[i][j] = min(matrix_left, matrix_above, matrix_diagonal)

				if D[i][j] == matrix_left:
					T[i][j] = 'left'
				elif D[i][j] == matrix_above:
					T[i][j] = 'up'
				else:
					T[i][j] = 'diag'

		for position in range(len(D[-1])):
			distance = D[-1][position]
			allowed_difference = min(min(D[-1]), allowed_difference)
			if distance > allowed_difference:
				continue

			xseq = []
			yseq = []
			i = len(aso)
			j = position

			while (i > 0 or j > 0):
				if T[i][j] == 'diag':
					xseq.append(aso[i-1])
					yseq.append(genome[j-1])
					i = i - 1
					j = j - 1
				elif T[i][j] == 'left':
					xseq.append('-')
					yseq.append(genome[j-1])
					j = j - 1
				elif T[i][j] == 'up':
					xseq.append(aso[i-1])
					yseq.append('-')
					i = i - 1
				elif T[i][j] == 'done':
					break

			x = ''.join(xseq[::-1])
			y = ''.join(yseq[::-1])

			match_result.append((x,y))

	return match_result


p = 'GTTTGGGGCCGGCCCAGGCCT'
rna = mkdic('old_splice.fasta')

output = open('aso_result8.txt','w')

with ProcessPoolExecutor(max_workers=40) as pool:
	jobs = []
	D_job = {}
	for key, value in rna.items():
		value = value.upper()
		if len(value) < len(p):
			continue
		result = pool.submit(find_match, p, value, 2)
		jobs.append(result)
		D_job[result] = key

	for job in as_completed(jobs):
		match_result = job.result()
		origin = D_job[job].split('|')[0]

		for alignment in match_result:
			x = alignment[0]
			y = alignment[1]
			output.write('%s\n%s\n%s\n' % (origin, x, y))

		jobs.remove(job)
		del D_job[job]
