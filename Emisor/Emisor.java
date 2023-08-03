class ComputeHammingCode {

    public static String computeHammingCode(String data) {
        int r = calculateRedundantBits(data.length());
        String arr = addRedundantBits(data, r);
        arr = calculateParityBits(arr, r);
        return arr;
    }

    public static int calculateRedundantBits(int m) {
        for (int i = 0; i < m; i++) {
            if (Math.pow(2, i) >= m + i + 1) {
                return i;
            }
        }
        return 0;
    }

    public static String addRedundantBits(String data, int r) {
        int j = 0;
        int k = 1;
        int m = data.length();
        StringBuilder res = new StringBuilder();

        for (int i = 1; i <= m + r; i++) {
            if (i == Math.pow(2, j)) {
                res.append('0');
                j++;
            } else {
                res.append(data.charAt(m - k));
                k++;
            }
        }

        return res.reverse().toString();
    }

    public static String calculateParityBits(String arr, int r) {
        int n = arr.length();
        StringBuilder result = new StringBuilder(arr);

        for (int i = 0; i < r; i++) {
            int val = 0;
            for (int j = 1; j <= n; j++) {
                if ((j & (1 << i)) == (1 << i)) {
                    val ^= Integer.parseInt(String.valueOf(arr.charAt(n - j)));
                }
            }
            result.setCharAt(n - (1 << i), (char) (val + '0'));
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String data = "1011001";
        String hammingCode = computeHammingCode(data);
        System.out.println("Transferred data with Hamming code: " + hammingCode);
    }
}
