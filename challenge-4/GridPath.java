public class GridPath {

/** Initialized in the constructor with distinct values that never change */
private int[][] grid;
/**
* Returns the Location representing a neighbor of the grid element at row and col,
* as described in part (a)
* Preconditions: row is a valid row index and col is a valid column index in grid.
* row and col do not specify the element in the last row and last column of grid.
*/
public Location getNextLoc(int row, int col) { 
    if (row == this.grid.length()) {
        return new Location(row, col + 1);
    } else if (col == this.grid[row].length()) {
        return new Location(row + 1, col);
    } else if this.grid[row][col + 1] < this.grid[row][col] {
        return new Location(row, col + 1);
    } else {
        return new Location(row + 1, col);
    }
}
/**
* Computes and returns the sum of all values on a path through grid, as described in
* part (b)
* Preconditions: row is a valid row index and col is a valid column index in grid.
* row and col do not specify the element in the last row and last column of grid.
*/
public int sumPath(int row, int col)
{ /* to be implemented in part (b) */ }
// There may be instance variables, constructors, and methods that are not shown.
}