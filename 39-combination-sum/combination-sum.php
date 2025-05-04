class Solution {

	/**
	* @param Integer[] $candidates
	* @param Integer $target
	* @return Integer[][]
	*/
	function combinationSum($candidates, $target) {

		$backtrack = function($comb, $curSum, $index) use ($target, $candidates, &$ans, &$backtrack) {

			if ($curSum == $target) {
				$ans[] = $comb;
				return;
			}

			if ($curSum > $target || $index >= count($candidates)) {
				return;
			}

			for ($i = $index; $i < count($candidates); $i++) {

				if ($curSum + $candidates[$i] <= $target) {
					$comb[] = $candidates[$i];
					$backtrack($comb, $curSum+$candidates[$i], $i);
					array_pop($comb);
				}

			}
		};

		$ans = [];
		$backtrack([], 0, 0);
		return $ans;

	}
}