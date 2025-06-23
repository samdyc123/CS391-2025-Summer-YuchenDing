/* ****** TASK1 ****** */

#include "runtime.h"

/* ****** ****** */

extern
void*
mymalloc(size_t n) {
  void* p0;
  p0 = malloc(n);
  if (p0 != 0) return p0;
  fprintf(stderr, "myalloc failed!!!\n");
  exit(1);
}

/* ****** ****** */

extern
lamval1
LAMVAL_print(lamval1 x)
{
  int tag;
  tag = x->tag;
  switch( tag )
  {
    case TAGcfp:
      printf("<lamval1_cfp>"); break;
    case TAGint:
      printf("%i", ((lamval1_int)x)->data); break;
    case TAGstr:
      printf("%s", ((lamval1_str)x)->data); break;
    default: printf("Unrecognized tag = %i", tag);
  }
  return x;
}

/* ****** ****** */

/*
fun f91(x: int): int =
  if x > 100 then x-10 else f91(f91(x+11))
*/

/* ****** ****** */

extern
lamval1
f91(lamval1 x)
{

  lamval1 ret0;
  lamval1 tmp1, tmp2, tmp3, tmp4;

  tmp1 = LAMOPR_igt(x, LAMVAL_int(100));

  if (((lamval1_int)tmp1)->data) {
    ret0 = LAMOPR_sub(x, LAMVAL_int(10));
  } else {
    tmp2 = LAMOPR_add(x, LAMVAL_int(11));
    tmp3 = f91(tmp2);
    tmp4 = f91(tmp3);
    ret0 = tmp4;
  }

  return ret0;
}

int main() {
  LAMVAL_print(f91(LAMVAL_int(1))); printf("\n");
  LAMVAL_print(f91(LAMVAL_int(50))); printf("\n"); 
  LAMVAL_print(f91(LAMVAL_int(110))); printf("\n");
  return 0;
}