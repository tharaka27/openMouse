#include "flood.h"
#include <algorithm> 


void init_path_maze(struct path_maze* pm){
    for(int i =0; i<SIZE;i++){
        for(int j=0; j<SIZE; j++){
            pm->maze[i][j] = false;           
        }
    }
}


void init_distance_maze(struct dist_maze* dm, struct coor* c,int center){
    if(center == 1){

        for(int i =0; i<SIZE;i++){
            for(int j=0; j<SIZE; j++){
                if(i<=SIZE/2 -1 && j<=SIZE/2 -1) dm->distance[i][j] = ((SIZE/2 -1-i) + (SIZE/2 -1-j));
    			if(i<=SIZE/2 -1 && j>SIZE/2 -1) dm->distance[i][j] = ((SIZE/2 -1-i) + (j-SIZE/2));
    			if(i>SIZE/2 -1 && j<=SIZE/2 -1) dm->distance[i][j] = ((i-SIZE/2 ) + (SIZE/2 -1-j));
    			if(i>SIZE/2 -1 && j>SIZE/2 -1) dm->distance[i][j] = ((i-SIZE/2) + (j-SIZE/2 ));
            }
        }
    }

    else
    {
        for(int i=0; i<14; i++)
        {
            for(int j=0; j<14; j++)
            {
                // get the distance to target cell
                int x = i - c->x;
                if(x<0) x = -x;
                int y = j - c->y;
                if(y<0) y = -y;
                dm->distance[i][j] = x + y;
            }
        }
    }
    
}






void init_wall_maze(struct wall_maze* wm){
	for(int i=0; i<SIZE ; i++)
	{
		for(int j=0; j<SIZE ; j++)
		{
			wm->cells[i][j].walls[NORTH] = 0;
			wm->cells[i][j].walls[EAST] = 0;
			wm->cells[i][j].walls[SOUTH] = 0;
			wm->cells[i][j].walls[WEST] = 0;
			wm->cells[i][j].visited = 0;

			// put the walls surrounding the maze
			if(i==0) wm->cells[i][j].walls[NORTH] = 1;
			if(j==0) wm->cells[i][j].walls[WEST] = 1;
			if(i==13) wm->cells[i][j].walls[SOUTH] = 1;
			if(j==13) wm->cells[i][j].walls[EAST] = 1;
		}
	}

}

void init_coor(struct coor* c, int x, int y){
	c->x = x;
	c->y = y;
}

struct coor pop_stack(struct stack* s){
    if(s->index == 0 ) 
    {
        //std::cout << "stack is empty";
        exit(1);
    } 
	s->index = s->index -1;
    return s->array[s->index + 1];
}

void push_stack(struct stack* s, struct coor c){
    
    if(s->index >= STACK_MAX) 
    {
        //std::cout << "stack full";
        exit(1);
    }
	s->index = s->index +1;
	s->array[s->index] = c;
}


bool is_stack_empty(struct stack* s){
    bool isEmpty = false;
    if(s->index == 0){
        isEmpty = true;
    }
    return isEmpty;
}


