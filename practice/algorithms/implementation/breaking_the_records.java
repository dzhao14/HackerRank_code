import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Solution {

	static int bests(List<Integer> scores) {
		if (scores.size() == 0) {
			return 0;
		}
		int count = 0;
		int cur = scores.get(0);
		for (int score : scores) {
			if (score > cur) {
				count += 1;
				cur = score;
			}
		}
		return count;
	}

	static int worsts(List<Integer> scores) {
		if (scores.size() == 0) {
			return 0;
		}
		int count = 0;
		int cur = scores.get(0);
		for (int score: scores) {
			if (score < cur) {
				count += 1;
				cur = score;
			}
		}
		return count;
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		List<Integer> scores = new ArrayList<Integer>();
		int n = scan.nextInt();
		for (int i = 0; i < n; i++) {
			int score = scan.nextInt();
			scores.add(score);
		}
		Integer improve = bests(scores);
		Integer sucks = worsts(scores);
		System.out.println(improve.toString() + " " + sucks.toString());
	}

}
