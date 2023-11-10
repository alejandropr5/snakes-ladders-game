/**
* Class for implementing methods to play the snakes and ladders board game.
*
* @param  snakes  a map for board snakes, keys: snake heads, values: snake tails
* @param  ladders  a map for board ladders, keys: ladder start, values: ladder end
*/
public class SnakesAndLadders {  
    private static Map<Integer, Integer> snakes = new Map<Integer, Integer>{
        14 => 4,
        19 => 8,
        22 => 20,
        24 => 16
    };
 
    private static Map<Integer, Integer> ladders = new Map<Integer, Integer>{
        3 => 11,
        6 => 17,
        9 => 18,
        10 => 12
    };

    /**
    * Simulates rolling a dice, returning a random integer between 1 and 6
    * @return  Random integer between 1 and 6
    */
    public static Integer rollDice (){
        return Math.round((Math.random() * 6));
    }

    /**
    * Given the initial position, and the positions to move returns the new position.
    * taking into account whether it falls on snake or ladder
    * @param  newPos  The new position
    * @return  The new position
    */
    public static Integer setGameState (Integer initPos, Integer movement){
        Integer newPos = initPos + movement;
        if (newPos <= 25) {
            if (snakes.keySet().contains(newPos)){
                newPos = snakes.get(newPos);
            }
            if (ladders.keySet().contains(newPos)){
                newPos = ladders.get(newPos);
            }          	
        }
        return newPos;
    }   
}