int modified_floodfill(struct wall_maze* tm, struct dist_maze* dm, struct coor* c, struct wall_maze* wm, int a, int direction, struct stack* upst){
    
    int counter = 0;

    int x = c->x ;
    int y = c->y ;

    int next_move;
    struct coor next;
    
    int j = 0; 
    while(1)
    { 

        //print_distance_maze(dm);
        switch(direction)
        {
            case NORTH: c->x -= 1;
            break;
            case EAST: c->y +=1;
            break;
            case SOUTH: c->x +=1;
            break;
            case WEST: c->y -=1;
            default:
            break;
        }
        

        if(wm->cells[c->x][c->y].visited == 0){

            // move one cell forward

            //update wall data
            // forward walls

            if(tm->cells[c->x][c->y].walls[direction] == 1)
            {    
                
                // put wall ahead of us
                wm->cells[c->x][c->y].walls[direction] = 1;

                // put wall ahead of us in the cell ahead of us

                switch(direction)
                {
                case NORTH:
                    if(c->x-1 > -1) wm->cells[c->x-1][c->y].walls[SOUTH] = 1;
                    break;
                case EAST:
                    if(c->y+1 < 14) wm->cells[c->x][c->y+1].walls[WEST] = 1;
                    break;
                case SOUTH:
                    if(c->x+1 < 14) wm->cells[c->x+1][c->y].walls[NORTH] = 1;
                    break;
                case WEST:
                    if(c->y-1 > -1) wm->cells[c->x][c->y-1].walls[EAST] = 1;
                    break;
                }


            }


            // left side walls
           
            int left_to_direction ;
            switch(direction){
                case 0: left_to_direction = 3;
                break;
                case 3: left_to_direction = 2;
                break;
                case 2: left_to_direction = 1;
                break;
                case 1: left_to_direction = 0;
                break;
            }


             if(tm->cells[c->x][c->y].walls[left_to_direction] == 1)
            {   
                // put wall ahead of us
                wm->cells[c->x][c->y].walls[left_to_direction] = 1;

                // put wall ahead of us in the cell ahead of us
                switch(left_to_direction)
                {
                case NORTH:
                    if(c->x-1 > -1) wm->cells[c->x-1][c->y].walls[SOUTH] = 1;
                    break;
                case EAST:
                    if(c->y+1 < 14) wm->cells[c->x][c->y+1].walls[WEST] = 1;
                    break;
                case SOUTH:
                    if(c->x+1 < 14) wm->cells[c->x+1][c->y].walls[NORTH] = 1;
                    break;
                case WEST:
                    if(c->y-1 > -1) wm->cells[c->x][c->y-1].walls[EAST] = 1;
                    break;
                }


            }

            // right side walls
            int right_to_direction = 0;
            switch(direction){
                case NORTH: right_to_direction = 1;
                break;
                case EAST: right_to_direction = 2;
                break;
                case SOUTH: right_to_direction = 3;
                break;
                case WEST: right_to_direction = 0;
                break;
            }


            if(tm->cells[c->x][c->y].walls[right_to_direction] == 1)
            {
                
                // put wall ahead of us
                wm->cells[c->x][c->y].walls[right_to_direction] = 1;

                // put wall ahead of us in the cell ahead of us
                switch(right_to_direction)
                {
                case NORTH:
                    if(c->x-1 > -1) wm->cells[c->x-1][c->y].walls[SOUTH] = 1;
                    break;
                case EAST:
                    if(c->y+1 < 14) wm->cells[c->x][c->y+1].walls[WEST] = 1;
                    break;
                case SOUTH:
                    if(c->x+1 < 14) wm->cells[c->x+1][c->y].walls[NORTH] = 1;
                    break;
                case WEST:
                    if(c->y-1 > -1) wm->cells[c->x][c->y-1].walls[EAST] = 1;
                    break;
                }


            }

            //debug
            std::cout << "Mouse_cell  (" << c->x << "," << c->y << ")," ;
            std::cout << "direction " << direction ;
            std::cout << ",left_direction " << left_to_direction ;
            std::cout << ",right_direction " << right_to_direction ;
            std::cout << ",forward_wall " << wm->cells[c->x][c->y].walls[direction] ;
            std::cout << ",left_wall  " << wm->cells[c->x][c->y].walls[left_to_direction] ;
            std::cout << ",right_wall " << wm->cells[c->x][c->y].walls[right_to_direction] << std::endl;

            wm->cells[c->x][c->y].visited = 1;

            counter++;
        }
        else{

            // if this cell is already visited before no need to update
            // wall data again.


            /*
                Test Function 

                Usually we come to this "else" statement. No idea how to interact i this condition
                Here are the some tried by Tharaka Ratnayake

                format 
                1. Test ID - Condition - Success/Failure
                   // Code 

                
                1. Test 1 -  - 


            */
            //debug
            // move one cell forward

            //update wall data
            // forward walls




            // left side walls
           
            int left_to_direction ;
            switch(direction){
                case 0: left_to_direction = 3;
                break;
                case 3: left_to_direction = 2;
                break;
                case 2: left_to_direction = 1;
                break;
                case 1: left_to_direction = 0;
                break;
            }


            // right side walls
            int right_to_direction = 0;
            switch(direction){
                case NORTH: right_to_direction = 1;
                break;
                case EAST: right_to_direction = 2;
                break;
                case SOUTH: right_to_direction = 3;
                break;
                case WEST: right_to_direction = 0;
                break;
            }

            //debug
            std::cout << "Mouse_cell  (" << c->x << "," << c->y << ")," ;
            std::cout << "direction " << direction ;
            std::cout << ",left_direction " << left_to_direction ;
            std::cout << ",right_direction " << right_to_direction ;
            std::cout << ",forward_wall " << wm->cells[c->x][c->y].walls[direction] ;
            std::cout << ",left_wall  " << wm->cells[c->x][c->y].walls[left_to_direction] ;
            std::cout << ",right_wall " << wm->cells[c->x][c->y].walls[right_to_direction] << std::endl;

            //continue;
            counter++;

        }

        if(dm->distance[c->x][c->y] == 0)
        {
            // Wade goda fuck off bitches!!!
            std::cout << "Done and Dusted   !!!!"  << std::endl;
            break;
        }
        
        push_stack(upst, *c);
        next_move = UpdateAndNextMove(dm,wm,c,upst,a);
        
        // First turn to face the correct direction
        int difference = direction - next_move;
        switch(difference)
        {
        case -3:
           //Turn left 90
            break;
        case -2:
            //Turn left 180
            break;
        case -1:
           //Turn right 90
            break;
        case 0:
           // do nothing
            break;
        case 1:
            //Turn left 90
            break;
        case 2:
            //Turn right 180
            break;
        case 3:
            //Turn left 90
            break;
        default:
            // bla bla
            break;
        }

        // update the direction we are currently facing
        direction = next_move;

    }

    std::cout<< "Counter = " << counter<< std::endl;
    return direction;
}


