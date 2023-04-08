package Algorithm;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;

class WordTokenizationTest {

    private WordTokenization wordTokenization = new WordTokenization();

    @Test
    public void twoWordsTokenizationTest() {
        wordTokenization = new WordTokenization();
        String string = "The/Boy";
        String[] actual = wordTokenization.tokenizeString(string);
        String[] expected = {"The", "Boy"};
        assertEquals(Arrays.toString(expected), Arrays.toString(actual));
    }

    @Test
    public void threeWordsTokenizationTest() {
        wordTokenization = new WordTokenization();
        String string = "The_Bottle_Stinks";
        String[] actual = wordTokenization.tokenizeString(string);
        String[] expected = {"The", "Bottle", "Stinks"};
        assertEquals(Arrays.toString(expected), Arrays.toString(actual));
    }

    @Test
    public void fourWordsTokenizationTest() {
        wordTokenization = new WordTokenization();
        String string = "The,Boy,is,handsome";
        String[] actual = wordTokenization.tokenizeString(string);
        String[] expected = {"The", "Boy", "is", "handsome"};
        assertEquals(Arrays.toString(expected), Arrays.toString(actual));
    }

    @Test
    public void fiveWordsTokenizationTest() {
        wordTokenization = new WordTokenization();
        String string = "Ada is a beautiful girl";
        String[] actual = wordTokenization.tokenizeString(string);
        String[] expected = {"Ada", "is", "a", "beautiful", "girl"};
        assertEquals(Arrays.toString(expected), Arrays.toString(actual));
    }

    @Test
    public void sixWordsTokenizationTest() {
        wordTokenization = new WordTokenization();
        String string = "The-Boy-is-in-the-Shop";
        String[] actual = wordTokenization.tokenizeString(string);
        String[] expected = {"The", "Boy", "is", "in", "the", "Shop"};
        assertEquals(Arrays.toString(expected), Arrays.toString(actual));
    }

}