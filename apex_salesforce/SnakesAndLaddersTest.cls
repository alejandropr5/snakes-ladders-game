@isTest
public class SnakesAndLaddersTest {
    @isTest static void tesRollDice() {
        Integer diceVal = SnakesAndLadders.rollDice();
        System.assert((diceVal >= 1) && (diceVal <= 6));
    }
        
    @isTest static void testFirstStep() {
        Integer newPos = SnakesAndLadders.setGameState(0, 1);
        System.assertEquals(1,newPos);
    }

    @isTest static void testSecondtStep() {
        Integer newPos = SnakesAndLadders.setGameState(1, 2);
        System.assertEquals(11,newPos);
    }

    @isTest static void testThirdStep() {
        Integer newPos = SnakesAndLadders.setGameState(11, 5);
        System.assertEquals(16,newPos);
    }  
    
    @isTest static void testFourthStep() {
        Integer newPos = SnakesAndLadders.setGameState(16, 4);
        System.assertEquals(20,newPos);
    } 
    
    @isTest static void testFifthStep() {
        Integer newPos = SnakesAndLadders.setGameState(20, 2);
        System.assertEquals(20,newPos);
    }
    
    @isTest static void testSixthStep() {
        Integer newPos = SnakesAndLadders.setGameState(20, 6);
        System.assert(newPos > 25);
    }      
}