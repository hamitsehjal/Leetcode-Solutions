class Solution {

	/**
	* @param Integer[] $nums
	* @return Integer[][]
	*/
	function permute($nums) {
		$n = count($nums);
		$ans = [];
		$set = [];
		$this->backtrack([], $ans, $set, $n, $nums);
		return $ans;
	}

	function backtrack($cur, &$ans, $set, $n, $nums) {
		if (count($cur) === $n) {
			$ans[] = $cur;
		}

		foreach ($nums as $num) {
			if (!array_key_exists($num, $set)) {
				$cur[] = $num;
				$set[$num] = True;
				$this->backtrack($cur, $ans, $set, $n, $nums);
				unset($set[array_pop($cur)]);
			}
		}
	}
}