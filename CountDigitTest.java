package Algorithm;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CountDigitTest {

    @Test
    public void countNumberOfDigitsFirstTest() {
        CountDigit countDigit = new CountDigit();
        String[] theArray = {"Ab1U96", "Q2RBS", "G381ac"};
        int actual = countDigit.returnDigit(theArray);
        int expected = 7;
        assertEquals(expected, actual);
    }

    @Test
    public void countNumberOfDigitsSecondTest() {
        CountDigit countDigit = new CountDigit();
        String[] theArray = {"A21U96", "Q2RBS", "1381ac"};
        int actual = countDigit.returnDigit(theArray);
        int expected = 9;
        assertEquals(expected, actual);
    }
}