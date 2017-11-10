import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		List<Integer> heights = new ArrayList<Integer>();
		for (int i=0; i<n; i++) {
			int height = scan.nextInt();
			heights.add(height);
		}
		int maxval = Collections.max(heights);
		int counts = 0;
		for (int i : heights) {
			if (i == maxval) {
				counts += 1;
			}
		}
		System.out.println(counts);
	}

}
