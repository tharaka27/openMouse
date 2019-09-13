#ifndef FLOOD_H_
#define FLOOD_H_

/*
   Written by : Tharaka Sachintha Ratnayake
   Gmail : tharakasachintha27@gmail.com
*/

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <iostream>

#define NORTH 0
#define EAST 1
#define SOUTH 2
#define WEST 3
#define UNKNOWN 4
#define SIZE 14
#define STACK_MAX 3000


// int EAST = 1
// int SOUTH =  2
// int WEST = 3
// int  UNKNOWN = 4
// int SIZE = 16
// int STACK_MAX =  3000
/* 
define a structure that can hold data about a 
single cell 
*/
struct cell_info
{
    bool walls[4];
    bool visited;
};

/*
define a structure that call hold data about
all maze using cell info
*/
struct wall_maze
{
    struct cell_info cells[SIZE][SIZE];
    
};
//
struct dist_maze
{
    int distance[SIZE][SIZE];
};




struct path_maze
{
    bool maze[SIZE][SIZE];
};

/*
structure that can hold data about
the coordinate
*/
struct coor
{
    int x;
    int y;
};

/*
structure defined for flood fill algorithm
stack
*/
struct stack
{
    struct coor array[STACK_MAX];
    int index;
    
};


void init_path_maze(struct path_maze* pm);
void init_distance_maze(struct dist_maze* dm, struct coor* c, int center);
void init_wall_maze(struct wall_maze* wm);
void init_coor(struct coor* c, int x, int y);
struct coor pop_stack(struct stack* s);
void push_stack(struct stack* s, struct coor c);
bool is_stack_empty(struct stack* s);
int UpdateAndNextMove(struct dist_maze* dm, struct wall_maze* wm, struct coor* c, struct stack* upst , int a);
int nextMove(struct dist_maze* dm, struct wall_maze* wm, struct coor* c);
void pushSurrounding(struct stack* s, struct coor* c , struct dist_maze* dm );
int minimumOpenNeighbor(struct dist_maze* dm, struct wall_maze* wm, struct coor* c);
int modified_floodfill(struct wall_maze* tm, struct dist_maze* dm, struct coor* c, struct wall_maze* wm, int a, int direction, struct stack* upst);
void print_distance_maze(struct dist_maze* dm);
void print_path_maze(struct path_maze* pm);
int return_floodfill(struct dist_maze* dm, struct coor* c, struct wall_maze* wm, int direction, struct path_maze* pm);


// bla
int minusOneNeighbor(struct dist_maze* dm, struct wall_maze* wm, struct coor* c, struct stack* s, int a);
int floodFill(struct dist_maze* dm, struct coor* c, struct wall_maze* wm, struct wall_maze* tm ,int a, int direction, struct stack* upst);


#endif