package Receptor;
class Receptor {

    public static int calculateFletcherChecksum(String message) {
        int modulo = 255;
        int sum1 = 0;
        int sum2 = 0;
        byte[] messageBytes = message.getBytes();
        for (byte b : messageBytes) {
            sum1 = (sum1 + (b & 0xFF)) % modulo;
            sum2 = (sum2 + sum1) % modulo;
        }

        int checksum = (sum2 << 8) | sum1;

        return checksum;
    }

    public static boolean verifyFletcherChecksum(String message, int checksum) {
        int calculatedChecksum = calculateFletcherChecksum(message);
        return calculatedChecksum == checksum;
    }

    public static int calculateRedundantBits(int m) {
        for (int i = 0; i < m; i++) {
            if (Math.pow(2, i) >= m + i + 1) {
                return i;
            }
        }
        return 0;
    }

    public static int detectError(String arr, int nr) {
        int n = arr.length();
        int res = 0;
    
        for (int i = 0; i < nr; i++) {
            int val = 0;
            for (int j = 1; j <= n; j++) {
                if ((j & (1 << i)) == (1 << i)) {
                    val = val ^ Integer.parseInt(String.valueOf(arr.charAt(n - j)));
                }
            }
            res = res + val * (int) Math.pow(10, i);
        }
    
        return Integer.parseInt(Integer.toBinaryString(res), 2);
    }

    public static void main(String[] args) {
        String testMessage = "11001101111101010100101101"; // original message
        int expectedChecksum = 0xF4F4; // checksum calculated by the sender

        System.out.println("Original Message received: " + testMessage);
        int calculatedChecksum = calculateFletcherChecksum(testMessage);
        System.out.println("Calculated Checksum: 0x" + Integer.toHexString(calculatedChecksum).toUpperCase());
        System.out.println("Checksum Matches: " + verifyFletcherChecksum(testMessage, expectedChecksum));

        String modifiedMessage = "11001001111101010100101101";
        System.out.println("Modified Message received: " + modifiedMessage);
        System.out.println("Checksum Matches (Modified Message): " + verifyFletcherChecksum(modifiedMessage, expectedChecksum));

    }
}