int UpdateAndNextMove(struct dist_maze* dm, struct wall_maze* wm, struct coor* t, struct stack* upst , int a){
    
    //look for the PDF- "Modified floodfill algorithm" for the algorithm.

    // Updating the values
    while(!(is_stack_empty(upst))){
        struct coor g = pop_stack(upst);
        struct coor *k = &g;
        int md = minimumOpenNeighbor( dm, wm, k);

        if(md != (dm->distance[k->x][k->y] - 1)){
            
            dm->distance[k->x][k->y] = md +1 ;
            pushSurrounding(upst, k,dm);

        }

    }
    

    //method to find the next cell to go
    int target = dm->distance[t->x][t->y] - 1;

    
    int to_direction = 0;
    
    
    for(int i=0; i<4; i++)
    {
        // choice of direction preference

        //int j = (i + a) % 4;
        // If there is no wall blocking the way
        if(wm->cells[t->x][t->y].walls[i]== 0 )
        {


            switch(i)
            {
            case 0: 
                if(dm->distance[t->x-1][t->y] == target && t->x-1 > -1)
                {
                    // if the cell exists return the direction we want to move
                    to_direction = i;
                    
                    
                }
                break;
            case 1:if(dm->distance[t->x][t->y+1] == target && t->y+1 < 14)
                {
                    // if the cell exists return the direction we want to move
                    to_direction = i;
                    
                    
                }
                break;

            case 2://SOUTH
                if(dm->distance[t->x+1][t->y] == target && t->x+1 < 14)
                {
                    // if the cell exists return the direction we want to move
                    to_direction = i;
                    
                    
                }
                break;

            case 3://WEST
                if(dm->distance[t->x][t->y-1] == target && t->y-1 > -1)
                {
                    // if the cell exists return the direction we want to move
                    to_direction = i;
                    
                    
                }
                break;
            }
        }
        


        //return to_direction;
    }

    return to_direction;

}



int minimumOpenNeighbor(struct dist_maze* dm, struct wall_maze* wm, struct coor* c){
    
    // This function written to return the distance value of the neighbour open
    // cell.   
    int minimum = 200;
    for(int i=0;i< 4;i++){
        if( wm->cells[c->x][c->y].walls[i] == 0 ){
            
            switch(i)
            {
            case NORTH: 
                if(c->x-1 > -1){
                    minimum = std::min( minimum, dm->distance[c->x-1][c->y]);
                    break;
                }
                
            case EAST:  
                if(c->y+1 < 14){
                    minimum = std::min( minimum, dm->distance[c->x][c->y+1]);
                    break;
                }

            case SOUTH: 
                if(c->x+1 < 14){
                    minimum = std::min( minimum, dm->distance[c->x+1][c->y]);
                    break;
                }


            case WEST:  
                if(c->y-1 > -1){
                    minimum = std::min( minimum, dm->distance[c->x][c->y-1]);
                    break;
                }

            }
                
        }
    }

    return minimum;
}

