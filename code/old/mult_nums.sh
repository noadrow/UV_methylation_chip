paste $1 $2 |    awk '{l = (match($1,/[.][[:digit:]]+/) > 0) ? RLENGTH-1 : 0;
  printf "%.*f\n", l, ($1 * $2)
}' > mult_sim_illum.txt
