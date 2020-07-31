package reverse;

public class ReverseWords {

    public static void main(String[] args) {
        String word = "mother was washing a window";
        System.out.println(reverseWords(word));
    }

    public static String reverseWords(String input) {
        char[] reversed = reverseChars(input.toCharArray(), 0, input.length() - 1);
        int spaceIndex = -1;
        for (int i = 0; i < reversed.length; i++) {
            if (reversed[i] == ' ') {
                reverseChars(reversed, spaceIndex + 1, i - 1);
            }

            while(i < reversed.length && reversed[i] == ' ') {
                spaceIndex = i;
                i++;
            }

            if (i == reversed.length - 1) {
                reverseChars(reversed, spaceIndex + 1, i);
            }

        }
        return String.valueOf(reversed);
    }

    public static char[] reverseChars(char[] chars, int from, int to) {
        int forward = from;
        int backwards = to;

        char temp;
        while(forward < backwards) {
            temp = chars[backwards];
            chars[backwards] = chars[forward];
            chars[forward] = temp;
            forward++;
            backwards--;
        }
        return chars;
    }

}
