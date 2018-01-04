#include<stdio.h>
 
int main() {
   FILE *fp1, *fp2;
   char ch1, ch2;
   char fname1[40], fname2[40];
 
   printf("Enter name of first file :");
   gets(fname1);
 
   printf("Enter name of second file:");
   gets(fname2);
 
   fp1 = fopen(fname1, "r");
   fp2 = fopen(fname2, "r");
 
   if (fp1 == NULL) {
      printf("Cannot open %s for reading ", fname1);
      exit(1);
   } else if (fp2 == NULL) {
      printf("Cannot open %s for reading ", fname2);
      exit(1);
   } else {
      ch1 = getc(fp1);
      ch2 = getc(fp2);
 
      while ((ch1 != EOF) && (ch2 != EOF) && (ch1 == ch2)) {
         ch1 = getc(fp1);
         ch2 = getc(fp2);
      
 }
      if (ch1 == ch2)
         printf("Files are identical n");
      else if (ch1 != ch2)
         printf("Files are Not identical n");
 
      fclose(fp1);
      fclose(fp2);
   }
   
}