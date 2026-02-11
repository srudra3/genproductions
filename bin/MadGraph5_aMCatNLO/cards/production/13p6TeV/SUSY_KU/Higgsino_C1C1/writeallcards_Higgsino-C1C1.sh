#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="Higgsino-C1C1"
PARTC1="_MC1-"
PARTN1="_MN1-"

### Create cards and SLHAs for all mass points

for MN2 in 101 126 151 176 201 226 251 276 301 326 351 376 401 426 451 476 501; do
    for DM in 2 3 5 6 7.5 10 15 20 25 30 40 50 60 70 80 90 100 120 140; do
        if (( $(echo "$DM >= $MN2" | bc -l) )); then
            continue
        fi

	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`	
	MC1=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
	MN2STR=${MN2/./p}
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODEL=${PROC}${PARTC1}${MC1STR}${PARTN1}${MN1STR}
	mkdir -p "${JOBS}/${MODEL}"
	cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
	sed "s/%MN2%/${MN2STR}/g;s/%MC1%/${MC1STR}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
	sed "s/%MN2%/${MN2}/g;s/%MN1%/${MN1}/g;s/%MC1%/${MC1}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
	sed "s/%MN2%/${MN2}/g;s/%MN1%/${MN1}/g;s/%MC1%/${MC1}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
    done
done
