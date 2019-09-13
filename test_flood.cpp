#include<stdio.h>
#include<iostream>
#include "flood.h"


using namespace std;
int main()
{



freopen("results.txt", "w", stdout);

struct wall_maze wm;
struct wall_maze tm;
struct dist_maze dm;
struct dist_maze rm;

struct path_maze pm;

struct coor xy;
struct stack st;



init_distance_maze(&dm, &xy, 1);



init_wall_maze(&wm);
init_wall_maze(&tm);
init_path_maze(&pm);

// logical floodfill
struct wall_maze lm;
struct dist_maze ldm;
init_wall_maze(&lm);
//init_distance_maze(&ldm);



/*

8
7
6
5
4
3
2
1
0 1 2 3 4 5 6 7 8 9 

Let's setup some walls
*/

// wm.cells[0][0].walls[1] = 1;
// wm.cells[1][0].walls[1] = 1;
// wm.cells[2][0].walls[1] = 1;
// wm.cells[3][0].walls[1] = 1;
// wm.cells[4][0].walls[1] = 1;
// wm.cells[5][0].walls[1] = 1;
// wm.cells[6][0].walls[1] = 1;
// wm.cells[7][0].walls[1] = 1;
// wm.cells[8][0].walls[1] = 1;
// wm.cells[9][0].walls[1] = 1;


// wm.cells[10][2].walls[1] = 1;
// wm.cells[9][2].walls[1] = 1;
// //---- other side

// wm.cells[10][2].walls[0] = 1;
// wm.cells[9][2].walls[2] = 1;


// wm.cells[11][2].walls[1] = 1;
// wm.cells[11][3].walls[3] = 1;


// wm.cells[0][1].walls[3] = 1;
// wm.cells[1][1].walls[3] = 1;
// wm.cells[2][1].walls[3] = 1;
// wm.cells[3][1].walls[3] = 1;
// wm.cells[4][1].walls[3] = 1;
// wm.cells[5][1].walls[3] = 1;
// wm.cells[6][1].walls[3] = 1;
// wm.cells[7][1].walls[3] = 1;
// wm.cells[8][1].walls[3] = 1;
// wm.cells[9][1].walls[3] = 1;
// // end of walls

// wm.cells[10][3].walls[1] = 1;
// wm.cells[9][3].walls[1] = 1;



wm.cells[3][3].walls[1] = 1;
wm.cells[3][4].walls[3] = 1;
wm.cells[3][4].walls[2] = 1;
wm.cells[4][4].walls[0] = 1;
wm.cells[0][0].walls[2] = 1;
wm.cells[1][0].walls[0] = 1;
wm.cells[0][1].walls[2] = 1;
wm.cells[1][1].walls[0] = 1;
wm.cells[0][2].walls[2] = 1;
wm.cells[1][2].walls[0] = 1;
wm.cells[1][0].walls[1] = 1;
wm.cells[1][1].walls[3] = 1;
wm.cells[1][1].walls[2] = 1;
wm.cells[2][1].walls[0] = 1;
wm.cells[1][3].walls[2] = 1;
wm.cells[2][3].walls[0] = 1;
wm.cells[1][3].walls[1] = 1;
wm.cells[1][4].walls[3] = 1;
wm.cells[2][3].walls[1] = 1;
wm.cells[2][4].walls[3] = 1;
wm.cells[2][3].walls[2] = 1;
wm.cells[3][3].walls[0] = 1;
wm.cells[3][2].walls[1] = 1;
wm.cells[3][3].walls[3] = 1;
wm.cells[2][1].walls[2] = 1;
wm.cells[3][1].walls[0] = 1;
wm.cells[3][1].walls[1] = 1;
wm.cells[3][2].walls[3] = 1;
wm.cells[4][0].walls[1] = 1;
wm.cells[4][1].walls[3] = 1;
wm.cells[4][1].walls[2] = 1;
wm.cells[5][1].walls[0] = 1;
wm.cells[4][2].walls[2] = 1;
wm.cells[5][2].walls[0] = 1;
wm.cells[4][3].walls[2] = 1;
wm.cells[5][3].walls[0] = 1;
wm.cells[5][3].walls[1] = 1;
wm.cells[5][4].walls[3] = 1;
wm.cells[5][0].walls[1] = 1;
wm.cells[5][1].walls[3] = 1;
wm.cells[6][0].walls[1] = 1;
wm.cells[6][1].walls[3] = 1;
wm.cells[7][0].walls[1] = 1;
wm.cells[7][1].walls[3] = 1;
wm.cells[8][0].walls[1] = 1;
wm.cells[8][1].walls[3] = 1;
wm.cells[6][1].walls[1] = 1;
wm.cells[6][2].walls[3] = 1;
wm.cells[7][1].walls[1] = 1;
wm.cells[7][2].walls[3] = 1;
wm.cells[7][2].walls[2] = 1;
wm.cells[8][2].walls[0] = 1;
wm.cells[7][3].walls[2] = 1;
wm.cells[8][3].walls[0] = 1;
wm.cells[6][2].walls[1] = 1;
wm.cells[6][3].walls[3] = 1;
wm.cells[6][3].walls[2] = 1;
wm.cells[7][3].walls[0] = 1;
wm.cells[5][4].walls[1] = 1;
wm.cells[5][5].walls[3] = 1;
wm.cells[6][4].walls[1] = 1;
wm.cells[6][5].walls[3] = 1;
wm.cells[7][4].walls[1] = 1;
wm.cells[7][5].walls[3] = 1;
wm.cells[8][4].walls[1] = 1;
wm.cells[8][5].walls[3] = 1;
wm.cells[8][3].walls[2] = 1;
wm.cells[9][3].walls[0] = 1;
wm.cells[8][2].walls[2] = 1;
wm.cells[9][2].walls[0] = 1;
wm.cells[9][2].walls[1] = 1;
wm.cells[9][3].walls[3] = 1;
wm.cells[9][0].walls[2] = 1;
wm.cells[10][0].walls[0] = 1;
wm.cells[10][1].walls[2] = 1;
wm.cells[11][1].walls[0] = 1;
wm.cells[11][0].walls[1] = 1;
wm.cells[11][1].walls[3] = 1;
wm.cells[12][1].walls[2] = 1;
wm.cells[13][1].walls[0] = 1;
wm.cells[12][2].walls[2] = 1;
wm.cells[13][2].walls[0] = 1;
wm.cells[13][2].walls[1] = 1;
wm.cells[13][3].walls[3] = 1;
wm.cells[11][2].walls[2] = 1;
wm.cells[12][2].walls[0] = 1;
wm.cells[11][2].walls[1] = 1;
wm.cells[11][3].walls[3] = 1;
wm.cells[11][3].walls[2] = 1;
wm.cells[12][3].walls[0] = 1;
wm.cells[11][3].walls[1] = 1;
wm.cells[11][4].walls[3] = 1;
wm.cells[13][3].walls[1] = 1;
wm.cells[13][4].walls[3] = 1;
wm.cells[10][5].walls[2] = 1;
wm.cells[11][5].walls[0] = 1;
wm.cells[11][5].walls[2] = 1;
wm.cells[12][5].walls[0] = 1;
wm.cells[9][5].walls[2] = 1;
wm.cells[10][5].walls[0] = 1;
wm.cells[10][5].walls[1] = 1;
wm.cells[10][6].walls[3] = 1;
wm.cells[11][4].walls[1] = 1;
wm.cells[11][5].walls[3] = 1;
wm.cells[13][4].walls[1] = 1;
wm.cells[13][5].walls[3] = 1;
wm.cells[13][5].walls[1] = 1;
wm.cells[13][6].walls[3] = 1;
wm.cells[13][6].walls[1] = 1;
wm.cells[13][7].walls[3] = 1;
wm.cells[13][7].walls[1] = 1;
wm.cells[13][8].walls[3] = 1;
wm.cells[11][6].walls[1] = 1;
wm.cells[11][7].walls[3] = 1;
wm.cells[11][7].walls[2] = 1;
wm.cells[12][7].walls[0] = 1;
wm.cells[11][7].walls[1] = 1;
wm.cells[11][8].walls[3] = 1;
wm.cells[8][6].walls[2] = 1;
wm.cells[9][6].walls[0] = 1;
wm.cells[8][8].walls[2] = 1;
wm.cells[9][8].walls[0] = 1;
wm.cells[11][8].walls[1] = 1;
wm.cells[11][9].walls[3] = 1;
wm.cells[10][8].walls[1] = 1;
wm.cells[10][9].walls[3] = 1;
wm.cells[8][8].walls[1] = 1;
wm.cells[8][9].walls[3] = 1;
wm.cells[7][8].walls[1] = 1;
wm.cells[7][9].walls[3] = 1;
wm.cells[6][8].walls[1] = 1;
wm.cells[6][9].walls[3] = 1;
wm.cells[5][6].walls[2] = 1;
wm.cells[6][6].walls[0] = 1;
wm.cells[6][5].walls[1] = 1;
wm.cells[6][6].walls[3] = 1;
wm.cells[7][5].walls[1] = 1;
wm.cells[7][6].walls[3] = 1;
wm.cells[7][6].walls[2] = 1;
wm.cells[8][6].walls[0] = 1;
wm.cells[7][7].walls[2] = 1;
wm.cells[8][7].walls[0] = 1;
wm.cells[7][7].walls[1] = 1;
wm.cells[7][8].walls[3] = 1;
wm.cells[6][7].walls[1] = 1;
wm.cells[6][8].walls[3] = 1;
wm.cells[5][7].walls[1] = 1;
wm.cells[5][8].walls[3] = 1;
wm.cells[4][7].walls[2] = 1;
wm.cells[5][7].walls[0] = 1;
wm.cells[4][6].walls[2] = 1;
wm.cells[5][6].walls[0] = 1;
wm.cells[4][5].walls[1] = 1;
wm.cells[4][6].walls[3] = 1;
wm.cells[3][5].walls[2] = 1;
wm.cells[4][5].walls[0] = 1;
wm.cells[0][4].walls[1] = 1;
wm.cells[0][5].walls[3] = 1;
wm.cells[1][4].walls[1] = 1;
wm.cells[1][5].walls[3] = 1;
wm.cells[2][4].walls[1] = 1;
wm.cells[2][5].walls[3] = 1;
wm.cells[2][5].walls[2] = 1;
wm.cells[3][5].walls[0] = 1;
wm.cells[2][5].walls[1] = 1;
wm.cells[2][6].walls[3] = 1;
wm.cells[1][5].walls[1] = 1;
wm.cells[1][6].walls[3] = 1;
wm.cells[0][6].walls[1] = 1;
wm.cells[0][7].walls[3] = 1;
wm.cells[0][7].walls[2] = 1;
wm.cells[1][7].walls[0] = 1;
wm.cells[0][8].walls[2] = 1;
wm.cells[1][8].walls[0] = 1;
wm.cells[0][9].walls[2] = 1;
wm.cells[1][9].walls[0] = 1;
wm.cells[0][9].walls[1] = 1;
wm.cells[0][10].walls[3] = 1;
wm.cells[1][7].walls[2] = 1;
wm.cells[2][7].walls[0] = 1;
wm.cells[2][7].walls[1] = 1;
wm.cells[2][8].walls[3] = 1;
wm.cells[2][8].walls[2] = 1;
wm.cells[3][8].walls[0] = 1;
wm.cells[3][6].walls[1] = 1;
wm.cells[3][7].walls[3] = 1;
wm.cells[3][7].walls[2] = 1;
wm.cells[4][7].walls[0] = 1;
wm.cells[3][8].walls[2] = 1;
wm.cells[4][8].walls[0] = 1;
wm.cells[4][8].walls[1] = 1;
wm.cells[4][9].walls[3] = 1;
wm.cells[4][9].walls[2] = 1;
wm.cells[5][9].walls[0] = 1;
wm.cells[1][10].walls[2] = 1;
wm.cells[2][10].walls[0] = 1;
wm.cells[1][10].walls[1] = 1;
wm.cells[1][11].walls[3] = 1;
wm.cells[1][11].walls[1] = 1;
wm.cells[1][12].walls[3] = 1;
wm.cells[2][11].walls[2] = 1;
wm.cells[3][11].walls[0] = 1;
wm.cells[0][12].walls[1] = 1;
wm.cells[0][13].walls[3] = 1;
wm.cells[1][12].walls[1] = 1;
wm.cells[1][13].walls[3] = 1;
wm.cells[3][12].walls[1] = 1;
wm.cells[3][13].walls[3] = 1;
wm.cells[4][11].walls[2] = 1;
wm.cells[5][11].walls[0] = 1;
wm.cells[3][10].walls[2] = 1;
wm.cells[4][10].walls[0] = 1;
wm.cells[3][12].walls[2] = 1;
wm.cells[4][12].walls[0] = 1;
wm.cells[5][11].walls[1] = 1;
wm.cells[5][12].walls[3] = 1;
wm.cells[5][12].walls[2] = 1;
wm.cells[6][12].walls[0] = 1;
wm.cells[5][12].walls[1] = 1;
wm.cells[5][13].walls[3] = 1;
wm.cells[5][10].walls[1] = 1;
wm.cells[5][11].walls[3] = 1;
wm.cells[6][10].walls[1] = 1;
wm.cells[6][11].walls[3] = 1;
wm.cells[6][11].walls[2] = 1;
wm.cells[7][11].walls[0] = 1;
wm.cells[7][11].walls[1] = 1;
wm.cells[7][12].walls[3] = 1;
wm.cells[7][11].walls[2] = 1;
wm.cells[8][11].walls[0] = 1;
wm.cells[7][10].walls[2] = 1;
wm.cells[8][10].walls[0] = 1;
wm.cells[7][9].walls[1] = 1;
wm.cells[7][10].walls[3] = 1;
wm.cells[6][9].walls[1] = 1;
wm.cells[6][10].walls[3] = 1;
wm.cells[8][9].walls[2] = 1;
wm.cells[9][9].walls[0] = 1;
wm.cells[8][10].walls[2] = 1;
wm.cells[9][10].walls[0] = 1;
wm.cells[8][12].walls[2] = 1;
wm.cells[9][12].walls[0] = 1;
wm.cells[8][13].walls[2] = 1;
wm.cells[9][13].walls[0] = 1;
wm.cells[8][12].walls[1] = 1;
wm.cells[8][13].walls[3] = 1;
wm.cells[7][12].walls[1] = 1;
wm.cells[7][13].walls[3] = 1;
wm.cells[9][10].walls[1] = 1;
wm.cells[9][11].walls[3] = 1;
wm.cells[9][10].walls[2] = 1;
wm.cells[10][10].walls[0] = 1;
wm.cells[10][9].walls[1] = 1;
wm.cells[10][10].walls[3] = 1;
wm.cells[9][11].walls[1] = 1;
wm.cells[9][12].walls[3] = 1;
wm.cells[10][11].walls[1] = 1;
wm.cells[10][12].walls[3] = 1;
wm.cells[10][12].walls[1] = 1;
wm.cells[10][13].walls[3] = 1;
wm.cells[11][12].walls[1] = 1;
wm.cells[11][13].walls[3] = 1;
wm.cells[12][12].walls[1] = 1;
wm.cells[12][13].walls[3] = 1;
wm.cells[12][12].walls[2] = 1;
wm.cells[13][12].walls[0] = 1;
wm.cells[12][11].walls[2] = 1;
wm.cells[13][11].walls[0] = 1;
wm.cells[12][10].walls[1] = 1;
wm.cells[12][11].walls[3] = 1;
wm.cells[13][9].walls[1] = 1;
wm.cells[13][10].walls[3] = 1;
wm.cells[8][5].walls[1] = 1;
wm.cells[8][6].walls[3] = 1;
wm.cells[10][6].walls[1] = 1;
wm.cells[10][7].walls[3] = 1;
wm.cells[9][7].walls[2] = 1;
wm.cells[10][7].walls[0] = 1;
wm.cells[13][8].walls[1] = 1;
wm.cells[13][9].walls[3] = 1;
wm.cells[10][10].walls[1] = 1;
wm.cells[10][11].walls[3] = 1;
wm.cells[11][11].walls[1] = 1;
wm.cells[11][12].walls[3] = 1;
wm.cells[11][10].walls[1] = 1;
wm.cells[11][11].walls[3] = 1;
wm.cells[10][10].walls[2] = 1;
wm.cells[11][10].walls[0] = 1;
wm.cells[11][10].walls[2] = 1;
wm.cells[12][10].walls[0] = 1;
wm.cells[10][7].walls[1] = 1;
wm.cells[10][8].walls[3] = 1;
wm.cells[9][4].walls[1] = 1;
wm.cells[9][5].walls[3] = 1;
wm.cells[10][3].walls[1] = 1;
wm.cells[10][4].walls[3] = 1;
wm.cells[12][1].walls[1] = 1;
wm.cells[12][2].walls[3] = 1;
wm.cells[10][1].walls[1] = 1;
wm.cells[10][2].walls[3] = 1;
wm.cells[9][1].walls[1] = 1;
wm.cells[9][2].walls[3] = 1;
wm.cells[1][12].walls[2] = 1;
wm.cells[2][12].walls[0] = 1;
wm.cells[0][11].walls[2] = 1;
wm.cells[1][11].walls[0] = 1;
wm.cells[2][8].walls[1] = 1;
wm.cells[2][9].walls[3] = 1;
wm.cells[2][9].walls[2] = 1;
wm.cells[3][9].walls[0] = 1;


int direction;
int j = 0;
struct coor tr;
tr.x =0;
tr.y =0;
init_distance_maze(&rm, &tr, 0);


while(j < 4){

	j++;

	xy.x = 0;
	xy.y = 0;
	st.index = 0;
	direction = modified_floodfill(&wm, &dm , &xy, &tm, 1 , 1, &st);

	// Turn 180*

	print_distance_maze(&dm);

	// switch(direction)
	// {
	//    case NORTH: direction = 2;
	//    xy.x = xy.x - 1;
	//    break;
	//    case EAST: direction = 3;
	//    xy.y = xy.y - 1;
	//    break;
	//    case SOUTH: direction = 0;
	//    xy.x = xy.x + 1;
	//    break;
	//    case WEST: direction = 1;
	//    xy.y = xy.y + 1;
	//    default:
	//    break;
	// }
	        


	

	
	st.index = 0;
	direction = modified_floodfill(&wm, &rm , &xy, &tm, 1 , direction, &st);
	print_distance_maze(&rm);


// xy.x = 0;
// xy.y = -1;
// st.index = 0;

// int direction = floodFill(&dm, &xy, &wm, &tm ,1, 1, &st);
// print_distance_maze(&dm);

}
return 0;
}
