#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

struct Geometry;

#define SCANF_FMT_CIRCLE    "%f %f %f"
#define SCANF_FMT_RECTANGLE "%f %f %f %f"
#define SCANF_FMT_SQUARE    "%f %f %f"
#define SCANF_FMT_LINE      "%f %f %f %f"


#define PRINTF_FMT_CIRCLE    "Circle with center at %f, %f and radius %f "
#define PRINTF_FMT_RECTANGLE "Rectangle with corner at (%f, %f) with width %f and height %f "
#define PRINTF_FMT_SQUARE    "Square with corner at (%f, %f) and side %f "
#define PRINTF_FMT_LINE      "Line from (%f, %f) to (%f, %f) "


void initRectangle(struct Geometry **object){
    // string name;
    // name = object;
    float v1,v2,v3,v4;
    scanf(SCANF_FMT_RECTANGLE,&v1,&v2,&v3,&v4);
    printf(PRINTF_FMT_RECTANGLE,v1,v2,v3,v4);
};
void initSquare(struct Geometry **object){
    float v1,v2,v3;
    scanf(SCANF_FMT_SQUARE,&v1,&v2,&v3);
    printf(PRINTF_FMT_SQUARE,v1,v2,v3);
};
void initCircle(struct Geometry **object){
    float v1,v2,v3;
    scanf(SCANF_FMT_CIRCLE,&v1,&v2,&v3);
    printf(PRINTF_FMT_CIRCLE,v1,v2,v3);
};
void initLine(struct Geometry **object){
    float v1,v2,v3,v4;
    scanf(SCANF_FMT_LINE,&v1,&v2,&v3,&v4);
    printf(PRINTF_FMT_LINE,v1,v2,v3,v4);
};

// void printGeometry(struct Geometry* object){
//     printf("hello world %f ", object->v1);
//     // PRINTF_FMT_SQUARE
//     // if(!strcmp(object, "Rectangle")){
//     //     printf(" Hello Type checked " );
//     // }
// };

void freeGeometry(struct Geometry* object){
    free(object);
};


int main()
{
  int n;
  struct Geometry **object;
  scanf("%d", &n);
  printf("%d geometric items ", n);

  object = malloc(sizeof(struct Geometry*)*n);

  for(int i = 0; i < n; i++)
  {
    char objectType[40];
    scanf("%s", objectType);
    if(!strcmp(objectType, "Rectangle"))
    {
      initRectangle(&object[i]);
    }
    else if (!strcmp(objectType, "Square"))
    {
      initSquare(&object[i]);
    }
    else if(!strcmp(objectType, "Circle"))
    {
      initCircle(&object[i]);
    }
    else if(!strcmp(objectType, "Line"))
    {
      initLine(&object[i]);
    }
    else
    {
      printf("Unknown geometric type %s\n", objectType);
      exit(1);
    }

  }
  
//   for(int i = 0; i < n; i++)
//   {
//     printGeometry(object[i]);
//   }
  
  for(int i = 0; i < n; i++)
  {
    freeGeometry(object[i]);
  }

  free(object);
}