void pushSurrounding(struct stack* s, struct coor* c , struct dist_maze* dm ){
    struct coor temp;
    if ((c->x+1 < 14 ) && ( dm->distance[c->x+1][c->y] != 0)){ 
        init_coor(&temp, c->x+1, c->y);
        push_stack(s,temp);
    }
    if ((c->y+1 < 14) && ( dm->distance[c->x][c->y+1] != 0) ){
        init_coor(&temp, c->x, c->y+1);
        push_stack(s,temp);
    }
    if ((c->x-1 >= 0) && ( dm->distance[c->x-1][c->y] != 0) ){
        init_coor(&temp, c->x-1, c->y);
        push_stack(s,temp);
    }
    if ((c->y-1 >= 0) && ( dm->distance[c->x][c->y-1] != 0) ){
        init_coor(&temp, c->x, c->y-1);
        push_stack(s,temp);
    }
}


void print_distance_maze(struct dist_maze* dm){
    for(int i=0;i<SIZE;i++){
        for(int j=0;j<SIZE;j++){
            if(dm->distance[i][j] <10) std::cout<<" ";
            std::cout << dm->distance[i][j] ;
            std::cout << " ";
            
        }
        std::cout << std::endl;
    }
}




// Return Functionality 

int nextMove(struct dist_maze* dm, struct wall_maze* wm, struct coor* c){
    
    //method to find the next cell to go
    int target = dm->distance[c->x][c->y] - 1;

    
    int to_direction = 0;
    
    // if ((c->x+1 < 14 ) && ( dm->distance[c->x+1][c->y] == target) && ( wm->cells[c->x+1][c->y].visited == 1)){
    //    to_direction = 2;        
    // }

    // if ((c->y+1 < 14) && ( dm->distance[c->x][c->y+1] == target) && ( wm->cells[c->x][c->y+1].visited == 1)){
    //     to_direction = 1; 
            
    // }
    // if ((c->x-1 >= 0) && ( dm->distance[c->x-1][c->y] == target) && ( wm->cells[c->x-1][c->y].visited == 1)){
    //     to_direction = 0; 
            
    // }
    // if ((c->y-1 >= 0) && ( dm->distance[c->x][c->y-1] == target) && ( wm->cells[c->x][c->y-1].visited == 1)){
    //     to_direction = 3; 
    // }

    
    
    std::cout<< to_direction<< std::endl;

    return to_direction;

}


int return_floodfill(struct dist_maze* dm, struct coor* c, struct wall_maze* wm, int direction, struct path_maze* pm){
    
    int x = c->x ;
    int y = c->y ;

    int next_move;
    struct coor next;

    while(1)
    {
        switch(direction)
        {
            case NORTH: c->x -= 1;
            break;
            case EAST: c->y +=1;
            break;
            case SOUTH: c->x +=1;
            break;
            case WEST: c->y -=1;
            default:
            break;
        }
        
        pm->maze[c->x][c->y] = true;

        if(dm->distance[c->x][c->y] == 0)
        {
            // Wade goda fuck off bitches!!!
            std::cout << "Done and Dusted   !!!!"  << std::endl;
            break;
        }
               
        // update the direction we are currently facing
        direction = nextMove(dm,wm,c);

    }

    
    return 1;
}

void print_path_maze(struct path_maze* pm){
    for(int i=0;i<SIZE;i++){
        for(int j=0;j<SIZE;j++){
            if (pm->maze[i][j]){
                std::cout << " T ";
            }
            else{
                std::cout << " F ";
            }
        }
        std::cout << std::endl;
    }
}


