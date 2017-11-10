import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Solution {

	static List<Integer> roundUp(List<Integer> grades) {
		for(int idx = 0; idx < grades.size(); idx++) {
			int grade = grades.get(idx);
			if (grade < 38) {
				continue;
			}
			if (grade % 5 < 3) {
				continue;
			}
			else {
				grades.set(idx, grade + 5 - (grade % 5));
			}
		}
			return grades;
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		List<Integer> grades = new ArrayList<Integer>();
		Integer n = scan.nextInt();	
		for(int i=0; i < n; i++) {
			int grade = scan.nextInt();
			grades.add(grade);
		}
		grades = roundUp(grades);
		for(int i : grades) {
			System.out.println(i);
		}
	}
}
