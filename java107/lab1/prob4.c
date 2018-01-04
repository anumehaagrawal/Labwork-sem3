
#include <stdio.h>
int main()
{
    int a[10][10], b[10][10], result[10][10], r1, c1, r2, c2, i, j, k;

    printf("Enter rows and column for first matrix: ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and column for second matrix: ");
    scanf("%d %d",&r2, &c2);
    if(c1 != r2)
    {
        printf("Error! column of first matrix not equal to row of second.\n\n");
      }
    printf("\nEnter elements of matrix 1:\n");
    for(i=0; i<r1; ++i)
        for(j=0; j<c1; ++j)
        {
            scanf("%d", &a[i][j]);
        }

    printf("\nEnter elements of matrix 2:\n");
    for(i=0; i<r2; ++i)
        for(j=0; j<c2; ++j)     
        {
            scanf("%d",&b[i][j]);
        }
    for(i=0; i<r1; ++i)
        for(j=0; j<c2; ++j)
        {
            result[i][j] = 0;
        }
    for(i=0; i<r1; ++i)
        for(j=0; j<c2; ++j)
            for(k=0; k<c1; ++k)
            {
                result[i][j]+=a[i][k]*b[k][j];
            }
    printf("\nOutput Matrix:\n");
    for(i=0; i<r1; ++i)
        for(j=0; j<c2; ++j)
        {
            printf("%d  ", result[i][j]);
            if(j == c2-1)
                printf("\n\n");
        }
   
}