int minusOneNeighbor(struct dist_maze* dm, struct wall_maze* wm, struct coor* c, struct stack* s, int a)
{
    int i;
    // minimum distance
    int md=260;
    // get target distance we're looking for
    int target = dm->distance[c->x][c->y] - 1;
    // check neighbor cells
    for(i=0; i<4; i++)
    {
        // choice of direction preference
        int j = (i + a) % 4;
        // If there is no wall blocking the way
        if(wm->cells[c->x][c->y].walls[j]==0)
        {


            switch(j)
            {
            case NORTH:
                if(dm->distance[c->x-1][c->y]==target)
                {
                    // if the cell exists return the direction we want to move
                    return j;
                }
                if(dm->distance[c->x-1][c->y] < md) md = dm->distance[c->x-1][c->y];
                break;
            case EAST:
                if(dm->distance[c->x][c->y+1]==target)
                {
                    // if the cell exists return the direction we want to move
                    return j;
                }
                if(dm->distance[c->x][c->y+1] < md) md = dm->distance[c->x][c->y+1];
                break;
            case SOUTH:
                if(dm->distance[c->x+1][c->y]==target)
                {
                    // if the cell exists return the direction we want to move
                    return j;
                }
                if(dm->distance[c->x+1][c->y] < md) md = dm->distance[c->x+1][c->y];
                break;
            case WEST:
                if(dm->distance[c->x][c->y-1]==target)
                {
                    // if the cell exists return the direction we want to move
                    return j;
                }
                if(dm->distance[c->x][c->y-1] < md) md = dm->distance[c->x][c->y-1];
                break;
            default:

                break;
            }
        }
    }

    // update distance of coordinate to 1 plus minimum distance
    dm->distance[c->x][c->y] = md + 1;

    // Since we did not find a cell we push onto the stack
    for(i=0; i<4; i++)
    {
        // choice of direction preference
        int j = (i + a) % 4;
        // If there is no wall blocking the way
        if(wm->cells[c->x][c->y].walls[j]==0)
        {
            struct coor temp;
            switch(j)
            {
            case NORTH:
                init_coor(&temp, c->x-1, c->y );
                break;
            case EAST:
                init_coor(&temp, c->x , c->y+1);
                break;
            case SOUTH:
                init_coor(&temp, c->x+1, c->y );
                break;
            case WEST:
                init_coor(&temp, c->x , c->y-1);
                break;
            }
            push_stack(s, temp);
        }
    }
    // return unknown
    return UNKNOWN;
}


