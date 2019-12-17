#!/bin/bash

rm ./output/comp_readable.txt
touch ./output/comp_readable.txt
valueTempHome="$(sed -n '6p' setup_file.txt)"
valueTempOrg="$(sed -n '9p' setup_file.txt)"

grep -B1 "SCHEDULED" $valueTempOrg >> comp_readable.txt
