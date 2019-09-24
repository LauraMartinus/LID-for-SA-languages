import subprocess
import argparse


def language_id(input_file, output_file=0):
	if output_file == 0:
		subprocess.call(["fastText/fasttext","test","langdetect.bin",input_file,"1"])
	else:
		with open(output_file, 'w') as f:
			subprocess.call(["fastText/fasttext","predict","langdetect.bin",input_file,"1"], stdout=f)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input", 
						help="input file containing sentences to be detected")
	parser.add_argument("--output", 
						help="output file to write detected ids to")
	args = parser.parse_args()

	if args.output:
		language_id(args.input,args.output)
	else:
		language_id(args.input)