int floodFill(struct dist_maze* dm, struct coor* c, struct wall_maze* wm, struct wall_maze* tm ,int a, int direction, struct stack* upst)
{
    
    int next_move;
    struct coor next;

    while(1)
    {
        
        switch(direction)
        {
                
        
        case NORTH: c->x -= 1;
        break;
        case EAST: c->y +=1;
        break;
        case SOUTH: c->x +=1;
        break;
        case WEST: c->y -=1;
        default:
        break;

        }

        
        if(wm->cells[c->x][c->y].visited == 0)
        {
            
            if(tm->cells[c->x][c->y].walls[direction] == 1)
            {
                // put wall ahead of us
                wm->cells[c->x][c->y].walls[direction] = 1;
                switch(direction)
                {
                case NORTH:
                    if(c->x-1 > -1) wm->cells[c->x-1][c->y].walls[SOUTH] = 1;
                    break;
                case EAST:
                    if(c->y+1 < 14) wm->cells[c->x][c->y+1].walls[WEST] = 1;
                    break;
                case SOUTH:
                    if(c->x+1 < 14) wm->cells[c->x+1][c->y].walls[NORTH] = 1;
                    break;
                case WEST:
                    if(c->y-1 > -1) wm->cells[c->x][c->y-1].walls[EAST] = 1;
                    break;          
                 }
            }
               
            // left side walls
           
            int left_to_direction ;
            switch(direction){
                case 0: left_to_direction = 3;
                break;
                case 3: left_to_direction = 2;
                break;
                case 2: left_to_direction = 1;
                break;
                case 1: left_to_direction = 0;
                break;
            }


             if(tm->cells[c->x][c->y].walls[left_to_direction] == 1)
            {   
                // put wall ahead of us
                wm->cells[c->x][c->y].walls[left_to_direction] = 1;

                // put wall ahead of us in the cell ahead of us
                switch(left_to_direction)
                {
                case NORTH:
                    if(c->x-1 > -1) wm->cells[c->x-1][c->y].walls[SOUTH] = 1;
                    break;
                case EAST:
                    if(c->y+1 < 14) wm->cells[c->x][c->y+1].walls[WEST] = 1;
                    break;
                case SOUTH:
                    if(c->x+1 < 14) wm->cells[c->x+1][c->y].walls[NORTH] = 1;
                    break;
                case WEST:
                    if(c->y-1 > -1) wm->cells[c->x][c->y-1].walls[EAST] = 1;
                    break;
                }


            }

            // right side walls
            int right_to_direction = 0;
            switch(direction){
                case NORTH: right_to_direction = 1;
                break;
                case EAST: right_to_direction = 2;
                break;
                case SOUTH: right_to_direction = 3;
                break;
                case WEST: right_to_direction = 0;
                break;
            }


            if(tm->cells[c->x][c->y].walls[right_to_direction] == 1)
            {
                // put wall ahead of us
                wm->cells[c->x][c->y].walls[right_to_direction] = 1;

                // put wall ahead of us in the cell ahead of us
                switch(right_to_direction)
                {
                case NORTH:
                    if(c->x-1 > -1) wm->cells[c->x-1][c->y].walls[SOUTH] = 1;
                    break;
                case EAST:
                    if(c->y+1 < 14) wm->cells[c->x][c->y+1].walls[WEST] = 1;
                    break;
                case SOUTH:
                    if(c->x+1 < 14) wm->cells[c->x+1][c->y].walls[NORTH] = 1;
                    break;
                case WEST:
                    if(c->y-1 > -1) wm->cells[c->x][c->y-1].walls[EAST] = 1;
                    break;
                }


            }

            //debug
            std::cout << "Mouse_cell  (" << c->x << "," << c->y << ")," ;
            std::cout << "direction " << direction ;
            std::cout << ",left_direction " << left_to_direction ;
            std::cout << ",right_direction " << right_to_direction ;
            std::cout << ",forward_wall " << wm->cells[c->x][c->y].walls[direction] ;
            std::cout << ",left_wall  " << wm->cells[c->x][c->y].walls[left_to_direction] ;
            std::cout << ",right_wall " << wm->cells[c->x][c->y].walls[right_to_direction] << std::endl;


            // update the current cell as visited
            wm->cells[c->x][c->y].visited = 1;

        }
        else
        {
            // advance one cell without scanning for walls


            // left side walls
           
            int left_to_direction ;
            switch(direction){
                case 0: left_to_direction = 3;
                break;
                case 3: left_to_direction = 2;
                break;
                case 2: left_to_direction = 1;
                break;
                case 1: left_to_direction = 0;
                break;
            }


            // right side walls
            int right_to_direction = 0;
            switch(direction){
                case NORTH: right_to_direction = 1;
                break;
                case EAST: right_to_direction = 2;
                break;
                case SOUTH: right_to_direction = 3;
                break;
                case WEST: right_to_direction = 0;
                break;
            }

            //debug
            std::cout << "Mouse_cell  (" << c->x << "," << c->y << ")," ;
            std::cout << "direction " << direction ;
            std::cout << ",left_direction " << left_to_direction ;
            std::cout << ",right_direction " << right_to_direction ;
            std::cout << ",forward_wall " << wm->cells[c->x][c->y].walls[direction] ;
            std::cout << ",left_wall  " << wm->cells[c->x][c->y].walls[left_to_direction] ;
            std::cout << ",right_wall " << wm->cells[c->x][c->y].walls[right_to_direction] << std::endl;

            //continue;
        }

        // if we are at target destination
        if (dm->distance[c->x][c->y]==0)
        {
            return direction;
            break;
        }

        // check if there is a neighbor with one less distance
        // next_move is the direction we should move next
        next_move = minusOneNeighbor(dm, wm, c, upst, a);

        // If we couldn't find a valid cell
        if(next_move == UNKNOWN)
        {
            // while stack is not empty
            while(upst->index!=0)
            {

                // get the cell to test from the stack
                next = pop_stack(upst);

                // find a neighbor cell with distance one less than current
                minusOneNeighbor(dm, wm, &next, upst, a);

            }
            // get next cell to traverse to
            // next_move is actually the direction we need to go next

            next_move = minusOneNeighbor(dm, wm, c, upst, a);

        }

        // Move to next cell
        // First turn to face the correct direction
        int difference = direction - next_move;
        switch(difference)
        {
        case -3:
            break;
        case -2:
            break;
        case -1:
            break;
        case 0:
            break;
        case 1:
            break;
        case 2:
            break;
        case 3:
            break;
        default:
            break;
        }

        // update the direction we are currently facing
        direction = next_move;
    }
}