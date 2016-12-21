#!/bin/sh

# for FILE in *; do
find . -type f | while read FILE
  if [ ${FILE}]
    bzip2 -d "${FILE}"
done
