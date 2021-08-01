#!/bin/bash

# @brief: print tikz-requirements
# @detail: This script checks whether a given file contains a line like `tikz-requirements: digides_drawings` and returns the value specified for summary-type via stderr.
#          If no such line can be found, the error code -1 will be printed to stdout, otherwise it will be 0
# @TODO: exiting does not work. exit status is always -1

cat /dev/stdin | while read line
do
	if [ "$line" == *"---"* ] || [ "$line" == *"..."* ]; then
		break
	elif [[ "$line" == *"tikz-requirements:"* ]]; then
		value="$(echo $line | cut -d ":" -f2 | xargs)" # only take part of line after the colon and trim it
		printf "%s" "$value" > /dev/stdout
		exit 0
	fi
done

exit 1
