from comf import *
import re
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


def find_match(aso, genome, allowed_difference):
	fragment_length = int(round(len(aso) / (allowed_difference+1)))
	frag_list = []
	match_result = dict()
	for i in range(allowed_difference+1):
		start = i * fragment_length
		end = min((i+1)*fragment_length, len(aso))

		frag_list.append(aso[start:end])

	index_result = {}
	order = 0
	for fragment in frag_list:
		query = re.finditer(fragment, genome)
		if query == -1:
			continue
		index_result[order] = query

	if len(index_result) == 0:
		return match_result

	for index_hit in index_result:
		start = max(0, index_hit-len(aso))
		end = min(len(genome), index_hit+len(aso))
		genome = genome[start:end]

		# Create distance matrix
		D = []
		for i in range(len(aso)+1):
			D.append([0]*(len(genome)+1))
	
		# Fill in the first column of the matrix
		for i in range(len(aso)+1):
			D[i][0] = i

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

		# Count number of matches with less than allowed indel, mismatch
		for distance in D[-1]: # Final line of matrix containing distance
			if distance > allowed_difference:
				continue
			
			if distance not in match_result:
				match_result[distance] = 0 # Add key for distance

			match_result[distance] += 1 # Add 1 to count

	return match_result
			
p = 'GTTTGGGGCCGGCCCAGGCCT'
rna = mkdic('old_splice.fasta')

output = open('aso_result5.txt','w')

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

		for key, value in match_result.items():
			output.write('%s\t%s\t%s\n' % (origin, key, value))

		jobs.remove(job)
		del D_job[job]
