package tema2;

public class WordBreak {

    private static void wordBreak(String word) {
        wordBreakUtil(word, word.length(), "");
    }

    private static void wordBreakUtil(String word, int length, String result) {

        for (int i = 1; i <= length; i++) {
            String prefix = word.substring(0, i);
            if (dictionaryContains(prefix)) {
                // si no hay más elementos, imprímalo
                if (i == length) {
                    // agregar este elemento al prefijo anterior
                    result += prefix;
                    System.out.println(result);
                    return;
                }
                wordBreakUtil(word.substring(i, length), length - i, result + prefix + " ");
            }
        }
    }

    private static boolean dictionaryContains(String prefix) {
        String dictionary[] = {"mobile", "samsung", "sam", "sung", "man",
            "mango", "icecream", "and", "go", "i", "love", "ice", "cream"};
        int n = dictionary.length;
        for (int i = 0; i < n; i++) {
            if (dictionary[i].compareTo(prefix) == 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("*Primera prueba:");
        String word = "iloveicecreamandmango";
        wordBreak(word);
        System.out.println("*Segunda prueba:");
        String word1 = "ilovesamsungmobile";
        wordBreak(word1);
    }
}
